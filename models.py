from locale import currency
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
#from datetime import DateTime
fake = Faker()
from sqlalchemy import ForeignKey
import random
from app import db

from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin # a mixin class is a normal class but with a few added restrictions in how it can be used. This one is called 'UserMixin'.



class User(UserMixin, db.Model): # ********************* Flask-Login  extension works with application's user model, and expects certain properties and methods to be implemented in it. These are 'is_authenticated', 'is_active', 'is_anonymous' and 'get_id'. You can implemtent these manually or just inherit all of them from a class called UserMixin from flask_login
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50), nullable=False)#
    second_name = db.Column(db.String(75), nullable=False)#
    dob = db.Column(db.String(40), nullable=False)
    balance = db.Column(db.Integer)
    address1 = db.Column(db.String(100), nullable=False)#
    address2 = db.Column(db.String(100), nullable=False)#
    country = db.Column(db.String(100), nullable=False)#
    currency = db.Column(db.String(3))#
    postcode = db.Column(db.String(8), nullable=False)#
    email = db.Column(db.String(320), nullable=False)#
    password = db.Column(db.String(1000), nullable=False)#
    unenc = db.Column(db.String(1000))# REMOVE  IN  THE  LIVE  ENVIRONMENT

    games = db.relationship('Games', backref="user")
    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, passw):
        return check_password_hash(self.password, passw)


class Games(db.Model):
    slot_id = db.Column(db.String, nullable=False)
    game_id = db.Column(db.Integer, primary_key=True)
    reel1 = db.Column(db.Integer, nullable=False)
    reel2 = db.Column(db.Integer, nullable=False)
    reel3 = db.Column(db.Integer, nullable=False)
    stake = db.Column(db.Integer, nullable=False)
    won = db.Column(db.Integer, nullable=True)
    timestamp = db.Column(db.String(20))
    user_id = db.Column(db.Integer, ForeignKey(User.id), nullable=False)

class Transaction(db.Model):
    transactino_id = db.Column(db.Integer, primary_key=True)
    house_win = db.Column(db.Integer(), nullable=True)
    user_win = db.Column(db.Integer(), nullable=True)



def add_user():
    for i in range(10):
        new_password = fake.password()
        user = User(f_name = fake.first_name(),second_name = fake.last_name(), dob = random.randint(8, 90), balance = 200, address1 = fake.street_address(),address2 = fake.city(),postcode = fake.postcode(), email = fake.email(), unenc = new_password)
        user.set_password(new_password)
        user.password = user.password_hash

        db.session.add(user)
        print("new f_name:", user.f_name)
        print("new password:", new_password)
        print("new hashed password:", user.password)
        hashed_password = user.check_password(new_password)
        print(hashed_password)
    db.session.commit()

def query_user(email, posited_password):
    print("Name:")
    users = User.query.filter(User.email==email, User.check_password(User.password, posited_password)==True).all()
    #name = User.query.   

    for user in users:
        print(user.password)
        print(user.f_name)
        print(user.email)
    #return user

# ************ because flask_login knows nothing about databases, it needs the application's help loading a user. For that reason the extension expects that the application will configure a user loader function, that can be called to load a user given the ID. (Usually added to the model.py module.)
@login.user_loader            # **************** the user_loader is registered with Flask-Login with the @login.user_loader decorator. The id that Flask-Login passes to the function as an argument is going to be a string, so databases which use numeric ids need to convert the string to integer as you see below.
def load_user(id):
    return User.query.get(int(id))