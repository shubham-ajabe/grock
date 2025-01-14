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

webhook_data_store = []
@home.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Render the UI with stored webhook data
        return render_template('index.html', data=webhook_data_store)

    if request.method == 'POST':
        # Parse incoming JSON payload
        data = request.json
        if not data:
            logging.error("Invalid payload: No data received")
            return jsonify({"error": "Invalid payload: No data received"}), 400

        # Extract the auth token
        auth = data.get('auth', {})
        access_token = auth.get('access_token', '')

        # Replace with your actual Bitrix24 token
        VALID_TOKEN = "YOUR_VALID_ACCESS_TOKEN"

        if access_token != VALID_TOKEN:
            logging.error("Unauthorized: Invalid access token")
            return jsonify({"error": "Unauthorized: Invalid access token"}), 401

        # Extract event type
        event = data.get("event", "")
        event_data = data.get("data", {})

        # Handle OnTaskAdd
        if event == "OnTaskAdd":
            fields_after = event_data.get("FIELDS_AFTER", {})
            task_id = fields_after.get("ID", "N/A")
            task_title = fields_after.get("TITLE", "N/A")
            logging.info(f"Task Added: ID={task_id}, Title={task_title}")
            webhook_data_store.append({
                "event": "OnTaskAdd",
                "task_id": task_id,
                "task_title": task_title,
                "fields_after": fields_after
            })

        # Handle OnTaskUpdate
        elif event == "OnTaskUpdate":
            fields_before = event_data.get("FIELDS_BEFORE", {})
            fields_after = event_data.get("FIELDS_AFTER", {})
            task_id = fields_after.get("ID", "N/A")
            old_title = fields_before.get("TITLE", "N/A")
            new_title = fields_after.get("TITLE", "N/A")
            logging.info(f"Task Updated: ID={task_id}, Old Title={old_title}, New Title={new_title}")
            webhook_data_store.append({
                "event": "OnTaskUpdate",
                "task_id": task_id,
                "fields_before": fields_before,
                "fields_after": fields_after
            })

        # Unknown Event
        else:
            logging.warning(f"Unhandled event type: {event}")
            return jsonify({"error": f"Unhandled event type: {event}"}), 400

        # Return success response
        return jsonify({"status": "success", "message": f"{event} event processed"}), 200

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
