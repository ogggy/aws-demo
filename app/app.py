from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index_1():
    return render_template('index.html')

@app.route('/cart.html')
def cart():
    return render_template('cart.html')


@app.route('/checkout.html')
def checkout():
    return render_template('checkout.html')

@app.route('/shop.html')
def shop():
    return render_template('shop.html')


@app.route('/single-product.html')
def single_product():
    return render_template('single-product.html')

app.run(host='0.0.0.0', port=81)