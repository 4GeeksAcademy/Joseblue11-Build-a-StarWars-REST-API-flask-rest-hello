from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    last_name = db.Column(db.String(250), unique=False, nullable=False)  
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean, unique=False, nullable=False)
    favorite_character = db.relationship('FavoriteCharacter', backref='user', lazy=True)
    favorite_planet = db.relationship('FavoritePlanet', backref='user', lazy=True)
    favorite_starship = db.relationship('FavoriteStarship', backref='user', lazy=True)  
    favorite_vehicle = db.relationship('FavoriteVehicle', backref='user', lazy=True)  
    favorite_specie = db.relationship('FavoriteSpecie', backref='user', lazy=True)
    
    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "last_name":self.last_name,
            "email": self.email,
            "is_active":self.is_active
            # Exclude password for security reasons
        }

class Character(db.Model):
    __tablename__= "character"
    id = db.Column(db.Integer, primary_key=True)
    # El nombre de esta persona.
    name = db.Column(db.String(120), unique=True, nullable=False)
    # El género de esta persona.
    gender = db.Column(db.String(80), unique=False, nullable=False)
    # El color de ojos de esta persona.
    eyes_color = db.Column(db.String(80), unique=False, nullable=False)
    # El color de pelo de esta persona.
    hair_color = db.Column(db.String(80), unique=False, nullable=False)
    # La altura de la persona en centímetros.
    height = db.Column(db.Integer, unique=False, nullable=False)
    # La masa de la persona en kilogramos.
    mass = db.Column(db.Integer, unique=False, nullable=False)
    # El color de piel de esta persona.
    skin_color = db.Column(db.String(80), unique=False, nullable=False)
    favorite_character = db.relationship('FavoriteCharacter', backref='character', lazy=True)

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "eyes_color": self.eyes_color,
            "hair_color": self.hair_color,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
        }

class Planet(db.Model):
    __tablename__= "planet"
    id = db.Column(db.Integer, primary_key=True)
    # El nombre de este planeta.
    name = db.Column(db.String(120), unique=True, nullable=False)
    # El clima de este planeta.
    climate = db.Column(db.String(80), unique=False, nullable=False)
    # El terreno de este planeta.
    terrain = db.Column(db.String(80), unique=False, nullable=False)
    # El número de días estándar que le toma a este planeta completar una única órbita de su estrella local.
    orbital_period = db.Column(db.Integer, unique=False, nullable=False)
    # El diámetro de este planeta en kilómetros.
    diameter = db.Column(db.Integer, unique=False, nullable=False)
    # El porcentaje de la superficie del planeta que es agua o masas de agua naturales.
    gravity = db.Column(db.Integer, unique=False, nullable=False)
    # El número de horas estándar que le toma a este planeta completar una sola rotación sobre su eje.
    surface_water = db.Column(db.Integer, unique=False, nullable=False)
    # El número de horas estándar que le toma a este planeta completar una sola rotación sobre su eje.
    rotation_period = db.Column(db.Integer, unique=False, nullable=False)
    # La población promedio de seres sintientes que habitan este planeta.
    population = db.Column(db.Integer, unique=False, nullable=False)
    favorite_planet = db.relationship('FavoritePlanet', backref='planet', lazy=True)
    


    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "surface_water": self.surface_water,
            "rotation_period": self.rotation_period,
            "population": self.population,
        }

class Starship(db.Model):
    __tablename__= "starship"
    id = db.Column(db.Integer, primary_key=True)
    # El nombre de esta nave estelar
    name = db.Column(db.String(120), unique=True, nullable=False)
    # El modelo oficial de esta nave estelar.
    model = db.Column(db.String(120), unique=True, nullable=False)
    # La clase de esta nave espacial.
    starship_class = db.Column(db.String(120), unique=True, nullable=False)   
    # El fabricante de esta nave estelar.
    manufacturer = db.Column(db.String(120), unique=True, nullable=False)
    # El costo de esta nueva nave espacial.
    cost_in_credits = db.Column(db.Integer, unique=False, nullable=False)
    # La longitud de esta nave estelar en metros.
    length = db.Column(db.Integer, unique=False, nullable=False)
    # La cantidad de personal necesario para ejecutar o pilotar esta nave estelar.
    crew = db.Column(db.Integer, unique=False, nullable=False)
    # La cantidad de personas no esenciales que esta nave espacial puede transportar.
    passengers = db.Column(db.Integer, unique=False, nullable=False)
    # La velocidad máxima de esta nave estelar en la atmósfera.
    max_atmosphering_speed = db.Column(db.Integer, unique=False, nullable=False)
    # La clase del hiperimpulsor de esta nave estelar.
    hyperdrive_rating = db.Column(db.String(120), unique=True, nullable=False)
    favorite_starship = db.relationship('FavoriteStarship', backref='starship', lazy=True)

    def __repr__(self):
        return '<Starships %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "starship_class": self.starship_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
        }


