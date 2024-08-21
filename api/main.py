from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

app = Flask(__name__)

# Récupérer la clé API Pinterest depuis l'environnement
PINTEREST_API_KEY = os.getenv("PINTEREST_API_KEY")

@app.route('/api/pinterest', methods=['GET'])
def search_pinterest():
    query = request.args.get('query')
    
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    # URL de l'API Pinterest (exemple: recherche de Pins)
    pinterest_url = f"https://api.pinterest.com/v1/pins/search/?query={query}&access_token={PINTEREST_API_KEY}"

    try:
        response = requests.get(pinterest_url)
        response.raise_for_status()
        return jsonify(response.json()), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
