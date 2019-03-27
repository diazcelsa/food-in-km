import { combineReducers } from "redux";


const nameReducer = (loader = 'unkown', action) => {
    switch (action.type) {
        case 'NAME_CHANGE':
            return action.name
        default:
            return loader;
    }
}

const errorReducer = (error = [], action) => {
    switch (action.type) {
        case 'ERROR_ACKNOWLEDGED':
            return []
        case 'ERROR':
            return [{message: action.message, trace: action.trace}]
        default:
            return error;
    }
}

const locationReducer = (location={lat: 34, lon: 23}, action) => {
    switch (action.type) {
        case 'LOCATION_UPDATE':
            return {lat: action.lat, lon: action.lon}
        default:
            return location;
    }
}

let productsDummy = [
{
    'product_name' : 'Arroz',
    'price' : '1€',
    'distance': '33.4km',
    'loc' : [41.582578,0.603605]
},
{
    'product_name' : 'Chocolate',
    'price' : '130€',
    'distance': '33.4km',
    'loc' : [33.601301, 5.290211]
},
{
    'product_name' : 'TEST',
    'price' : '12€',
    'distance': '83.4km',
    'loc' : [36.803759,-2.541634]
},
]

const productsReducer = (products = productsDummy, action) => {
    switch (action.type) {
        case 'PRODUCTS_UPDATE':
            return action.products
        default:
            return products;
    }
}

const basketReducer = (basket = [], action) => {
    switch (action.type) {
        case 'BASKET_ADD':
            return [...basket, action.product]
        case 'BASKET_REMOVE':
            return [...array.slice(0, action.index), ...array.slice(action.index + 1)]
        default:
            return basket;
    }
}

const reducers = combineReducers({
    name: nameReducer,
    errors: errorReducer,
    location: locationReducer,
    products: productsReducer,
    basket: basketReducer
});

export default reducers;
