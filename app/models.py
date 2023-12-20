from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import validates


db = SQLAlchemy()

class Hero(db.Model):

    __tablename__ = 'heros'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)
    powers = db.relationship('Power', secondary='heropowers', backref='heroes')

class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

class HeroPower(db.Model):
    __tablename__ = 'heropowers'
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heros.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)
    strength = db.Column(db.String(100), nullable=False)

    hero = db.relationship('Hero', backref='heropowers')
    power = db.relationship('Power')
    

    __table_args__ = (
        CheckConstraint(
            strength.in_(['Strong', 'Weak', 'Average']),
            name='check_strength_values'
        ),
    )

    @validates('strength')
    def validate_strength(self, key, value):
        if value not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be one of: 'Strong', 'Weak', 'Average'")
        return value

    @validates('description')
    def validate_description(self, key, value):
        if len(value.strip()) < 20:
            raise ValueError("Description must be at least 20 characters long.")
        return value

# add any models you may need. 