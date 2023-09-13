from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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