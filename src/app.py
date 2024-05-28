"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,Character,Planet,Starship,Vehicle,Specie,FavoriteCharacter,FavoritePlanet,FavoriteStarship,FavoriteVehicle,FavoriteSpecie
#from models import Person
import json

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    users = User.query.all()
    result = list(map(lambda x: x.serialize(),users))
    return jsonify(result),200

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return jsonify({"msg":"el usuario no existe" }), 404
    return jsonify(user.serialize()),200


## RUTAS DE LOS PERSONAJES

## Ruta para obtener todos los Personajes
@app.route('/character', methods=['GET'])
def get_all_characters():
    characters = Character.query.all()
    result = list(map(lambda x: x.serialize(),characters))
    return jsonify(result),200

## Ruta para obtener un Personaje por ID 
@app.route('/character/<int:character_id>', methods=['GET'])
def get_character_by_id(character_id):
    character = Character.query.get(character_id)
    if character is None:
        return jsonify({"msg":"el Personaje no existe" }), 404
    return jsonify(character.serialize()),200

## Ruta para crear un Personaje favorito 
@app.route('/favorite/character/<int:character_id>/user/<int:user_id>', methods=['POST'])
def create_favorite_character(character_id,user_id):
    newFavorite = FavoriteCharacter(
        user_id = user_id,
        character_id = character_id
    )
    db.session.add(newFavorite)
    db.session.commit()
    return jsonify({"msg":"El Personaje Favorito esta Guardado"}), 200

## Ruta para Eliminar un Personaje favorito 
@app.route('/favorite/character/<int:character_id>/user/<int:user_id>', methods=['DELETE'])
def delete_favorite_character(character_id,user_id):
    favorite = FavoriteCharacter.query.filter_by(character_id=character_id,user_id=user_id).first()
    if favorite is None:
        return jsonify({"msg":"el Personaje favorito no existe" }), 404
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"msg":"El Personaje Favorito esta Eliminado"}), 200



## RUTAS DE LOS PLANETAS

## Ruta para obtener todos los Planetas
@app.route('/planet', methods=['GET'])
def get_all_planets():
    planets = Planet.query.all()
    result = list(map(lambda x: x.serialize(),planets))
    return jsonify(result),200

## Ruta para obtener un Planeta por ID 
@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_planet_by_id(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify({"msg":"el Planeta no existe" }), 404
    return jsonify(planet.serialize()),200

## Ruta para crear un Planeta favorito 
@app.route('/favorite/planet/<int:planet_id>/user/<int:user_id>', methods=['POST'])
def create_favorite_planet(planet_id,user_id):
    newFavorite = FavoritePlanet(
        user_id = user_id,
        planet_id = planet_id
    )
    db.session.add(newFavorite)
    db.session.commit()
    return jsonify({"msg":"El Planeta Favorito esta Guardado"}), 200

## Ruta para Eliminar un Planeta favorito 
@app.route('/favorite/planet/<int:planet_id>/user/<int:user_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id,user_id):
    favorite = FavoritePlanet.query.filter_by(planet_id=planet_id,user_id=user_id).first()
    if favorite is None:
        return jsonify({"msg":"el Planeta favorito no existe" }), 404
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"msg":"El Planeta Favorito esta Eliminado"}), 200


## RUTAS DE LAS NAVES ESPACIALES

## Ruta para obtener todas las Naves Espaciales 
@app.route('/starship', methods=['GET'])
def get_all_starship():
    starships = Starship.query.all()
    result = list(map(lambda x: x.serialize(),starships))
    return jsonify(result),200

## Ruta para obtener una Nave Espacial por ID 
@app.route('/starship/<int:starship_id>', methods=['GET'])
def get_starship_by_id(starship_id):
    starship = Starship.query.get(starship_id)
    if starship is None:
        return jsonify({"msg":"La Nave espacial no existe" }), 404
    return jsonify(starship.serialize()),200

