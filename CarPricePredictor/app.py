from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('RandomForestRegressor_model.pkl', 'rb'))

@app.route('/')
def home():
    return open('index.html').read()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    # Extracting values from form data
    vehicle_age = float(data.get('vehicle_age', 0))
    km_driven = float(data.get('km_driven', 0))
    mileage = float(data.get('mileage', 0))
    engine = float(data.get('engine', 0))
    max_power = float(data.get('max_power', 0))
    seats = float(data.get('seats', 0))
    seller_type = [float(data.get('seller_type_Dealer', 0)),
                   float(data.get('seller_type_Individual', 0)),
                   float(data.get('seller_type_Trustmark Dealer', 0))]
    fuel_type = [float(data.get('fuel_type_CNG', 0)),
                 float(data.get('fuel_type_Diesel', 0)),
                 float(data.get('fuel_type_Electric', 0)),
                 float(data.get('fuel_type_LPG', 0)),
                 float(data.get('fuel_type_Petrol', 0))]
    transmission_type = [float(data.get('transmission_type_Automatic', 0)),
                         float(data.get('transmission_type_Manual', 0))]

    # Creating input array with all 16 features
    input_data_model = np.array([vehicle_age, km_driven, mileage, engine, max_power, seats] +
                                seller_type + fuel_type + transmission_type).reshape(1, -1)

    # Predicting car price
    prediction = model.predict(input_data_model)
    return str(prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
