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
        this.theMap = new map({
            'center' : [this.props.location.lat,this.props.location.lon],
            'mapId': this.props.mapId
        });

        // const anyActive = !_.some(this.props.list, ({active}) => active);
        // console.log(anyActive);
        const locations = this.props.list.map(
            ({location, product_name, distance, active}) => (
                {product: {product_name, distance}, weight: (active ? 4: 2), color: (active ? '#4A4A4A': '#FF530D'), loc: [location.lat, location.lon]}))
        const locations_sorted = _.orderBy(locations, 'weight', 'asc');
        if (locations_sorted.length > 0) {
            this.theMap.addLocations(locations_sorted);
        }
    }

    componentDidUpdate(){
        this.theMap.updateCenter([this.props.location.lat,this.props.location.lon]);
        // this.theMap = new map({
        //     'center' : [this.props.location.lat,this.props.location.lon]
        // });

        // const anyActive = _.some(this.props.list, ({active}) => active);
        const locations = this.props.list.map(
            ({location, product_name, distance, active}) => (
                {product: {product_name, distance}, weight: (active ? 4: 2), color: (active ? '#4A4A4A': '#FF530D'), loc: [location.lat, location.lon]}))
        const locations_sorted = _.orderBy(locations, 'weight', 'asc');
        console.log(locations_sorted);
        if (locations_sorted.length > 0) {
            this.theMap.addLocations(locations_sorted);
        } else {
            this.theMap.resetView();
        }
    }

    render() {
        return (
        <div id={this.props.mapId}>
        </div>)
    }
}

const MapContainer = connect(
    (state, ownProps) => ({
        list: state.products,
        location: state.location,
        mapId: 'mapSearch'
    }),
    (dispatch, ownProps) => ({
    })
)(MapComponent)



export {MapComponent};

export default MapContainer
