from flask import Flask
from pyngrok import ngrok

# Create a Flask app instance
app = Flask(__name__)

# Import and register routes
from app.routes.home import home
app.register_blueprint(home)

if __name__ == '__main__':
    try:
        # Start ngrok tunnel
        public_url = ngrok.connect(5000)
        print("ngrok Public URL:", public_url)
    except Exception as e:
        print(f"An error occurred while starting ngrok: {e}")
        print("Make sure no other ngrok sessions are active and your auth token is valid.")
        exit(1)

    # Run the Flask app
    app.run(debug=True, port=5000)
