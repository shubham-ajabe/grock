from flask import Blueprint, render_template, request, jsonify

# Create a Blueprint for routes
home = Blueprint('home', __name__)

# Store webhook data for display (optional for testing)
webhook_data_store = []

@home.route('/')  # Home route
def index():
    return render_template('index.html', webhook_data=webhook_data_store)

@home.route('/webhook', methods=['POST'])  # Webhook route
def webhook_handler():
    # Parse the incoming webhook data
    if request.is_json:
        webhook_data = request.json
        webhook_data_store.append(webhook_data)  # Store for display
        print(f"Webhook received: {webhook_data}")
        return jsonify({"status": "success", "message": "Webhook received!"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid data format!"}), 400
