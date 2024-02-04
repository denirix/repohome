from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select, text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from flask import Flask, make_response, redirect, render_template, request, url_for
from db import addOrder, deleteOrder, get_order_by_id, get_orders, updateOrder

app = Flask(__name__)

@app.route('/', methods=["GET"])
def orders():
    ord = get_orders()
    return render_template("index.html", data = ord)

@app.route('/orders/add', methods=["GET","POST"])
def add():
    if request.method=="POST":
        cost = request.form["cost"]
        name = request.form["name"]
        client_id = request.form["client_id"]
        addOrder(client_id, name, cost)
        return redirect(url_for('orders'))
    return render_template("add.html")

@app.route('/orders/update', methods=["GET","POST"])
def update():
    if request.method=="POST":
        id = request.form["id"]
        cost = request.form["cost"]
        name = request.form["name"]
        updateOrder(id,name, cost)
        return redirect(url_for('orders'))
    id = request.args.get("id")
    if not id:
        return make_response("id not found", 400)
    ord = get_order_by_id(id)
    return render_template("update.html", data = ord)

@app.route('/orders/delete', methods=["POST"])
def delete():
    id = request.form["id"]
    if not id:
        return make_response("id not found", 400)
    deleteOrder(id)
    return redirect(url_for('orders'))

if __name__ == "__main__":
    app.run(debug=True)
