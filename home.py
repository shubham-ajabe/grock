
from flask import Blueprint, render_template, request, jsonify
import logging

logging.basicConfig(filename='webhook.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Create a Blueprint for routes
home = Blueprint('home', __name__)

@home.route('/')  # Home route
def index():
    return render_template('index.html', webhook_data=webhook_data_store)

# Store received webhook data
webhook_payloads = []

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    global webhook_payloads

    if request.method == 'POST':
        # Capture the incoming POST request payload
        data = request.json
        if not data:
            logging.error("No data received in POST request.")
            return jsonify({"message": "No data received"}), 400

        # Log the raw payload
        logging.info(f"Received Payload: {data}")

        # Store the payload for display
        webhook_payloads.append(data)

        # Limit to the last 10 payloads
        if len(webhook_payloads) > 10:
            webhook_payloads.pop(0)

        # Respond to Bitrix24 webhook
        return jsonify({"message": "Webhook payload received and logged"}), 200

    # Render the HTML page with the captured payloads
    return render_template('business_sector.html', payloads=webhook_payloads)

# Add routes for additional pages
@home.route('/about_us')  # About Us route
def about_us():
    return render_template('about_us.html')

@home.route('/our_services')  # Our Services route
def our_services():
    return render_template('our_services.html')

@home.route('/business_sector')  # Business Sector route
def business_sector():
    global bitrix_request_received
    bitrix_request_received = False  # Reset the flag on page load
    return render_template('business_sector.html', received=bitrix_request_received)

@home.route('/blog')  # Blog route
def blog():
    return render_template('blog.html')

@home.route('/quick_links')  # Quick Links route
def quick_links():
    return render_template('quick_links.html')

@home.route('/our_vision')  # Our Vision route
def our_vision():
    return render_template('our_vision.html')
