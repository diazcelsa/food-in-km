import L from 'leaflet'
import './stamen-map.js'
import {extent} from 'd3-array'

export default class map {
  constructor(opts) {
    Object.assign(this, opts);

    this.theMap = L.map('map', {
      center: this.center,
      zoom: 13
    });

    let layer = new L.StamenTileLayer("toner-lite");
    this.theMap.addLayer(layer);



    this.features = []
  }

  removeAllFeatures() {
    this.features.forEach(layer => {
      this.theMap.removeLayer(layer)
    })
  }

  addLocations(locations) {
    this.removeAllFeatures()

    locations.forEach(loc => {
      let line = L.polyline([this.center,loc.loc],{
        'color': '#A169FF',
        'weight' : 2
      }).addTo(this.theMap);

      let circle = L.circleMarker(loc.loc, {
        'radius' : 3,
        'color' : '#fff',
        'weight' : 1,
        'fillOpacity': 1,
        'fillColor': '#A169FF'
      }).addTo(this.theMap);
      this.features.push(line)
    })

    let circle = L.circleMarker(this.center, {
        'radius' : 5,
        'stroke': true,
        'fillOpacity': 1,
        'weight' : 1,
        'fillColor': '#4a4a4a',
        'color' : '#fff'
    }).addTo(this.theMap);
    this.features.push(circle)

    let latExtents = extent(locations, d => {
      return d.loc[0]
    })

    let lonExtents = extent(locations, d => {
      return d.loc[1]
    })

    this.theMap.fitBounds([
      [latExtents[0],lonExtents[0]],
      [latExtents[1],lonExtents[1]]
    ])
    console.log(latExtents,lonExtents)

  }
}
