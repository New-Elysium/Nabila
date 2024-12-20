from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbounce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from datetime import datetime
db = SQLAlchemy(app)

class Campaigns(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    emails_per_day = db.Column(db.Integer, nullable=False)
    total_sent = db.Column(db.Integer, nullable=False)
    success_rate = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class WarmUpEmail(db.Model):
    email = db.Column(db.String(100), primary_key=True)
    status = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    daily_limit = db.Column(db.Integer, nullable=False)
    warm_up_days = db.Column(db.Integer, nullable=False)
    inbox_rate = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return render_template('index.html',)
    return render_template('login.html')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    all_warm_up_emails = WarmUpEmail.query.all()  # Correct model name
    return render_template('dashboard.html', warm_up_emails=all_warm_up_emails)


@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/campaigns')
def campaigns():
    all_campaigns = Campaigns.query.all()
    return render_template('campaigns.html', campaigns=all_campaigns)



@app.route('/smart_inbox')
def smart_inbox():
    return render_template('smart_inbox.html')



@app.route('/warm_up_emails', methods=['GET', 'POST'])
def warm_up_emails():
    if request.method == 'POST':
        email = request.form['email']
        status = request.form['status']
        daily_limit = request.form['daily_limit']
        warm_up_days = request.form['warm_up_days']
        inbox_rate = request.form['inbox_rate']

        # Debugging: Check which table the data is being inserted into
        print(f"Adding to WarmUpEmail Table: {email}")

        # Create a new warm up email instance
        new_warm_up_email = WarmUpEmail(
            email=email,
            status=status,
            daily_limit=int(daily_limit),
            warm_up_days=int(warm_up_days),
            inbox_rate=float(inbox_rate)
        )

        # Add to the database
        db.session.add(new_warm_up_email)
        db.session.commit()

        # Redirect to the dashboard after form submission
        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/add_campaign', methods=['GET', 'POST'])
def add_campaign():
    if request.method == 'POST':
        campaign_name = request.form['campaign_name']
        status = request.form['status']
        emails_per_day = request.form['emails_per_day']
        total_sent = request.form['total_sent']
        success_rate = request.form['success_rate']

        # Debugging: Check which table the data is being inserted into
        print(f"Adding to Campaigns Table: {campaign_name}")

        # Create a new campaign instance
        new_campaign = Campaigns(
            campaign_name=campaign_name,
            status=status,
            emails_per_day=int(emails_per_day),
            total_sent=int(total_sent),
            success_rate=float(success_rate)
        )

        # Add to the database
        db.session.add(new_campaign)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
