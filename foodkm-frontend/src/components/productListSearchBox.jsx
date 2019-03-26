import React from 'react'

const ProductListSearchBox = ({onChange}) => (
  <div id="product-list-search-box">
    <input type="text"
        id='product-list-search-box'
        placeholder='Buscar producto...'
        onChange={onChange}
    />
    <div id="autocomplete-box">
    </div>
  </div>

)

export default ProductListSearchBox