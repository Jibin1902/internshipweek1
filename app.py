from flask import Flask, request, jsonify
import numpy as np
import joblib  # To load the trained model

app = Flask(_name_)

# Load the trained machine learning model (Assume it's already trained)
model = joblib.load("grade_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Extracting input values from frontend
    attendance = data["attendance"]
    study_hours = data["study_hours"]
    assignment_score = data["assignment_score"]

    # Convert inputs into numpy array for prediction
    features = np.array([[attendance, study_hours, assignment_score]])

    # Predict the grade
    predicted_grade = model.predict(features)[0]

    return jsonify({"grade": round(predicted_grade, 2)})

if _name_ == "_main_":
    app.run(debug=True)
