from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
car=pd.read_csv("data/cars_dataset.csv")

@app.route('/')
def index():
    vehicle_age
    km_driven
    mileage
    engine
    max_power
    seats
    seller_type
    fuel_type
    transmission_type
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
