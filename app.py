from flask import Flask, request,jsonify
from flask_jwt_extended import jwt_manager,create_access_token
import psycopg2
import psycopg2.extras


app = Flask(__name__)
jwt_1 = jwt_manager (app)

# config 
DB_host = "localhost"
DB_name="lass_API"
DB_user= "Lansana"
DB_pass= "Lass5920@"


conn = psycopg2.connect(host=DB_host, dbname=DB_name, user=DB_user, password=DB_pass)

@app.route("/connection", methods= ['POST'])
def login ():
       data = request.get_json()
       recup_user= data.get("username")
       recup_pass= data.get("lucien1234")

       parcours = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
       parcours.execute("SELECT * FROM utilisateur where nom = %s pass_word=%s")(recup_user, recup_pass)

       var_recuper=parcours.fetchone()
       if var_recuper and recup_user and recup_pass :
        recup_token = create_access_token(identity={'id':parcours["id"], 'role':parcours["role"]})
        return jsonify({"recup_token": recup_token})
       else :
        return jsonify ({"message" : "invalide"})
    


