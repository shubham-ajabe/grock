from flask import Blueprint, render_template, request, jsonify
import logging

logging.basicConfig(filename='webhook.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Create a Blueprint for routes
home = Blueprint('home', __name__)

# Store webhook data for display (optional for testing)
webhook_data_store = []

@home.route('/')  # Home route
def index():
    return render_template('index.html', webhook_data=webhook_data_store)

@home.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Handle browser-based GET requests
        return jsonify({"status": "Webhook is live!"}), 200

    if request.method == 'POST':
        # Parse the incoming JSON payload
        data = request.json
        if not data:
            logging.error("Invalid payload: No data received")
            return jsonify({"error": "Invalid payload: No data received"}), 400

        # Extract the auth token from the payload
        auth = data.get('auth', {})
        access_token = auth.get('access_token', '')

        # Replace 'YOUR_VALID_ACCESS_TOKEN' with your actual Bitrix24 token
        VALID_TOKEN = "vyci2oo2qbtykj55ndjnlwuq8kks6clr"

        if access_token != VALID_TOKEN:
            logging.error("Unauthorized: Invalid access token")
            return jsonify({"error": "Unauthorized: Invalid access token"}), 401

        # Log the successful reception of data
        logging.info(f"Webhook received: {data}")
        return jsonify({"status": "success", "message": "Webhook received!"}), 200

# Add routes for additional pages
@home.route('/about_us')  # About Us route
def about_us():
    return render_template('about_us.html')

@home.route('/our_services')  # Our Services route
def our_services():
    return render_template('our_services.html')

@home.route('/business_sector')  # Business Sector route
def business_sector():
    return render_template('business_sector.html')

@home.route('/blog')  # Blog route
def blog():
    return render_template('blog.html')

@home.route('/quick_links')  # Quick Links route
def quick_links():
    return render_template('quick_links.html')

@home.route('/our_vision')  # Our Vision route
def our_vision():
    return render_template('our_vision.html')
