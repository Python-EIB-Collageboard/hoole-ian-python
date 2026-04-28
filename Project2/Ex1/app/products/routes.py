from flask import Blueprint, request
from uuid import uuid8

product_bp = Blueprint('products', __name__, url_prefix='/products')

_products: list = []

@product_bp.get('/')
def get_products():
  return {'products': _products}, 200

@product_bp.post('/')
def create_product():
  try:
    payload = request.get_json()
    payload['id'] = str(uuid8())
    _products.append(payload)
    return {'created': payload}, 201
  except Exception as e:
    print(e)
    return {"error": "Item failed to update"}, 404
  

@product_bp.get('/<string:product_id>')
def get_product(product_id):
  for i in _products:
    if i["id"] == product_id:
      return {'product': i}, 200
  return { "error": "No item found" }, 404

@product_bp.put('/<string:product_id>')
def put_product(product_id):
  payload = request.get_json()
  payload['id'] = product_id
  for i in _products:
    if i["id"] == product_id:
      _products.remove(i)
      _products.append(payload)
      return {'product': payload}, 200
  return {"error": "Item update failed"}, 404

@product_bp.delete('/<string:product_id>')
def delete_product(product_id):
  try: 
    print("IH ", product_id)   
    for i in _products:
      if i["id"] == product_id:
        print("IH ", i)  
        _products.remove(i)
        return {}, 204
    return {"error": "Item delete failed"}, 404
  except Exception as e:
    print("IH", e)
    return {"error": "Item delete failed"}, 404