class Vehicle(db.Model):
    __tablename__= "vehicle"
    id = db.Column(db.Integer, primary_key=True)
     # El nombre de este Vehiculo
    name = db.Column(db.String(120), unique=True, nullable=False)
    # El modelo oficial de este Vehiculo.
    model = db.Column(db.String(120), unique=True, nullable=False)
    # La clase de este Vehiculo.
    vehicle_class = db.Column(db.String(120), unique=True, nullable=False)
    # El fabricante de este Vehiculo.
    manufacturer = db.Column(db.String(120), unique=True, nullable=False)
    # El costo de este Vehiculo.
    cost_in_credits = db.Column(db.Integer, unique=False, nullable=False)
    # La longitud de este Vehiculo en metros.
    length = db.Column(db.Integer, unique=False, nullable=False)
    # La cantidad de personal necesario para ejecutar o pilotar este Vehiculo.
    crew = db.Column(db.Integer, unique=False, nullable=False)
    # La cantidad de personas no esenciales que esta Vehiculo puede transportar.
    passengers = db.Column(db.Integer, unique=False, nullable=False)
    # La velocidad máxima de este Vehiculo en la atmósfera.
    max_atmosphering_speed = db.Column(db.Integer, unique=False, nullable=False)
    favorite_vehicle = db.relationship('FavoriteVehicle', backref='vehicle', lazy=True)
    
    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
        }
    
class Specie(db.Model):
    __tablename__= "specie"
    id = db.Column(db.Integer, primary_key=True)
    # El nombre de esta especie.
    name = db.Column(db.String(120), unique=True, nullable=False)
    # La clasificación de esta especie.
    classification = db.Column(db.String(120), unique=True, nullable=False)
    # La altura promedio de esta especie en centímetros..
    average_height = db.Column(db.Integer, unique=False, nullable=False)
    # La esperanza de vida promedio de esta especie en años.
    average_lifespan = db.Column(db.Integer, unique=False, nullable=False)
    # Los colores de ojos comunes para esta especie.
    eye_colors = db.Column(db.String(120), unique=True, nullable=False)
    # Los colores de cabello comunes para esta especie.
    hair_colors = db.Column(db.String(120), unique=True, nullable=False)
    # los colores de piel comunes para esta especie, "ninguno" si esta especie no suele tener piel.
    skin_colors = db.Column(db.String(120), unique=True, nullable=False)
    # el idioma comúnmente hablado por esta especie.
    language = db.Column(db.String(120), unique=True, nullable=False)
    favorite_specie = db.relationship('FavoriteSpecie', backref='specie', lazy=True)

    def __repr__(self):
        return '<Specie %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "classification": self.classification,
            "average_height": self.average_height,
            "eye_colors": self.eye_colors,
            "hair_colors": self.hair_colors,
            "skin_colors": self.skin_colors,
            "language": self.language,
        }

class FavoriteCharacter(db.Model):
    __tablename__= "favoriteCharacter"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"), nullable=False)
 
    def __repr__(self):
        return '<FavoriteCharacter %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
        }
class FavoritePlanet(db.Model):
    __tablename__= "FavoritePlanet"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=False)
 
    def __repr__(self):
        return '<FavoritePlanet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
        }

class FavoriteStarship(db.Model):
    __tablename__= "FavoriteStartship"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    starship_id = db.Column(db.Integer, db.ForeignKey("starship.id"), nullable=False)
 
    def __repr__(self):
        return '<FavoriteStarship %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "starship_id": self.starship_id,
        }

class FavoriteVehicle(db.Model):
    __tablename__= "FavoriteVehicle"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"), nullable=False)
 
    def __repr__(self):
        return '<FavoriteVehicle %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehicle_id": self.vehicle_id,
        }
        
class FavoriteSpecie(db.Model):
    __tablename__= "FavoriteSpecie"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    specie_id = db.Column(db.Integer, db.ForeignKey("specie.id"), nullable=False)
 
    def __repr__(self):
        return '<FavoriteSpecie %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "specie_id": self.specie_id,
        }
        
