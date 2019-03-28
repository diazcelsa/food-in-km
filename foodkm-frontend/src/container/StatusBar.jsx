import React from 'react'
import { connect } from 'react-redux';

const StatusBar = (
        {totalPrice=70,totalKM=1300,onCheckout,totalMinRange,totalMaxRange}) => {
    const totalKMPro = (totalKM - totalMinRange) / (totalMaxRange - totalMinRange) * 100;
    return (
        <div id="status-bar">
        <div className="status-bar-title">Totales</div>
        <div className="status-bar-price">{totalPrice.toFixed(2)}€</div>
        <div className="status-bar-km">{totalKM.toFixed(0)}km</div>
        <div className="status-bar-range">{totalMinRange.toFixed(0)}km<progress max="100" value={totalKMPro.toFixed(0)}> {totalKMPro.toFixed(0)}% </progress>{totalMaxRange.toFixed(0)}km</div>
        <button className="button" id="add-to-cart-button" onClick={onCheckout}>Ver carrito</button>
        </div>
    )
}

const BasketComponent = ({basket,onCheckout}) => {
    const totalPrice = _.sum(basket.map(({price}) => price));
    const totalKM = _.sum(basket.map(({distance}) => distance));
    const totalMinRange = _.sum(basket.map(({minRange}) => minRange));
    const totalMaxRange = _.sum(basket.map(({maxRange}) => maxRange));
    return ((basket.length ?
        <StatusBar
            totalPrice={totalPrice}
            totalKM={totalKM}
            onCheckout={onCheckout}
            totalMinRange={totalMinRange}
            totalMaxRange={totalMaxRange}
        /> : null)
    )
};


const BasketContainer = connect(
    (state, ownProps) => ({
        basket: state.basket
    }),
    (dispatch, ownProps) => ({
        // onCheckout: (value) => dispatch(a.searchProducts(value))
    })
)(BasketComponent)

export default BasketContainer
