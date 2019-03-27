import React from 'react'
import _ from 'lodash';
import * as a from '../actions';
import { connect } from 'react-redux';
import { useState } from 'react';

const ProductListSearchBox = ({onChange}) => (
        <div id="product-list-search-box">
            <input type="text"
                placeholder='Buscar producto...'
                onInput={evt => onChange(evt.target.value)}
            />
            <div className="search-box-icon"></div>
            <div id="autocomplete-box">
            </div>
        </div>
)

const ProductListSearchBoxContainer = connect(
    (state, ownProps) => ({
        list: state.productList
    }),
    (dispatch, ownProps) => ({
        onChange: (value) => dispatch(a.searchProducts(value))
    })
)(ProductListSearchBox)

export default ProductListSearchBoxContainer
