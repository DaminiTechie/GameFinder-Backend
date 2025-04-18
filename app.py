from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)


CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:5173", "http://127.0.0.1:5173"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Add a root route to prevent 404
@app.route('/')
def home():
    return "Flask Backend Running"


@app.route('/api/games', methods=['GET'])
def get_games():
    games = [
        {"id": 1, "name": "Elden Ring"},
        {"id": 2, "name": "Cyberpunk 2077"}
    ]
    return jsonify(games)

if __name__ == '__main__':
    app.run(debug=True, port=5000)