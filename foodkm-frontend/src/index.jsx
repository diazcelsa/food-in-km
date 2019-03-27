import './css/main.css';
import './css/leaflet.css';

import React from "react";
import ReactDOM from "react-dom";

import map from './map';

import { Provider } from "react-redux";
import { createStore, applyMiddleware, compose } from "redux";
import { createEpicMiddleware } from "redux-observable";
import logger from 'redux-logger';

import epics from "./epics";
import reducers from "./reducer";


import ErrorsContainer from './container/error';
import ProductListSearchBox from './container/ProductListSearchBox';
import ProductList from './container/ProductList';
import MapComponent from './container/MapComponent';
import StatusBar from './container/StatusBar';


class Index extends React.Component {
    constructor() {
        super();
    }
    componentWillMount(){
    }
    componentWillUnmount() {
    }

    render() {
        return (
        <div id="cart-wrapper">
            <ErrorsContainer/>
            <ProductListSearchBox/>

            <div id="cart-wrapper-body">

                <div id="map-panel">
                    <MapComponent/>
                </div>

                <div id="product-list-panel">
                    <div className="product-list-item header-row">
                      <div className="product-list-item-name">Producto</div>
                      <div className="product-list-item-price">Precio</div>
                      <div className="product-list-item-km">Distancia</div>
                    </div>

                    <div className="inner">
                        <ProductList/>
                    </div>
                </div>
            </div>
            <StatusBar/>
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

ReactDOM.render(
  <Provider store={store}>
    <Index />
  </Provider>,
  document.getElementById("index")
);

let theMap = new map({
    'center' : [40.4,-3.68]
})

theMap.addLocations([
  {
    'name' : 'Arroz',
    'price' : '1€',
    'distance': '33.4km',
    'loc' : [41.582578,0.603605]
  },
  {
    'name' : 'Chocolate',
    'price' : '130€',
    'distance': '33.4km',
    'loc' : [33.601301, 5.290211]
  },
  {
    'name' : 'Vino',
    'price' : '12€',
    'distance': '83.4km',
    'loc' : [36.803759,-2.541634]
  },
])
