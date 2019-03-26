import React from 'react'

let dummy = [
  {
    'name' : 'Arroz',
    'price' : '1€',
    'distance': '33.4km',
    'loc' : [41.582578,0.603605]
  },
  {
    'name' : 'Chocolate',
    'price' : '130€',
    'distance': '33.4km',
    'loc' : [33.601301, 5.290211]
  },
  {
    'name' : 'Vino',
    'price' : '12€',
    'distance': '83.4km',
    'loc' : [36.803759,-2.541634]
  },
]


const ProductListItem = ({name,price,distance,idx,onClick}) => (
    <div className="product-list-item">
      <div className="product-list-item-name">{name}</div>
      <div className="product-list-item-price">{price}</div>
      <div className="product-list-item-km">{distance}</div>
      <button className="add-to-cart-button" onClick={onClick}>+</button>
    </div>
)

const ProductList = ({list=dummy, onClick}) => (
    _.map(list, (listItem, idx) => (
        <ProductListItem {...listItem} key={'product_'+idx} onClick={onClick}/>
    ))
)

export default ProductList