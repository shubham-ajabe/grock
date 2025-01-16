
from flask import Blueprint, render_template, request, jsonify
import logging

logging.basicConfig(filename='webhook.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Create a Blueprint for routes
home = Blueprint('home', __name__)

# Store webhook data for display (optional for testing)
webhook_data_store = []
bitrix_request_received = False  # Track if a Bitrix24 POST request has been received

@home.route('/')  # Home route
def index():
    return render_template('index.html', webhook_data=webhook_data_store)

# Store received webhook data
webhook_data_store = []

@home.route('/webhook', methods=['GET', 'POST'])
def webhook():
    global webhook_data_store

    if request.method == 'POST':
        # Parse the incoming POST request
        data = request.json
        if not data:
            logging.info("No data received in POST request.")
            return jsonify({"message": "No data received"}), 400

        # Extract event details
        event_name = data.get('event', 'No Event Name Provided')
        fields_after = data.get('data', {}).get('FIELDS_AFTER', {})
        task_id = fields_after.get('ID', 'No Task ID Provided')
        task_title = fields_after.get('TITLE', 'No Title Provided')

        # Append the new event data to the list
        webhook_data_store.append({
            "event": event_name,
            "task_id": task_id,
            "task_title": task_title
        })

        # Log the full payload and extracted data
        logging.info(f"Received Payload: {data}")
        logging.info(f"Processed Event: {event_name}")
        logging.info(f"Task ID: {task_id}, Task Title: {task_title}")

        # Respond with success
        return jsonify({"message": "Webhook POST request processed successfully"}), 200

    # Handle GET request (refresh page) and display all stored events
    return render_template('business_sector.html', data=webhook_data_store)

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
