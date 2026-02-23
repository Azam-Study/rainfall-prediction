from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from model import predict_rainfall, FEATURES

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html") 

@app.route("/", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        
        for feature in FEATURES:
            if feature not in data:
                return jsonify({"error": f"Missing feature: {feature}"}), 400
        
        prediction = predict_rainfall(data)
        return jsonify({"rainfall": prediction})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)