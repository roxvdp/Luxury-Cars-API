from flask import Flask, jsonify, request, url_for
import os

app = Flask(__name__, static_folder='static')

# Use relative paths only here
luxury_cars = [
    {"brand": "Lamborghini", "model": "Aventador", "year": 2022, "price": 1200.00, "license_plate": "LMB-001", "available": True, "foto_filename": "img/LamborghiniAventador.webp"},
    {"brand": "Ferrari", "model": "488 GTB", "year": 2021, "price": 1000.00, "license_plate": "FER-002", "available": True, "foto_filename": "img/Ferrari488GTB.jpg"},
    {"brand": "Maserati", "model": "Levante", "year": 2020, "price": 800.00, "license_plate": "MAS-003", "available": True, "foto_filename": "img/MaseratiLevante.avif"},
    {"brand": "Porsche", "model": "911 GT3", "year": 2023, "price": 1100.00, "license_plate": "POR-004", "available": True, "foto_filename": "img/Porsche911GT3.avif"},
    {"brand": "Rolls Royce", "model": "Ghost", "year": 2022, "price": 1500.00, "license_plate": "RR-005", "available": True, "foto_filename": "img/RollsRoyceGhost.avif"},
]

@app.route('/cars')
def get_cars():
    # Clone cars list and attach full URL
    enriched_cars = []
    for car in luxury_cars:
        enriched = car.copy()
        enriched['foto_url'] = url_for('static', filename=car['foto_filename'], _external=True)
        enriched_cars.append(enriched)
    return jsonify(enriched_cars)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
