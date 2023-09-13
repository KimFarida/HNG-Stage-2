from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db,Person
from flasgger import Swagger
from flask_restful import Api
import yaml
   
app = Flask(__name__)
# Load Swagger content from the file
with open('swagger.yaml', 'r') as file:
    swagger_config = yaml.load(file, Loader=yaml.FullLoader)

# Initialize Flask-RESTful
api = Api(app)

# Initialize Flasgger with the loaded Swagger configuration
Swagger(app, template=swagger_config)

# Load application configuration from Config class
app.config.from_object(Config)

# Initialize the SQLAlchemy database
db.init_app(app)


@app.route('/api', methods=['POST'])
def create_person():
    """
    Create Person Endpoint
    """
    data = request.get_json()

    if not data:
        return {'error': 'No input data was provided'}, 400

    name = data.get('name')
   
    if not isinstance(name, str):
        return {'error': 'Name must be a string'}, 400

    # Check if the user already exists by name
    existing_person = Person.query.filter_by(name=name).first()
    if existing_person:
        return {'error': 'User with the same name already exists'}, 409
       
    new_person = Person(name=name)

    try:
        db.session.add(new_person)
        db.session.commit()
        return {'message': 'New person created successfully'}, 201
    except Exception as e:
        db.session.rollback()
        return {'error': 'Something went wrong while creating the person'}, 500


@app.route('/api/<identifier>', methods=['GET'])
def get_person(identifier):
    """
    Get Person Endpoint
    """
    # Try to fetch by ID first
    person = Person.query.get(identifier)
    
    if person is None:
        # If not found by ID, try to fetch by name
        person = Person.query.filter_by(name=identifier).first()
    
    if not person:
        return jsonify({'error': 'Person not found'}), 404

    person_data = {
        'id': person.id,
        'name': person.name
    }
    return jsonify(person_data)

@app.route('/api/<identifier>', methods=['PUT'])
def update_person(identifier):
    """
    Update Person Endpoint
    """
    # Try to fetch by ID first
    person = Person.query.get(identifier)
    
    if person is None:
        # If not found by ID, try to fetch by name
        person = Person.query.filter_by(name=identifier).first()
    
    if not person:
        return jsonify({'error': 'Person not found'}), 404

    data = request.json

    name = data.get('name', person.name)
  
    if not isinstance(str):
        return jsonify({'error': 'Invalid data format'}), 400
       
   # Check if the user already exists by name
     existing_person = Person.query.filter_by(name=name).first()
   if existing_person:
         return {'error': 'User with the same name already exists'}, 409
    person.name = name
    try:
        db.session.commit()
        return jsonify({'message': 'Person updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Something went wrong while updating the person'}), 500

@app.route('/api/<identifier>', methods=['DELETE'])
def delete_person(identifier):
    """
    Delete Person Endpoint
    """
    
    person = Person.query.get(identifier)
    
    if person is None:
        person = Person.query.filter_by(name=identifier).first()

    if not person:
        return jsonify({'error': 'Person not found'}), 404

    try:
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Something went wrong while deleting the person'}), 500

@app.cli.command("create_tables")
def create_tables():
    db.create_all()
    print("Database tables created")

if __name__ == '__main__':
    app.run(debug=True)
