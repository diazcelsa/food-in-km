import './css/main.css';
import './css/leaflet.css';

import './images/mapa-1.png'
import './images/mapa-2.png'
import './images/mapa-3.png'
import './images/mapa-4.png'
import './images/mapa-5.png'

import React from "react";
import ReactDOM from "react-dom";


import { Provider } from "react-redux";
import { createStore, applyMiddleware, compose } from "redux";
import { createEpicMiddleware } from "redux-observable";
import logger from 'redux-logger';

import epics from "./epics";
import reducers from "./reducer";


import ErrorsContainer from './container/error';
import ProductListSearchBox from './container/ProductListSearchBox';
import ProductList from './container/ProductList';
import CardList from './container/CardList';
import MapComponent from './map/MapComponent';
import StatusBar from './container/StatusBar';
import ZIPSearch from './container/ZIPSearch';
import TabMenu from './container/TabMenu';
import { dispatch } from 'rxjs/internal/observable/pairs';


class Index extends React.Component {
    constructor() {
        super();
    }
    componentWillMount(){
    }
    componentWillUnmount() {
    }

    componentDidUpdate(){

    }

    render() {
        return (

        <div id="cart-wrapper">

            <h3>Haz tu lista de la compra</h3>
            

            <ErrorsContainer/>
            <ZIPSearch/>
            <ProductListSearchBox/>

            <div id="cart-wrapper-body">

                <div id="map-panel">
                    <MapComponent/>
                </div>

                <div id="product-list-panel">

                    <TabMenu />

                  <div className="inner">
                      <ProductList/>
                  </div>

                </div>

            </div>

            <StatusBar/>
            <CardList/>
        </div>)
    }
}

const epicMiddleware = createEpicMiddleware();

const middlewares = [
    logger,
    epicMiddleware,
];

const enhancer = compose(
    applyMiddleware(...middlewares)
);

const initalState = {};

const store = createStore(reducers, initalState, enhancer);

epicMiddleware.run(epics);


// let theMap = new map({
//     'center' : [40.4,-3.68]
// })




ReactDOM.render(
  <Provider store={store}>
    <Index />
  </Provider>,
  document.getElementById("index")
);



