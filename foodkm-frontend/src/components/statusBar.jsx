import React from 'react'

const StatusBar = ({totalPrice=70,totalKM=1300,onClick}) => (
    <div id="status-bar">
      <div className="status-bar-title">Totales</div>
      <div className="status-bar-price">{totalPrice}€</div>
      <div className="status-bar-km">{totalKM}km</div>
      <button id="add-to-cart-button" onClick={onClick}>Ver carrito</button>
    </div>
)

export default StatusBar