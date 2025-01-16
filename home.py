
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
    global bitrix_request_received, webhook_data_store

    if request.method == 'POST':
        # Log the incoming POST request
        logging.info("Received POST request from Bitrix24")
        logging.info(f"Headers: {request.headers}")
        logging.info(f"Body: {request.data.decode('utf-8')}")

        # Parse the incoming POST request
        data = request.json
        if not data:
            logging.error("No data received in POST request.")
            return jsonify({"message": "No data received"}), 400

        # Extract data from Bitrix24 payload
        event_name = data.get('event', 'No Event Name Provided')
        fields_after = data.get('data', {}).get('FIELDS_AFTER', {})
        task_id = fields_after.get('ID', 'No Task ID Provided')
        task_title = fields_after.get('TITLE', 'No Title Provided')

        # Store the extracted data
        webhook_data_store.append({
            "event": event_name,
            "task_id": task_id,
            "task_title": task_title
        })

        # Limit data store size to prevent overflow
        if len(webhook_data_store) > 10:
            webhook_data_store.pop(0)

        # Set the flag to True
        bitrix_request_received = True

        # Respond with a success message to Bitrix24
        return jsonify({"message": "Webhook POST request received and processed"}), 200

    # Render the HTML page with the received data
    return render_template('business_sector.html', received=bitrix_request_received, data=webhook_data_store)

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
