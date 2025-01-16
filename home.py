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

@home.route('/webhook', methods=['GET', 'POST'])
def webhook():
    global bitrix_request_received
    global webhook_data_store

    if request.method == 'POST':
        # Parse the incoming POST request
        data = request.json
        if not data:
            logging.info("No data received in POST request.")
            return {"message": "No data received"}, 400

        # Extract the event name (if available)
        event_name = data.get('event', 'No Event Name Provided')

        # Store the event name for display
        webhook_data_store = {"event": event_name}

        # Log the event name
        logging.info(f"Received Event: {event_name}")

        # Confirm receipt to Bitrix24
        return {"message": "Webhook POST request received"}, 200

    # Handle GET request (refresh page)
    bitrix_request_received = False
    return render_template('business_sector.html', event=webhook_data_store.get('event', 'No Data Yet'))

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
