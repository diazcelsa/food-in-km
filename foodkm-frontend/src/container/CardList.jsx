import React from 'react'
import _ from 'lodash';
import * as a from '../actions';
import { connect } from 'react-redux';


const CardListItem = ({product_brand,product_name,price,distance,idx,onClick}) => (
        <div className="product-list-item">
          <div className="product-list-item-name">{product_brand} {product_name}</div>
          <div className="product-list-item-price">{(price ? price.toFixed(2) + "€" : null)}</div>
          <div className="product-list-item-km">{(distance ? Math.round(distance) + "km" : null)}</div>
          <button className="add-to-cart-button" onClick={onClick}>-</button>
        </div>
)

const ProductList = ({basket=dummy, onClick, closeOverlay, cardViewOverlayOpen}) => {
    const totalPrice = (basket.length > 0 ? _.sum(basket.map(({price}) => price)):0);
    const totalKM = (basket.length > 0 ? _.sum(basket.map(({distance}) => distance)):0);
    const numBasket = basket.length;
    const meanKM = (basket.length > 0 ? _.mean(basket.map(({distance}) => distance)):0);
    // const totalMinRange = _.sum(basket.map(({minRange}) => minRange));
    // const totalMaxRange = _.sum(basket.map(({maxRange}) => maxRange));


    return (

    <div id="cart-view-overlay" className={(cardViewOverlayOpen ? 'cart-view-is-active' : null)}>

        <div className="barns">
        <h3>Resumen de tu compra</h3>

          <div className="barn-unit">
            <em>Cantidad de productos</em>
            <strong>{numBasket}</strong>
          </div>

          <div className="barn-unit">
            <em>Gasto total</em>
            <strong>{totalPrice.toFixed(2)}<span>€</span></strong>
          </div>

          <div className="barn-unit">
            <em>Distancia total</em>
            <strong>{totalKM.toFixed(0)}<span>km</span></strong>
          </div>

          <div className="barn-unit">
            <em>Distancia promedia</em>
            <strong>{meanKM.toFixed(0)}<span>km</span></strong>
          </div>


        </div>
        {_.map(basket, (listItem, idx) => (
            <CardListItem
                {...listItem} key={'product_'+idx}
                onClick={() => onClick(idx)}
            />
        ))}

            </div>
    )
}

const ProductListContainer = connect(
    (state, ownProps) => ({
        basket: state.basket,
        cardViewOverlayOpen: state.ui.cardViewOverlayOpen
    }),
    (dispatch, ownProps) => ({
        onClick: (idx) => dispatch(a.removeBasket(idx)),
        closeOverlay: () => dispatch(a.updateUi({cardViewOverlayOpen: false}))
    })
)(ProductList)

export default ProductListContainer
