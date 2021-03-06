from pydantic import BaseModel
from typing import List


class Category(BaseModel):
    id: int
    name: str


class Product(BaseModel):
    id: int
    name: str
    base_price: float
    sale_price: float
    currency: str
    description: str
    category: Category = None




class ProductList(BaseModel):
    products: List[Product]
