from flask import Flask, render_template, request, jsonify

# Create Flask application
app = Flask(__name__)

# Sample product data (in a real app, this would come from a database)
products = [
    {
        "id": 1,
        "name": "Classic Tee",
        "description": "100% organic cotton",
        "price": 25.00,
        "image": "classic.jpg"
    },
    {
        "id": 2,
        "name": "Mountain Design",
        "description": "Limited edition artwork",
        "price": 35.00,
        "image": "mountain.jpg"
    },
    {
        "id": 3,
        "name": "Eco-Friendly",
        "description": "Made from recycled materials",
        "price": 30.00,
        "image": "eco.jpg"
    }
]

# Home page route
@app.route('/')
def home():
    return render_template('index.html', products=products)

# API route for products
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

# API route for orders
@app.route('/api/orders', methods=['POST'])
def create_order():
    # Get order data from request
    order_data = request.json
    
    # In a real application, you would save this to a database
    # and process payment through Stripe or PayPal
    
    print("Order received:", order_data)
    
    # Return success response
    return jsonify({
        "success": True,
        "message": "Order received successfully!",
        "order_id": "12345"  # In a real app, this would be generated
    })

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
