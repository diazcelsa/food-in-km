import React from 'react'

let dummy = [
  {
    'name' : 'Arroz',
    'price' : '1€',
    'distance': '33.4km'
  },
  {
    'name' : 'Cerveza',
    'price' : '2€',
    'distance': '63.4km'
  },
  {
    'name' : 'Aceitunas',
    'price' : '7.50€',
    'distance': '23.4km'
  },
  {
    'name' : 'Agua',
    'price' : '11€',
    'distance': '1,400km'
  },
  {
    'name' : 'Arroz',
    'price' : '1€',
    'distance': '33.4km'
  },
  {
    'name' : 'Vino',
    'price' : '12€',
    'distance': '83.4km'
  },
]


const ProductListItem = ({name,price,distance,idx,onClick}) => (
    <div className="product-list-item">
      <button className="add-to-cart-button" onClick={onClick}></button>
      <div className="product-list-item-name">{name}</div>
      <div className="product-list-item-price">{price}</div>
      <div className="product-list-item-km">{distance}</div>
    </div>
)

const ProductList = ({list=dummy, onClick}) => (
    _.map(list, (listItem, idx) => (
        <ProductListItem {...listItem} key={'product_'+idx} onClick={onClick}/>
    ))
)

export default ProductList