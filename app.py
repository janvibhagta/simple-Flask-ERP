from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
products = [
    {"id": 1, "name": "Product A", "quantity": 100},
    {"id": 2, "name": "Product B", "quantity": 200},
]

orders = []

@app.route('/')
def home():
    return "Welcome to Simple Flask ERP Demo"

# Products API
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    new_id = max([p["id"] for p in products]) + 1 if products else 1
    product = {"id": new_id, "name": data["name"], "quantity": data["quantity"]}
    products.append(product)
    return jsonify(product), 201

# Orders API
@app.route('/api/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.json
    order_id = len(orders) + 1
    order = {"id": order_id, "product_id": data["product_id"], "quantity": data["quantity"]}
    # Simple stock check
    product = next((p for p in products if p["id"] == data["product_id"]), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    if product["quantity"] < data["quantity"]:
        return jsonify({"error": "Insufficient quantity"}), 400
    product["quantity"] -= data["quantity"]
    orders.append(order)
    return jsonify(order), 201

if __name__ == '__main__':
    app.run(debug=True)
