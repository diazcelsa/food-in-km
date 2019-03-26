import 'semantic-ui-css/semantic.min.css';

import React from "react";
import ReactDOM from "react-dom";

import { Provider } from "react-redux";
import { createStore, applyMiddleware, compose } from "redux";
import { createEpicMiddleware } from "redux-observable";
import logger from 'redux-logger';

import epics from "./epics";
import reducers from "./reducer";


import InputContainer from './container/input';
import WelcomeContainer from './container/welcome';
import ErrorsContainer from './container/error';


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
        <div>
            <ErrorsContainer/>
            <InputContainer/>
            <WelcomeContainer/>
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
