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

    if request.method == 'POST':
        # Log the incoming POST request
        logging.info("Received POST request from Bitrix24")
        logging.info(f"Headers: {request.headers}")
        logging.info(f"Body: {request.data.decode('utf-8')}")

        # Set the flag to True to confirm a request was received
        bitrix_request_received = True

        # Respond with a success message to Bitrix24
        return {"message": "Webhook POST request received"}, 200

    # Render the HTML page with the status of the Bitrix24 POST request
    return render_template('business_sector.html', received=bitrix_request_received)

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
