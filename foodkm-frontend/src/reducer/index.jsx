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


const locationReducer = (location={lat: 40.4, lon: -3.68}, action) => {
    switch (action.type) {
        case 'LOCATION_UPDATE':
            return {lat: action.lat, lon: action.lon, address: action.address}
        default:
            return location;
    }
}

let productsDummy = [
{
    'product_name' : 'Arroz',
    'price' : 1,
    'distance': 33.4,
    'location' : {'lat': 41.582578, 'lon': 0.603605}
},
{
    'product_name' : 'Chocolate',
    'price' : 130,
    'distance': 33.4,
    'location' : {'lat': 33.601301, 'lon': 5.290211}
},
{
    'product_name' : 'TEST',
    'price' : 12,
    'distance': 83.4,
    'location' : {'lat': 36.803759, 'lon': -2.541634}
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

const suggestReducer = (suggest = [], action) => {
    switch (action.type) {
        case 'PRODUCTS_UPDATE':
            return action.suggest
        default:
            return suggest;
    }
}


const basketReducer = (basket = [], action) => {
    switch (action.type) {
        case 'BASKET_ADD':
            return [...basket, action.product]
        case 'BASKET_REMOVE':
            return [...basket.slice(0, action.index), ...basket.slice(action.index + 1)]
        default:
            return basket;
    }
}

const reducers = combineReducers({
    name: nameReducer,
    errors: errorReducer,
    location: locationReducer,
    products: productsReducer,
    basket: basketReducer,
    suggest: suggestReducer
});

export default reducers;
