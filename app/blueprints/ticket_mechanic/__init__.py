from flask import Blueprint

ticket_mechanic_bp = Blueprint('ticket_mechanic', __name__)
from . import routes
pass