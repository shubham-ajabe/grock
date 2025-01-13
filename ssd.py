from flask import Flask
from home import home  # Import the Blueprint from home.py

# Initialize the Flask app
app = Flask(__name__)

# Register the Blueprint for routes
app.register_blueprint(home)

if __name__ == '__main__':
    app.run()  # For local testing, Render will use Gunicorn
