import React from 'react'
import _ from 'lodash';
import * as a from '../actions';
import { connect } from 'react-redux';

const ZIPSearchBox = ({onChange, address, geoLocate, addressSearchOverlayOpen, onLocation}) => {
    const getLocation = () => {
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(onLocation);
        }
      }

    return (

        <div id="zip-search-overlay" className={"gray-overlay " + (addressSearchOverlayOpen ? 'zip-search-is-active' : null)}>
            <div className="transform-center" style={{width: "50%"}}>
            <h3>Entre su dirección</h3>
            <div id="zip-search-box" className="search-box">
                <input type="text" list="zip"
                    placeholder='Buscar...'
                    onInput={evt => onChange(evt.target.value)}
                />
                {/* <datalist id="suggestions">
                    {suggest.map(({text}, idx)=> <option value={text} key={'suggest-' + idx} />)}
                </datalist> */}
                {/* <div className="search-box-icon"></div>
                <button className="button" id="geolocate-button" onClick={getLocation}>⚑</button>
                <div id="autocomplete-box">
                    {address}
                </div> */}
            </div>
            </div>
        </div>
    )
}


const ZIPSearchBoxContainer = connect(
    (state, ownProps) => ({
        address: state.location.address,
        addressSearchOverlayOpen: state.ui.addressSearchOverlayOpen
    }),
    (dispatch, ownProps) => ({
        onChange: (value) => dispatch(a.searchLocation(value)),
        onLocation: ({coords}) => dispatch(a.locationUpdate({lat:coords.latitude, lon:coords.longitude}))
    })
)(ZIPSearchBox)

export default ZIPSearchBoxContainer
