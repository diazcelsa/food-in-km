import React from 'react'
import { connect } from 'react-redux';

const StatusBar = ({totalPrice=70,totalKM=1300,onCheckout}) => (
    <div id="status-bar">
      <div className="status-bar-title">Totales</div>
      <div className="status-bar-price">{totalPrice}€</div>
      <div className="status-bar-km">{totalKM}km</div>
      <button id="add-to-cart-button" onClick={onCheckout}>Ver carrito</button>
    </div>
)

const BasketComponent = ({basket,onCheckout}) => {
    const totalPrice = _.sum(basket.map(({price}) => price));
    const totalKM = _.sum(basket.map(({distance}) => distance));
    return (
        <StatusBar totalPrice={totalPrice} totalKM={totalKM} onCheckout={onCheckout}/>
    )
};


const BasketContainer = connect(
    (state, ownProps) => ({
        basket: state.basket
    }),
    (dispatch, ownProps) => ({
        onCheckout: (value) => dispatch(a.searchProducts(value))
    })
)(BasketComponent)

export default BasketContainer
