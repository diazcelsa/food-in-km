import React from 'react'
import _ from 'lodash';
import * as a from '../actions';
import { connect } from 'react-redux';
import stripPlot from './../map/strip-plot'
import {MapComponent} from '../map/MapComponent'


const CardListItem = ({product_brand,product_name,price,distance,idx,onClick,category_child1,category_child2,address,searchDistances}) => (
// searchDistances: array of distances of comparable products
    <div className="product-list-item">
        <div className="result-info">
          <div className="product-list-item-category">{category_child1} | {category_child2}</div>
          <div className="product-list-item-name">{(product_name ? product_name : product_description)}</div>
          <div className="product-list-item-brand">Marca {product_brand}, {address}</div>
          <div className="result-float">
            <strong>Precio</strong>
            <div className="product-list-item-datum">{(price ? price.toFixed(2) + "€" : null)}</div>
          </div>
          <div className="result-float">
            <strong>Distancia</strong>
            <div className="product-list-item-datum">{(distance ? Math.round(distance) + "km" : null)}</div>
          </div>
        </div>
        <div className="result-chart" id={"chart_"+idx}>
            <svg></svg>
            
        </div>
    </div>
)

const ProductList = ({basket=dummy, onClick, location, cardViewOverlayOpen}) => {
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

<<<<<<< HEAD
        <div className="map" id="analysis-map"></div>

=======
          <div className='map'>
            <MapComponent location={location} list={basket} mapId="analysisMap" />
        </div>
>>>>>>> 38d5a2ac0ffb133b6f3a23f3b5a8d6fa9d8628eb


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
        location: state.location,
        cardViewOverlayOpen: state.ui.cardViewOverlayOpen
    }),
    (dispatch, ownProps) => ({
        onClick: (idx) => dispatch(a.removeBasket(idx)),
        closeOverlay: () => dispatch(a.updateUi({cardViewOverlayOpen: false}))
    })
)(ProductList)

export default ProductListContainer
