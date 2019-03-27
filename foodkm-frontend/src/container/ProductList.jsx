import React from 'react'
import _ from 'lodash';
import * as a from '../actions';
import { connect } from 'react-redux';


const ProductListItem = ({product_name,price,distance,idx,onClick}) => (
    <div className="product-list-item" onClick={onClick}>
      <div className="product-list-item-name">{product_name}</div>
      <div className="product-list-item-price">{price}</div>
      <div className="product-list-item-km">{distance}</div>
      <button className="add-to-cart-button">+</button>
    </div>
)

const ProductList = ({list=dummy, onClick}) => (
    _.map(list, (listItem, idx) => (
        <ProductListItem {...listItem} key={'product_'+idx} onClick={() => onClick(listItem)}/>
    ))
)


const ProductListContainer = connect(
    (state, ownProps) => ({
        list: state.products
    }),
    (dispatch, ownProps) => ({
        onClick: (product) => dispatch(a.addBasket(product))
    })
)(ProductList)

export default ProductListContainer
