from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


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
    return render_template('dashboard.html')  


@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/campaigns')
def campaigns():
    return render_template('campaigns.html')

@app.route('/smart_inbox')
def smart_inbox():
    return render_template('smart_inbox.html')


   


if __name__ == '__main__':
    app.run(debug=True)
