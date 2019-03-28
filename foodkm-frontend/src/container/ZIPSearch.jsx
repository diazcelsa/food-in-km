import React from 'react'
import _ from 'lodash';
import * as a from '../actions';
import { connect } from 'react-redux';

const ZIPSearchBox = ({onChange}) => (
        <div id="product-list-search-box">
            <input type="text" list="zip"
                placeholder='Buscar zip...'
                onInput={evt => onChange(evt.target.value)}
            />
            {/* <datalist id="suggestions">
                {suggest.map(({text}, idx)=> <option value={text} key={'suggest-' + idx} />)}
            </datalist> */}
            <div className="search-box-icon"></div>
            <div id="autocomplete-box">
            </div>
        </div>
)

const ZIPSearchBoxContainer = connect(
    (state, ownProps) => ({
    }),
    (dispatch, ownProps) => ({
        onChange: (value) => dispatch(a.searchLocation(value))
    })
)(ZIPSearchBox)

export default ZIPSearchBoxContainer
