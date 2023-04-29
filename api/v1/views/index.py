from flask import jsonify
from api.v1.views import app_views

# Create a route on the app_views Blueprint instance
@app_views.route('/status', methods=['GET'])
def get_status():
    # Return a JSON response with a "status" key and "OK" value
    return jsonify({"status": "OK"})
