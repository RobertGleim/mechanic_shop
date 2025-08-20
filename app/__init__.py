from flask import Flask 
from .models import db
from .extenstions import ma, limiter, cache 
from .blueprints.customers import customers_bp
from .blueprints.mechanics import mechanics_bp
from .blueprints.service_tickets import service_tickets_bp
from .blueprints.ticket_mechanics import ticket_mechanics_bp





def create_app(config_name):
    
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')
    
    
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)
    
    
    app.register_blueprint(customers_bp, url_prefix='/customers')
    app.register_blueprint(mechanics_bp, url_prefix='/mechanics')
    app.register_blueprint(service_tickets_bp, url_prefix='/service_tickets')
    app.register_blueprint(ticket_mechanics_bp, url_prefix='/ticket_mechanics')
   
    
    
    return app


# =================================================================================================
    # python -m venv venv
    # venv\Scripts\activate
    # pip install flask-marshmallow
    # pip install marshmallow-sqlalchemy
    # pip install flask-sqlalchemy
    # pip install -r requirements.txt
    # pip freeze > requirements.txt
    # app.run(debug=True)  
    # pip install Flask-Limiter
    # pip install Flask-Caching
# =================================================================================================