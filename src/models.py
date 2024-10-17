from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Planets(db.Model):
    __tablename__ = 'Planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))
    gravity = db.Column(db.String(250))
    population = db.Column(db.String(250))
    climate = db.Column(db.String(250))

class Vehicles(db.Model):
    __tablename__ = 'Vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    lastname = db.Column(db.String(250))
    description = db.Column(db.String(250))
    model = db.Column(db.String(250))
    manufacturer = db.Column(db.String(250))

class Characters(db.Model):
    __tablename__ = 'Characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))
    color_eyes = db.Column(db.String(250))
    birth_year = db.Column(db.String(250))
    gender = db.Column(db.String(6))
    hair_color = db.Column(db.String(250))


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))
    fecha_ingreso = db.Column(db.String(250))
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

class Login(db.Model):
    __tablename__ = 'Login'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250))
    password = db.Column(db.String(250))
    usuario_id = db.Column(db.Integer, db.ForeignKey("User.id"))

class Favorites(db.Model):
    __tablename__ = 'Favorites'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    favorites = db.Column(db.Enum('personaje', 'vehiculo', 'planeta', name='favorite_type'))

class FavoriteCharacters(db.Model):
    __tablename__ = 'favoriteCharacters'
    id = db.Column(db.Integer, primary_key=True)

class FavoriteVehicles(db.Model):
    __tablename__ = 'FavoriteVehicles'
    id = db.Column(db.Integer, primary_key=True)

class FavoritePlanets(db.Model):
    __tablename__ = 'FavoritePlanets'
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }