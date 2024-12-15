from flask import Flask, render_template_string, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

# Root URL (this is the home page)
@app.route('/')
def index():
    return render_template_string(open("email_warmup/index.html").read())

# Endpoint to handle the button click and return modal content
@app.route('/api/warmup/configure', methods=['GET'])
def configure_warmup():
    modal_html = """
    <div class="modal-overlay">
        <div class="modal-content">
            <h3>Warmup Configuration</h3>
            <form action="/api/warmup/save" method="POST">
                <label for="email-count">Emails Per Day</label>
                <input type="number" id="email-count" name="email_count" required>
                <button type="submit">Save Configuration</button>
            </form>
            <button onclick="document.getElementById('warmup-modal').classList.add('hidden')">Close</button>
        </div>
    </div>
    """
    return modal_html

# Endpoint to handle the form submission (optional)
@app.route('/api/warmup/save', methods=['POST'])
def save_warmup_config():
    email_count = request.form.get('email_count')
    # Check if email_count is None or empty
    if not email_count:
        return jsonify({"error": "Email count is required."}), 400
    # Perform any saving logic here
    return jsonify({"message": f"Warmup configuration saved with {email_count} emails per day."})

# Routes for campaigns
@app.route('/api/campaigns', methods=['GET'])
def campaigns():
    return jsonify({"message": "Campaigns will be here."})

@app.route('/api/campaigns/<int:id>', methods=['GET'])
def campaign(id):
    return jsonify({"message": f"Campaign with id {id} will be here."})

@app.route('/api/campaigns/new', methods=['GET'])
def new_campaign():
    modal_html = """
    <div id="campaign-modal" class="modal-overlay">
        <div class="modal-content">
            <h3>Create New Campaign</h3>
            <form action="/api/campaigns/create" method="POST" id="create-campaign-form">
                <label for="campaign-name">Campaign Name</label>
                <input type="text" id="campaign-name" name="campaign_name" required>
                <label for="emails-per-day">Emails per Day</label>
                <input type="number" id="emails-per-day" name="emails_per_day" required>
                <button type="submit">Create Campaign</button>
            </form>
        </div>
    </div>
    """
    return modal_html

# Endpoint to create the campaign (post data)
@app.route('/api/campaigns/create', methods=['POST'])
def create_campaign():
    try:
        campaign_name = request.form['campaign_name']
        emails_per_day = request.form['emails_per_day']

        # Debugging: Print received data
        print(f"Received data: campaign_name={campaign_name}, emails_per_day={emails_per_day}")

        # Check for missing fields
        if not campaign_name or not emails_per_day:
            return jsonify({"error": "Both campaign name and emails per day are required."}), 400

        # Perform saving logic (e.g., save to database or process data)
        return jsonify({"message": f"New campaign '{campaign_name}' created with {emails_per_day} emails per day."})

    except Exception as e:
        # Log error message
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred while creating the campaign."}), 500


if __name__ == '__main__':
    app.run(debug=True)
