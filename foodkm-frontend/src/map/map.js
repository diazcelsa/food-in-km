import L from 'leaflet'
import './stamen-map.js'
import {extent} from 'd3-array'

export default class map {
  constructor(opts) {
    Object.assign(this, opts);

    this.theMap = L.map('map', {
      center: this.center,
      zoom: 7,
      dragging: false,
      zoomControl: false
    });

    let layer = new L.StamenTileLayer("toner-lite");
    this.theMap.addLayer(layer);

    this.features = []
  }

  updateCenter(center) {
      this.center = center;
  }

  resetView() {
    this.theMap.setZoom(7);
    this.theMap.setView(this.center);
    this.removeAllFeatures();
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
        'color': '#FF530D',
        'weight' : 2
      }).addTo(this.theMap);

      let circle = L.circleMarker(loc.loc, {
        'radius' : 3,
        'color' : '#fff',
        'weight' : 1,
        'fillOpacity': 1,
        'fillColor': '#FF530D'
      }).addTo(this.theMap);
      line.bindPopup('<b>' + loc.product.distance.toFixed(2) + 'km</b>');
      line.on('mouseover', function (e) {
          this.openPopup();
      });
      line.on('mouseout', function (e) {
          this.closePopup();
      });

      circle.bindPopup(loc.product.product_name);
      circle.on('mouseover', function (e) {
          this.openPopup();
      });
      circle.on('mouseout', function (e) {
          this.closePopup();
      });

      this.features.push(line);
      this.features.push(circle);
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

    lonExtents = [Math.min(lonExtents[0], this.center[1]), Math.max(lonExtents[1], this.center[1])]
    latExtents = [Math.min(latExtents[0], this.center[0]), Math.max(latExtents[1], this.center[0])]

    this.theMap.fitBounds([
      [latExtents[0],lonExtents[0]],
      [latExtents[1],lonExtents[1]]
    ])
    console.log(latExtents,lonExtents)

  }
}
