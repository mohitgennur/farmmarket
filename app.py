from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "dev-secret-key"

# Sample product data
PRODUCTS = [
    {"id": 1, "name": "Apple", "price": 0.5, "description": "Fresh red apples."},
    {"id": 2, "name": "Orange", "price": 0.6, "description": "Juicy oranges."},
    {"id": 3, "name": "Tomato", "price": 0.3, "description": "Ripe tomatoes."},
]


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/products')
def products():
    return render_template('products.html', products=PRODUCTS)


@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        return render_template('404.html'), 404
    return render_template('product_detail.html', product=product)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # In a real app you'd send/store the message. Here we'll flash a success message.
        flash(f'Thanks {name or "friend"}! We received your message.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
