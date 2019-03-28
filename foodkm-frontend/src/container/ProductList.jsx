import React from 'react'
import _ from 'lodash';
import * as a from '../actions';
import { connect } from 'react-redux';


const ProductListItem = ({category_child1, category_child2, additives, allergens, address,
    product_brand,product_name,price,distance,idx,onClick}) => (
    <div className="product-list-item">
      <div className="product-list-item-info">
          <div className="product-list-item-category">{category_child1} | {category_child2}</div>
          <div className="product-list-item-name">{product_name}</div>
          <div className="product-list-item-brand">Marca {product_brand}, {address}</div>
      </div>
      <div className="product-list-item-data">
          <strong>Precio</strong>
          <div className="product-list-item-datum">{(price ? price.toFixed(2) + "€" : null)}</div>
          <strong>Distancia</strong>
          <div className="product-list-item-datum">{(distance ? Math.round(distance) + "km" : null)}</div>
      </div>
      <button className="add-to-cart-button" onClick={onClick}>+</button>
    </div>
)

const ProductList = ({list=dummy, onClick}) => {
    const minRange = _.min(list.map(({distance}) => distance));
    const maxRange = _.max(list.map(({distance}) => distance));
    return (
        _.map(list, (listItem, idx) => (
            <ProductListItem
                {...listItem} key={'product_'+idx}
                onClick={() => onClick({...listItem, minRange, maxRange})}
            />
        ))
    )
}


const ProductListContainer = connect(
    (state, ownProps) => ({
        list: state.products
    }),
    (dispatch, ownProps) => ({
        onClick: (product) => dispatch(a.addBasket(product))
    })
)(ProductList)

export default ProductListContainer
