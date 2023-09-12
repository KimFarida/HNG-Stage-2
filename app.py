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

# 


# READ: Fetch details of a person
@app.route('/api/<int:user_id>', methods=['GET'])

def get_person(user_id):
    person = Person.query.get(user_id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404

    person_data = {
        'id': person.id,
        'name': person.name,
        'age': person.age,
        'address': person.address
    }
    return jsonify(person_data)

# @app.route('/persons', methods=['GET'])
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
    app.run()
