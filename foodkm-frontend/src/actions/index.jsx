export const locationUpdate = ({lat, lon}) => {
    return {
      type: 'LOCATION_UPDATE',
      lat,
      lon
    };
}

export const updateProducts = (products) => {
  return {
    type: 'PRODUCTS_UPDATE',
    products
  };
}

export const searchProducts = (query) => {
    return {
        type: 'PRODUCTS_SEARCH',
        query
    };
}

export const addBasket = (product) => {
    return {
        type: 'BASKET_ADD',
        product
    };
}

export const removeBasket = (index) => {
    return {
        type: 'BASKET_REMOVE',
        index
    };
}



export const error = (message, trace) => {
  return {
    type: 'ERROR',
    message,
    trace
  };
}


export const acknowledgeError = () => {
  return {
    type: 'ERROR_ACKNOWLEDGED'
  };
}
