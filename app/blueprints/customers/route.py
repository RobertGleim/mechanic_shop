from . import customers_bp
from .schema import customer_schema, customers_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Customers, db


@customers_bp.route('/', methods=['POST'])

def create_customer():
    try:
        data = customer_schema.load(request.json)
    except ValidationError as e: 
        return jsonify(e.messages),400

    new_customer = Customers(**data)
    db.session.add(new_customer)
    db.session.commit()
    print(f"New Customer was created, Welcome: {new_customer.first_name} {new_customer.last_name}")
    return customer_schema.jsonify(new_customer), 201

@customers_bp.route('', methods=['GET'])
def read_customers():
    customers = db.session.query(Customers).all()
    return customers_schema.jsonify(customers), 200

@customers_bp.route('<int:customer_id>', methods=['GET'])
def read_customer(customer_id):
    customer = db.session.get(Customers, customer_id) 
    print(f"Customer found: {customer.first_name} {customer.last_name}")
    return customer_schema.jsonify(customer), 200


@customers_bp.route('/<int:customers_id>', methods=['DELETE'])  
def delete_customer(customers_id):
    customer = db.session.get(Customers, customers_id)
    db.session.delete(customer)
    db.session.commit()
    print(f"Customer deleted: {customer.first_name} {customer.last_name}")
    return jsonify({"message": f"Sorry to see you go! {customers_id}"}), 200

@customers_bp.route('<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = db.session.get(Customers, customer_id)
    
    if not customer:
        return jsonify({"message": "Customer not found"}), 404
    try:
        Customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"Message": e.messages}), 400
    for key, value in Customer_data.items():
        setattr(customer, key, value)
    db.session.commit()
    print(f"Customer updated: {customer.first_name} {customer.last_name}")
    return customer_schema.jsonify(customer), 200
