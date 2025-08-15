from . import mechanics_bp
from .schema import mechanic_schema, mechanics_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Mechanics, db



@mechanics_bp.route('', methods=['POST'])

def create_customer():
    try:
        data = mechanics_schema.load(request.json)
    except ValidationError as e: 
        return jsonify(e.messages),400

    new_mechanic = Mechanics(**data)
    db.session.add(new_mechanic)
    db.session.commit()
    print(f"New mechanic was created, Hello: {new_mechanic.first_name} {new_mechanic.last_name}")
    return mechanic_schema.jsonify(new_mechanic), 201

@mechanics_bp.route('', methods=['GET'])
def read_mechanics():
    mechanics = db.session.query(Mechanics).all()
    return mechanics_schema.jsonify(mechanics), 200

@mechanics_bp.route('<int:mechanic_id>', methods=['GET'])
def read_mechainc(mechanic_id):
    mechanic = db.session.get(Mechanics, mechanic_id) 
    print(f"Mechanic found: {mechanic.first_name} {mechanic.last_name}")
    return mechanic_schema.jsonify(mechanic), 200


@mechanics_bp.route('/<int:mechanics_id>', methods=['DELETE'])  
def delete_mechanic(mechanics_id):
    mechanic = db.session.get(Mechanics, mechanics_id)
    db.session.delete(mechanic)
    db.session.commit()
    print(f"Mechanic deleted: {mechanic.first_name} {mechanic.last_name}")
    return jsonify({"message": f"Sorry to see you go! {mechanics_id}"}), 200

@mechanics_bp.route('<int:mechanic_id>', methods=['PUT'])
def update_mechanic(mechanic_id):
    mechanic = db.session.get(Mechanics, mechanic_id)
    
    if not mechanic:
        return jsonify({"message": "mechainc not found"}), 404
    try:
        Mechainc_data = mechanic_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"Message": e.messages}), 400
    for key, value in Mechainc_data.items():
        setattr(mechanic, key, value)
    db.session.commit()
    print(f"Mechanic updated: {mechanic.first_name} {mechanic.last_name}")
    return mechanic_schema.jsonify(mechanic), 200
