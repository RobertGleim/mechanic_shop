from app.extenstions import ma
from app.models import Ticket_Mechanics


class Ticket_MechanicSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ticket_Mechanics
        include_fk = True
        
ticket_mechanic_schema = Ticket_MechanicSchema()
ticket_mechanics_schema = Ticket_MechanicSchema(many=True)
pass