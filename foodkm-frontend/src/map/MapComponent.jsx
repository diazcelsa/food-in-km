import React from 'react'
import _ from 'lodash';
import * as a from '../actions';
import { connect } from 'react-redux';

import map from './map';

// const MapComponent = ({list,userCoords=[40.4,-3.68],onClick}) => (

// )


// const test = [
//     {
//       'name' : 'Arroz',
//       'price' : '1€',
//       'distance': '33.4km',
//       'loc' : [41.582578,0.603605]
//     },
//     {
//       'name' : 'Chocolate',
//       'price' : '130€',
//       'distance': '33.4km',
//       'loc' : [33.601301, 5.290211]
//     },
//     {
//       'name' : 'Vino',
//       'price' : '12€',
//       'distance': '83.4km',
//       'loc' : [36.803759,-2.541634]
//     },
//   ]



class MapComponent extends React.Component {
    constructor() {
        super();
        // this.theMap = null;
    }

    componentDidMount(){
        console.log("MOUNT")
        this.theMap = new map({
            'center' : [40.4,-3.68]
        });
    }

    componentDidUpdate(){
        const locations = this.props.products.map(
            ({location, product_name}) => ({name: product_name, loc: [location.lat, location.lon]}))
        // console.log(locations);
        if (locations.length > 0) {
            console.log(locations);
            this.theMap.addLocations(locations);
        }
    }

    render() {
        return (
        <div id="map">
        </div>)
    }
}

const MapContainer = connect(
    (state, ownProps) => ({
        products: state.products
    }),
    (dispatch, ownProps) => ({
    })
)(MapComponent)





export default MapContainer
