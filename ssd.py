from flask import Flask
from home import home  # Import the blueprint

# Create the Flask application
app = Flask(__name__)

# Register the blueprint
app.register_blueprint(home)

if __name__ == '__main__':
    app.run(debug=True)
