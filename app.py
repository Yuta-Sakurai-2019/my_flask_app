from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/mydatabase'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello, {name}"

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name} for user in users])

if __name__ == '__main__':
    app.run(debug=True)