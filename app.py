from flask import Flask, jsonify, request

app = Flask(__name__)

luxury_cars = [
    {"brand": "Lamborghini", "model": "Aventador", "year": 2022, "price": 1200.00, "license_plate": "LMB-001", "available": True},
    {"brand": "Ferrari", "model": "488 GTB", "year": 2021, "price": 1000.00, "license_plate": "FER-002", "available": True},
    {"brand": "Maserati", "model": "Levante", "year": 2020, "price": 800.00, "license_plate": "MAS-003", "available": True},
    {"brand": "Porsche", "model": "911 GT3", "year": 2023, "price": 1100.00, "license_plate": "POR-004", "available": True},
    {"brand": "Rolls Royce", "model": "Ghost", "year": 2022, "price": 1500.00, "license_plate": "RR-005", "available": True},
]

@app.route('/cars', methods=['GET'])
def get_cars():
    brand = request.args.get('brand')
    model = request.args.get('model')
    min_price = request.args.get('min_price', type=int)
    max_price = request.args.get('max_price', type=int)
    available = request.args.get('available')

    results = luxury_cars

    if brand:
        results = [car for car in results if car['brand'].lower() == brand.lower()]

    if model:
        results = [car for car in results if model.lower() in car['model'].lower()]

    if min_price is not None:
        results = [car for car in results if car['price'] >= min_price]

    if max_price is not None:
        results = [car for car in results if car['price'] <= max_price]

    if available is not None:
        is_available = available.lower() == 'true'
        results = [car for car in results if car['available'] == is_available]

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)