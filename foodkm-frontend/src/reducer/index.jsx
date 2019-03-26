import { combineReducers } from "redux";


const nameReducer = (loader = 'unkown', action) => {
    switch (action.type) {
        case 'NAME_CHANGE':
            return action.name
        default:
            return loader;
    }
}

const errorReducer = (loader = [], action) => {
    switch (action.type) {
        case 'ERROR_ACKNOWLEDGED':
            return []
        case 'ERROR':
            return [{message: action.message, trace: action.trace}]
        default:
            return loader;
    }
}


const reducers = combineReducers({
    name: nameReducer,
    errors: errorReducer
});

export default reducers;
