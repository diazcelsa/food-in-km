import React from 'react'
import _ from 'lodash';
import * as a from '../actions';
import { connect } from 'react-redux';


const ProductListItem = ({category_child1, category_child2, additives, allergens, address,
    product_brand,product_name,price,distance,idx,onClick, buttonStyle, product_description}) => (
    <div className="product-list-item">
      <div className="product-list-item-info">
          <div className="product-list-item-category">{category_child1} | {category_child2}</div>
          <div className="product-list-item-name">{(product_name ? product_name : product_description)}</div>
          <div className="product-list-item-brand">Marca {product_brand}, {address}</div>
      </div>
      <div className="product-list-item-data">
          <strong>Precio</strong>
          <div className="product-list-item-datum">{(price ? price.toFixed(2) + "€" : null)}</div>
          <strong>Distancia</strong>
          <div className="product-list-item-datum">{(distance ? Math.round(distance) + "km" : null)}</div>
      </div>
      <button className="add-to-cart-button" onClick={onClick}>{buttonStyle}</button>
    </div>
)

const ProductList = ({basket, products, onRmBasket, onAddBasket, searchActive}) => {
    const minRange = _.min(products.map(({distance}) => distance));
    const maxRange = _.max(products.map(({distance}) => distance));
    const searchDistances = _.map(products, ({distance}) => distance);
    const buttonStyle = (searchActive ? '+' : '-');
    const list = (searchActive ? products : basket);
    return (
        _.map(list, (listItem, idx) => (
            <ProductListItem
                {...listItem} key={'product_'+idx}
                buttonStyle={buttonStyle}
                onClick={() =>
                    (searchActive ? onAddBasket({...listItem, minRange, maxRange, searchDistances}): onRmBasket(idx))}
            />
        ))
    )
}


const ProductListContainer = connect(
    (state, ownProps) => ({
        products: state.products,
        basket: state.basket,
        searchActive: state.ui.searchActive
    }),
    (dispatch, ownProps) => ({
        onAddBasket: (product) => dispatch(a.addBasket(product)),
        onRmBasket: (idx) => dispatch(a.removeBasket(idx))
    })
)(ProductList)

export default ProductListContainer
