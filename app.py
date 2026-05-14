from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__, template_folder='template')

# Load model
with open('soul_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load encoders
with open('label_encoders.pkl', 'rb') as f:
    label_encoders = pickle.load(f)


@app.route('/')
def home():
    return render_template('soul-landing.html')


@app.route('/analyzer')
def analyzer():
    return render_template('soul-analyzer.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        columns = [
            'Gender',
            'Occupation',
            'self_employed',
            'family_history',
            'Days_Indoors',
            'Growing_Stress',
            'Changes_Habits',
            'Mental_Health_History',
            'Mood_Swings',
            'Coping_Struggles',
            'Work_Interest',
            'Social_Weakness'
        ]

        input_data = {}

        for col in columns:
            value = data.get(col)

            if value is None:
                return jsonify({
                    "error": f"Missing value for {col}"
                }), 400

            # Clean input
            value = str(value).strip()

            encoder = label_encoders[col]

            # FIX FOR UNSEEN LABELS
            if value not in encoder.classes_:
                return jsonify({
                    "error": f"Unknown value '{value}' for column '{col}'",
                    "allowed_values": encoder.classes_.tolist()
                }), 400

            encoded_value = encoder.transform([value])[0]
            input_data[col] = [encoded_value]

        # Create dataframe
        df_features = pd.DataFrame(input_data)

        # Predict
        prediction = model.predict(df_features)

        # Decode prediction
        if 'treatment' in label_encoders:
            result = label_encoders['treatment'].inverse_transform(prediction)[0]
        else:
            result = prediction[0]

        return jsonify({
            "prediction": str(result)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == '__main__':
    app.run(debug=True)
