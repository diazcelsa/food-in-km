import React from 'react'
import { connect } from 'react-redux';
import * as a from '../actions';

const StatusBar = (
        {totalPrice=70,totalKM=1300,onCheckout,totalMinRange,totalMaxRange}) => {
    const totalKMPro = (totalKM ? (totalKM - totalMinRange) / (totalMaxRange - totalMinRange) * 100 : 0);
    const statusbar = (  totalKM ?   <div className="status-bar-range">{totalMinRange.toFixed(0)}km<progress max="100" value={totalKMPro.toFixed(0)}> {totalKMPro.toFixed(0)}% </progress>{totalMaxRange.toFixed(0)}km</div>:null)
    return (
        <div id="status-bar">
        <div className="status-bar-title">Totales</div>
        <div className="status-bar-price">{(totalPrice ? totalPrice.toFixed(0) : 0)}€</div>
        <div className="status-bar-km">{(totalKM ? totalKM.toFixed(0) : 0)}km</div>
        {statusbar}
        <button className="button" id="add-to-cart-button" onClick={onCheckout}>Ver carrito</button>
        </div>
    )
}

const BasketComponent = ({basket,onCheckout}) => {
    const totalPrice = _.sum(basket.map(({price}) => price));
    const totalKM = _.sum(basket.map(({distance}) => distance));
    const totalMinRange = _.sum(basket.map(({minRange}) => minRange));
    const totalMaxRange = _.sum(basket.map(({maxRange}) => maxRange));
    return (
    <StatusBar
        totalPrice={totalPrice}
        totalKM={totalKM}
        onCheckout={onCheckout}
        totalMinRange={totalMinRange}
        totalMaxRange={totalMaxRange}
    />)
};


const BasketContainer = connect(
    (state, ownProps) => ({
        basket: state.basket
    }),
    (dispatch, ownProps) => ({
        onCheckout: (value) => dispatch(a.updateUi({cardViewOverlayOpen: true}))
    })
)(BasketComponent)

export default BasketContainer
