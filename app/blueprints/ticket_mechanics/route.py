from app.blueprints import customers
from . import ticket_mechanics_bp
from .schema import ticket_mechanic_schema, ticket_mechanics_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Ticket_Mechanics, db


@ticket_mechanics_bp.route('', methods=['POST'])
def create_ticket_mechanic():
    try:
        data = ticket_mechanic_schema.load(request.json)
    except ValidationError as e: 
        return jsonify(e.messages),400

    new_ticket_mechanic = Ticket_Mechanics(**data)
    db.session.add(new_ticket_mechanic)
    db.session.commit()
    print(f"New Ticket was created:  ")
    return ticket_mechanics_schema.jsonify(new_ticket_mechanic), 201

@ticket_mechanics_bp.route('', methods=['GET'])
def read_ticket_mechanics():
    ticket_mechanics = db.session.query(Ticket_Mechanics).all()
    return ticket_mechanics_schema.jsonify(ticket_mechanics), 200

@ticket_mechanics_bp.route('<int:ticket_mechanic_id>', methods=['GET'])
def read_ticket_mechanic(ticket_mechanic_id):
    ticket_mechanic = db.session.get(Ticket_Mechanics, ticket_mechanic_id) 
    print(f"ticket_mechanics found: {ticket_mechanic_id}")
    return ticket_mechanic_schema.jsonify(ticket_mechanic), 200


@ticket_mechanics_bp.route('/<int:ticket_mechanics_id>', methods=['DELETE'])  
def delete_ticket_mechanic(ticket_mechanics_id):
    ticket_mechanic = db.session.get(Ticket_Mechanics, ticket_mechanics_id)
    db.session.delete(ticket_mechanic)
    db.session.commit()
    print(f"ticket_mechanics deleted:{ticket_mechanics_id}")
    return jsonify({"message": f"ticket was deleted: {ticket_mechanics_id}"}), 200

@ticket_mechanics_bp.route('<int:ticket_mechanic_id>', methods=['PUT'])
def update_ticket_mechanic(ticket_mechanic_id):
    ticket_mechanic = db.session.get(Ticket_Mechanics, ticket_mechanic_id)
    
    if not ticket_mechanic:
        return jsonify({"message": "ticket_mechanic not found"}), 404
    try:
        ticket_mechanic_data = ticket_mechanic_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"Message": e.messages}), 400
    for key, value in ticket_mechanic_data.items():
        setattr(ticket_mechanic, key, value)
    db.session.commit()
    print(f"ticket_mechanic updated: {ticket_mechanic_id}")
    return ticket_mechanic_schema.jsonify(ticket_mechanic), 200
