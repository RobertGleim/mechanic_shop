from app import create_app
from app.models import db

# customers: name, email. phone, address, id
# service tickets, id, cutomers, mechanics, service disc, price, vin
# mechanics: username, password, email, salary, address, id


    
    
#====================================== crud operations =========================================
app = create_app('DevelopmentConfig')

    

with app.app_context():
    # db.drop_all()  
    db.create_all()   
    
     
        
app.run(debug=True)        

