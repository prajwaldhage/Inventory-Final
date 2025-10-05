# from timeit import default_number
from flask import Flask, render_template

from init_db import init_db
from logic.dashboardlogic import customer_count, product_count, low_stock

app = Flask(__name__)

init_db()
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/dashboard")
def dashboard():
    data = {
        'customer_count': customer_count(),
        'inventory_items': product_count(),
        'low_stock': low_stock()
    }
    return render_template('dashboard.html', **data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
