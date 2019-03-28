export const locationUpdate = ({lat, lon, address}) => {
    return {
      type: 'LOCATION_UPDATE',
      lat,
      lon,
      address
    };
}

export const backetCheckout = () => {
    return {
      type: 'CHECKOUT_BASKET',
    };
}


export const searchLocation = (query) => {
    return {
      type: 'LOCATION_SEARCH',
      query
    };
}

export const updateProducts = (products,suggest) => {
  return {
    type: 'PRODUCTS_UPDATE',
    products,
    suggest
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
