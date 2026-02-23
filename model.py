import numpy as np
import joblib

# Path to trained model
MODEL_PATH = "./model/rainfall_model.pkl"

# Feature 
FEATURES = [
    "id",         
    "day",
    "pressure",
    "maxtemp",
    "temparature",  
    "mintemp",
    "dewpoint",
    "humidity",
    "cloud",
    "sunshine",
    "winddirection",
    "windspeed"
]

# Load model once
model = joblib.load(MODEL_PATH)


def predict_rainfall(input_dict):
    """
    Takes input as a dictionary of feature values
    Returns prediction (0 or 1)
    """

    # Arrange inputs in correct feature order
    input_data = [float(input_dict[feature]) for feature in FEATURES]

    # Convert to numpy array
    input_array = np.array(input_data).reshape(1, -1)

    # Predict
    prediction = model.predict(input_array)[0]

    return int(prediction)
