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
    return (

    <div id="cart-view-overlay" className={"gray-overlay " + (cardViewOverlayOpen ? 'cart-view-is-active' : null)}>
      <button className="close-button" onClick={closeOverlay} >×</button>
      <div className="padded-container" style={{width: "90%"}}>
        <h3>Productos seleccionados</h3>
        {_.map(basket, (listItem, idx) => (
            <CardListItem
                {...listItem} key={'product_'+idx}
                onClick={() => onClick(idx)}
            />
        ))}

              </div>
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
