import React from 'react'
import { connect } from 'react-redux';
import * as a from '../actions';

const StatusBar = ({onCheckout,changeLocation, basket}) => {
    // const totalKMPro = (totalKM ? (totalKM - totalMinRange) / (totalMaxRange - totalMinRange) * 100 : 0);
    // const statusbar = (  totalKM ?   <div className="status-bar-range">{totalMinRange.toFixed(0)}km<progress max="100" value={totalKMPro.toFixed(0)}> {totalKMPro.toFixed(0)}% </progress>{totalMaxRange.toFixed(0)}km</div>:null)
    return (
        <div id="status-bar">
            <button className="button" id={"add-to-cart-button"} onClick={(basket.length > 0 ? onCheckout : null)}>Analizar</button>
            <button className="button" id="back-to-location" onClick={changeLocation}>Cambiar locacion</button>
        </div>
    )
}

// const BasketComponent = ({onCheckout, changeLocation}) => {
//     // const totalPrice = _.sum(basket.map(({price}) => price));
//     // const totalKM = _.sum(basket.map(({distance}) => distance));
//     // const totalMinRange = _.sum(basket.map(({minRange}) => minRange));
//     // const totalMaxRange = _.sum(basket.map(({maxRange}) => maxRange));
//     return (
//     <StatusBar
//         totalPrice={totalPrice}
//         totalKM={totalKM}
//         onCheckout={onCheckout}
//         totalMinRange={totalMinRange}
//         totalMaxRange={totalMaxRange}
//     />)
// };


const BasketContainer = connect(
    (state, ownProps) => ({
        basket: state.basket
    }),
    (dispatch, ownProps) => ({
        onCheckout: (value) => dispatch(a.updateUi({cardViewOverlayOpen: true})),
        changeLocation: (value) => dispatch(a.updateUi({addressSearchOverlayOpen: true})),
    })
)(StatusBar)

export default BasketContainer
