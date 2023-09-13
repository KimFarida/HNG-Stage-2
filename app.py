from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flasgger import Swagger
from flask_restful import Api
import yaml



app = Flask(__name__)
api = Api(app)
# Load Swagger content from the file
with open('swagger.yaml', 'r') as file:
    swagger_config = yaml.load(file, Loader=yaml.FullLoader)

# Use the loaded swagger_config when initializing flasgger
Swagger(app, template=swagger_config)

app.config.from_object(Config)

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address= db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Person %r>' % self.name
    
    __table_args__ = (
        db.CheckConstraint('age >= 0', name='age_non_negative'),
    )

    @classmethod
    def validate_name_length(cls, name):
        max_length = 80  # Define the maximum length for the name field
        if len(name) > max_length:
            raise ValueError(f'Name must be {max_length} characters or less.')

    @classmethod
    def validate_address_length(cls, address):
        max_length = 255  # Define the maximum length for the address field
        if len(address) > max_length:
            raise ValueError(f'Address must be {max_length} characters or less.')

    @staticmethod
    def validate_age_non_negative(age):
        if age < 0:
            raise ValueError('Age must be a non-negative integer.')

@app.route('/api', methods=['POST'])
def create_person():
    """
    Create Person Endpoint
    """
    data = request.get_json()

    if not data:
        return {'error': 'No input data was provided'}, 400

    name = data.get('name')
    age = data.get('age')
    address = data.get('address')

    if not name or not age or not address:
        return {'error': 'Missing required parameters'}, 400

    if not isinstance(name, str):
        return {'error': 'Name must be a string'}, 400

    if not isinstance(age, int) or age < 0:
        return {'error': 'Age must be a positive integer'}, 400

    if not isinstance(address, str):
        return {'error': 'Address must be a string'}, 400

    new_person = Person(name=name, age=age, address=address)

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
        'name': person.name,
        'age': person.age,
        'address': person.address
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
    age = data.get('age', person.age)
    address = data.get('address', person.address)

    if not isinstance(name, str) or not isinstance(age, int) or age < 0 or not isinstance(address, str):
        return jsonify({'error': 'Invalid data format'}), 400

    person.name = name
    person.age = age
    person.address = address

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

# @app.route('/api/persons', methods=['GET'])
# def get_persons():
#     persons = Person.query.all()  # Query all persons from the database
#     person_list = []

#     for person in persons:
#         person_data = {
#             'id': person.id,
#             'name': person.name,
#             'age': person.age,
#             'address': person.address
#         }
#         person_list.append(person_data)

#     return jsonify(person_list)

@app.cli.command("create_tables")
def create_tables():
    db.create_all()
    print("Database tables created")

if __name__ == '__main__':
    app.run(debug=True)
