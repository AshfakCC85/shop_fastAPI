from fastapi import FastAPI
from routers import products

app = FastAPI()

app.include_router(products.router, prefix='/products', tags=['product'])

@app.get('/')
def index_page():
    return {
        'Message': 'hello'
    }