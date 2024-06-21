from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import os
import requests
from policies import enforce_access_control
from opal_client.data import DataUpdate
import opal_client

load_dotenv()

app = Flask(__name__)

WEATHER_API_URL = os.getenv('WEATHER_API_URL')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_health_tips():
    user_role = request.form.get('role')
    action = "view"
    
    if not enforce_access_control(user_role, action):
        return jsonify({"error": "Access denied"}), 403

    location = request.form.get('location')
    health_tips = fetch_health_tips(location)
    
    return jsonify(health_tips)

def fetch_health_tips(location):
    try:
        response = requests.get(WEATHER_API_URL, params={'key': WEATHER_API_KEY, 'q': location})
        response.raise_for_status()
        data = response.json()
        
        health_tips = generate_tips(data)
        return {"tips": health_tips, "location": location}
    except Exception as e:
        return {"error": str(e)}

def generate_tips(weather_data):
    condition = weather_data['current']['condition']['text']
    temp_c = weather_data['current']['temp_c']
    
    tips = []
    if 'rain' in condition.lower():
        tips.append("It's raining, carry an umbrella!")
    if temp_c < 10:
        tips.append("It's cold outside, wear warm clothes.")
    elif temp_c > 30:
        tips.append("Stay hydrated and avoid direct sunlight.")
    else:
        tips.append("The weather is mild, have a nice day!")

    return tips

if __name__ == '__main__':
    app.run(debug=True)
