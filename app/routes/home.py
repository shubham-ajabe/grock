# app/routes/home.py
from flask import Blueprint
from services.greeting_service import get_greeting

# Create a blueprint for the home route
home = Blueprint('home', __name__)

# Define a route for the home page
@home.route('/')
def index():
    greeting_message = get_greeting()
    return greeting_message
