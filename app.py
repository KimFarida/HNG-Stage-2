from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///persons.db'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address= db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Person %r>' % self.name

@app.route('/api', methods = ['POST'])
def create_person():
    '''Create a person'''
    data = request.json

    if not data:
        return jsonify({'error': 'No input data was provided'}), 400

    name = data.get('name')
    age = data.get('age')
    address = data.get('address')

    if not name or not age or not address:
        return jsonify({'error': 'Missing required parameters'}), 400

    if not isinstance(name, str):
        return jsonify({'error': 'Name must be a string'}), 400

    if not isinstance(age, int) or age < 0:
        return jsonify({'error': 'Age must be a positive integer'}), 400

    if not isinstance(address, str):
        return jsonify({'error': 'Address must be a string'}), 400

    new_person = Person(name=name, age=age, address=address)

    try:
        db.session.add(new_person)
        db.session.commit()
        return jsonify({'message': 'New person created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Something went wrong while creating the person'}), 500

@app.route('/api/<identifier>', methods=['GET'])
def get_person(identifier):
    '''Get a person's details by name or id'''
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
    '''Update a person's details by name or id'''
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
    '''Delete a person by name or id'''
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

@app.route('/api/persons', methods=['GET'])
def get_persons():
    persons = Person.query.all()  # Query all persons from the database
    person_list = []

    for person in persons:
        person_data = {
            'id': person.id,
            'name': person.name,
            'age': person.age,
            'address': person.address
        }
        person_list.append(person_data)

    return jsonify(person_list)

@app.cli.command("create_tables")
def create_tables():
    db.create_all()
    print("Database tables created")

if __name__ == '__main__':
    app.run()
