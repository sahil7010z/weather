from flask import Blueprint, request, jsonify
from utils.weather_api import get_weather

api_bp = Blueprint('api', __name__)

@api_bp.route('/get_weather', methods=['POST'])
def fetch_weather():
    city = request.form.get('city')
    if city:
        data = get_weather(city)
        return jsonify(data)
    return jsonify({"error": "City not provided"}), 400
