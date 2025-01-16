from flask import Blueprint, render_template, request, jsonify
import logging

# Configure logging
logging.basicConfig(filename='webhook.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Create a Blueprint for this module
home = Blueprint('home', __name__)

# Store webhook data
webhook_requests = []

@home.route('/webhook', methods=['GET', 'POST'])
def webhook():
    global webhook_requests

    if request.method == 'POST':
        # Parse the incoming POST request payload
        data = request.json
        if not data:
            logging.error("No data received in POST request.")
            return jsonify({"message": "Invalid payload: No data received"}), 400

        # Extract event details
        event_name = data.get('event', 'No Event Name Provided')
        fields_after = data.get('data', {}).get('FIELDS_AFTER', {})
        task_id = fields_after.get('ID', 'No Task ID Provided')
        task_title = fields_after.get('TITLE', 'No Title Provided')

        # Append the data to the global data store
        webhook_requests.append({
            "event": event_name,
            "task_id": task_id,
            "task_title": task_title
        })

        # Limit the list to the most recent 10 events
        if len(webhook_requests) > 10:
            webhook_requests.pop(0)

        # Log the received payload
        logging.info(f"Received Payload: {data}")
        logging.info(f"Processed Event: {event_name}, Task ID: {task_id}, Task Title: {task_title}")

        # Respond to Bitrix24 webhook
        return jsonify({"message": "Webhook received and processed successfully"}), 200

    # For GET requests, render the stored events on the HTML page
    return render_template('business_sector.html', requests=webhook_requests)
