from flask import Flask, render_template

app = Flask(__name__)

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
