import os

# file names
final_product_info_clean = "data/product_complete/product_info_complete_clean.csv"

# google API config
GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'
GOOGLE_MAPS_API_KEY = os.environ['GOOGLE_API_KEYS'].split('[')[1].split(']')[0].split(',')[0]

# Column selection per group
PRODUCT_INFO = ['product_id', 'Código EAN Producto:', 'Nombre Alimento:', 'Cantidad Neta:']
COL_INGREDIENTS = ['Alérgenos', 'Lista Ingredientes:', 'Instrucciones Uso:', 'Menciones Obligatorias:']
PROVIDER_INFO = ['Nombre Proveedor:', 'Dirección Proveedor:', 'Pais Origen:', 'Marca:']
CATEGORIES = ['root_cat', 'child_1_cat', 'child_2_cat', 'child_3_cat', 'child_4_cat', 'child_5_cat']
PRICES = ['price','price_norm'] 

# Columns to drop
COL_DROPS = ['Cantidad neta del alimento (Formato texto libre):','Declaración Nutricional:','Variedad:', 
             'Descripción del rango de raciones:', 'Descripción producto', 'Descripción:','Modo de empleo:',
             'Peso Neto Escurrido:', 'Propiedades Saludables:']

# Dictionary product info columns
COL_RENAME_DICT = {
    'Código EAN Producto:': 'provider_ean_id', 
    'Nombre Alimento:': 'product_name', 
    'Cantidad Neta:': 'product_amount_netto',
    'Nombre Proveedor:': 'provider_name', 
    'Dirección Proveedor:': 'provider_address', 
    'Pais Origen:': 'provider_country', 
    'Marca:': 'product_brand',
    'root_cat':'category_root', 
    'child_1_cat': 'category_child1', 
    'child_2_cat': 'category_child2', 
    'child_3_cat': 'category_child3', 
    'child_4_cat': 'category_child4', 
    'child_5_cat': 'category_child5',
}