## Ruta para crear una Nave Espacial favorito 
@app.route('/favorite/starship/<int:starship_id>/user/<int:user_id>', methods=['POST'])
def create_favorite_starship(starship_id,user_id):
    newFavorite = FavoriteStarship(
        user_id = user_id,
        starship_id = starship_id
    )
    db.session.add(newFavorite)
    db.session.commit()
    return jsonify({"msg":"La Nave Espacial Favorita esta Guardada"}), 200

## Ruta para Eliminar una Nave Espacial favorita 
@app.route('/favorite/starship/<int:starship_id>/user/<int:user_id>', methods=['DELETE'])
def delete_favorite_starship(starship_id,user_id):
    favorite = FavoriteStarship.query.filter_by(starship_id=starship_id,user_id=user_id).first()
    if favorite is None:
        return jsonify({"msg":"La Nave Espacial favorita no existe" }), 404
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"msg":"La Nave Espacial Favorita esta Eliminada"}), 200


## RUTAS DE LOS VEHICULOS

## Ruta para obtener todos los Vehiculos 
@app.route('/vehicle', methods=['GET'])
def get_all_vehicle():
    vehicles = Vehicle.query.all()
    result = list(map(lambda x: x.serialize(),vehicles))
    return jsonify(result),200

## Ruta para obtener un Vehiculos por ID 
@app.route('/vehicle/<int:vehicle_id>', methods=['GET'])
def get_vehicle_by_id(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    if vehicle is None:
        return jsonify({"msg":"El Vehiculo no existe" }), 404
    return jsonify(vehicle.serialize()),200

## Ruta para crear un Vehiculo favorito 
@app.route('/favorite/vehicle/<int:vehicle_id>/user/<int:user_id>', methods=['POST'])
def create_favorite_vehicle(vehicle_id,user_id):
    newFavorite = FavoriteVehicle(
        user_id = user_id,
        vehicle_id = vehicle_id
    )
    db.session.add(newFavorite)
    db.session.commit()
    return jsonify({"msg":"El Vehiculo Favorito esta Guardado"}), 200

## Ruta para Eliminar un Vehiculo favorito 
@app.route('/favorite/vehicle/<int:vehicle_id>/user/<int:user_id>', methods=['DELETE'])
def delete_favorite_vehicle(vehicle_id ,user_id):
    favorite = FavoriteVehicle.query.filter_by(vehicle_id=vehicle_id,user_id=user_id).first()
    if favorite is None:
        return jsonify({"msg":"El Vehiculo no existe" }), 404
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"msg":"El Vehiculo Favorito esta Eliminado"}), 200


## RUTAS DE LAS ESPECIES

## Ruta para obtener todas las Especies 
@app.route('/specie', methods=['GET'])
def get_all_specie():
    species = Specie.query.all()
    result = list(map(lambda x: x.serialize(),species))
    return jsonify(result),200

## Ruta para obtener una Especie por ID 
@app.route('/specie/<int:specie_id>', methods=['GET'])
def get_specie_by_id(specie_id):
    specie = Specie.query.get(specie_id)
    if specie is None:
        return jsonify({"msg":"La Especie no existe" }), 404
    return jsonify(specie.serialize()),200

## Ruta para crear una Especie favorita 
@app.route('/favorite/specie/<int:specie_id>/user/<int:user_id>', methods=['POST'])
def create_favorite_specie(specie_id,user_id):
    newFavorite = FavoriteSpecie(
        user_id = user_id,
        specie_id = specie_id
    )
    db.session.add(newFavorite)
    db.session.commit()
    return jsonify({"msg":"El Vehiculo Favorito esta Guardado"}), 200

## Ruta para Eliminar una Specie favorita 
@app.route('/favorite/specie/<int:specie_id>/user/<int:user_id>', methods=['DELETE'])
def delete_favorite_specie(specie_id ,user_id):
    favorite = FavoriteSpecie.query.filter_by(specie_id=specie_id,user_id=user_id).first()
    if favorite is None:
        return jsonify({"msg":"La Especie no existe" }), 404
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"msg":"La Especie Favorita esta Eliminada"}), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
