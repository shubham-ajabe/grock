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
