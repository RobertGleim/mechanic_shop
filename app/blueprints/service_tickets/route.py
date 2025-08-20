from . import service_tickets_bp
from .schema import service_ticket_schema, service_tickets_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Service_Ticket, db


@service_tickets_bp.route('', methods=['POST'])

def create_service_ticket():
    try:
        data = service_ticket_schema.load(request.json)
    except ValidationError as e: 
        return jsonify(e.messages),400

    new_service = Service_Ticket(**data)
    db.session.add(new_service)
    db.session.commit()
    print(f"New Service ticket was created : For Customer {new_service.customer_id}")
    return service_ticket_schema.jsonify(new_service), 201

@service_tickets_bp.route('', methods=['GET'])
def read_service_tickets():
    service_tickets = db.session.query(Service_Ticket).all()
    return service_tickets_schema.jsonify(service_tickets), 200

@service_tickets_bp.route('<int:service_tickets_id>', methods=['GET'])
def read_service_ticket(service_tickets_id):
    service_ticket = db.session.get(Service_Ticket, service_tickets_id) 
    print(f"Service Ticket found: {service_tickets_id}")
    return service_ticket_schema.jsonify(service_ticket), 200


@service_tickets_bp.route('/<int:service_tickets_id>', methods=['DELETE'])  
def delete_service_ticket(service_tickets_id):
    service_ticket = db.session.get(Service_Ticket, service_tickets_id)
    db.session.delete(service_ticket)
    db.session.commit()
    print(f"Service Ticket {service_tickets_id} was deleted ")
    return jsonify({"message": f"Service Ticket  {service_tickets_id} was deleted "}), 200

@service_tickets_bp.route('<int:service_ticket_id>', methods=['PUT'])
def update_service_ticket(service_ticket_id):
    service_ticket = db.session.get(Service_Ticket, service_ticket_id)
    
    if not service_ticket:
        return jsonify({"message": "Service Ticket not found"}), 404
    try:
        Service_Ticket_data = service_ticket_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"Message": e.messages}), 400
    for key, value in Service_Ticket_data.items():
        setattr(service_ticket, key, value)
    db.session.commit()
    print(f"Service Ticket updated: for customer {service_ticket.customer_id}")
    return service_ticket_schema.jsonify(service_ticket), 200