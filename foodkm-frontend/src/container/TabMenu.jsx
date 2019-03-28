import React from 'react';
import * as a from '../actions';
import { connect } from 'react-redux';

const TabMenu = ({inCart=0,resultCount=0,searchActive, onClickResults, onClickChart}) => (
    <div id="tab-menu">
      <button className={(searchActive ? "is-active" : '')} onClick={onClickResults}>Resultados ({resultCount})</button>
      <button className={(searchActive ? '' : "is-active")} onClick={onClickChart}>Canasta ({inCart})</button>
    </div>
)

const TabMenuContainer = connect(
    (state, ownProps) => ({
        resultCount: state.products.length,
        inCart: state.basket.length,
        searchActive: state.ui.searchActive
    }),
    (dispatch, ownProps) => ({
        onClickResults: () => dispatch(a.updateUi({searchActive: true})),
        onClickChart: () => dispatch(a.updateUi({searchActive: false}))
    })
)(TabMenu)

export default TabMenuContainer

