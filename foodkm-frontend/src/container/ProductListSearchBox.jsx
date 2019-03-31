import React from 'react'
import _ from 'lodash';
import * as a from '../actions';
import { connect } from 'react-redux';
import { useState } from 'react';

const ProductListSearchBox = ({onChange, suggest=[]}) => (
        <div id="product-list-search-box" className="search-box">
            <input type="text" list="suggestions"
                placeholder='Buscar producto...'
                defaultValue='garbanzo'
                onInput={evt => onChange(evt.target.value)}
            />
            <datalist id="suggestions">
                {suggest.map(({text}, idx)=> <option value={text} key={'suggest-' + idx} />)}
            </datalist>
            <div className="search-box-icon"></div>
            <div id="autocomplete-box">
            </div>
        </div>
)

const ProductListSearchBoxContainer = connect(
    (state, ownProps) => ({
        list: state.productList,
        suggest: state.suggest
    }),
    (dispatch, ownProps) => ({
        onChange: (value) => dispatch(a.searchProducts(value))
    })
)(ProductListSearchBox)

export default ProductListSearchBoxContainer
