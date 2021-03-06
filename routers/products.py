from fastapi import APIRouter
from schema import products

router = APIRouter()
product_list = {
    'products': [{
    'id': 1,
    'name': 'fruit juice',
    'base_price': 122.3,
    'sale_price': 111,
    'description': 'we are awesome',
    'currency': '$',
    'category':{
        'id': 1,
        'name': 'juice'
    }
}]}

@router.post('/')
def create_product():
    pass


@router.get('/', response_model=products.ProductList)
def list_products():
    return product_list


@router.get('/{product_id}', response_model=products.Product)
def get_product(product_id: int):
    return product_list['products'][0]