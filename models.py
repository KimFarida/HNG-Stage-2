from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    
    def __repr__(self):
        return '<Person %r>' % self.name
    
    @classmethod
    def validate_name_length(cls, name):
        max_length = 80  # Define the maximum length for the name field
        if len(name) > max_length:
            raise ValueError(f'Name must be {max_length} characters or less.')
