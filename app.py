from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import mysql.connector
from prettytable import PrettyTable
import datetime

app = Flask(__name__, template_folder='my_web_app/templates')

# Your existing code here
db = mysql.connector.connect (
    host = 'localhost',
    user = 'rahul',
    password  = 'Rahul@123',
    database = 'my_db',
    port = '3306'
)
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bakery_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS cust_bill (
    order_id INT,
    customer_name VARCHAR(255),
    cake VARCHAR(255),
    quantity INT,
    cost_per_cake INT,
    sum_of_each_cake INT,
    order_date DATETIME,
    FOREIGN KEY (order_id) REFERENCES bakery_orders(order_id)
)         
""")

db.commit()

menu = {'Classic_Chocolate':30,'Vanilla':40,'Red_Velvet':45,'Bliss':35,'Cookies':35}
# menu = {'a':30,'b':40,'c':45,'d':35,'e':35}
bill = {}
order = {}
print("MENU : ",menu)

@app.route('/')
def index():
    return render_template('index.html')

def add_order_to_database(order_id, customer_name, cake, quantity, cost_per_cake, total_cost, order_date):
    pass

@app.route('/add_orders', methods=['GET', 'POST'])
def add_orders():
    return render_template('add_orders.html')

@app.route('/view_orders', methods=['GET', 'POST'])
def view_orders():
    # Your existing view_orders_from_database() code here
    return render_template('view_orders.html', orders=orders, total_amount=total_amount)

@app.route('/cancel_order', methods=['GET', 'POST'])
def cancel_order():
    # Your code
    return render_template('cancel_order.html')

@app.route('/save_to_excel', methods=['GET', 'POST'])
def save_to_excel():
    # Your code
    return render_template('save_to_excel.html')

@app.route('/update_orders', methods=['GET', 'POST'])
def update_orders():
    # Your code
    return render_template('update_orders.html')

@app.route('/view_order_by_id', methods=['GET', 'POST'])
def view_order_by_id():
    # Your code
    return render_template('view_order_by_id.html')




# Similar route functions for other functionalities (view by order ID, update orders, cancel orders, save to Excel)...

if __name__ == '__main__':
    app.run(debug=True)
