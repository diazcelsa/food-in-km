import React from 'react'

const ProductListSearchBox = ({onChange}) => (
  <div id="product-list-search-box">
    <input type="text"
        placeholder='Buscar producto...'
        onChange={onChange}
    />
    <div className="search-box-icon"></div>
    <div id="autocomplete-box">
    </div>
  </div>

)

export default ProductListSearchBox