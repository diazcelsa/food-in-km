import React from 'react'

const TabMenu = ({list,inCart=0,resultCount=0,onClick}) => (
    <div id="tab-menu">
      <button className="is-active">Resultados ({resultCount})</button>
      <button>Canasta ({inCart})</button>
    </div>
)

export default TabMenu