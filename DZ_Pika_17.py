from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select, text
from flask import Flask, render_template

connection_string = "sqlite:///DZ_Pika_15.sqlite"
engine = create_engine(connection_string)

class Orders():

    def __init__(self, id, cost, name, client_id):
        self.id = id
        self.cost = cost
        self.name = name
        self.client_id = client_id

app = Flask(__name__)

ord = []

@app.route('/', methods=["GET"])
def orders():
    global ord
    return render_template("index.html", data = ord)

def initDB():
    connection = engine.connect()
    query_1 = connection.execute(
        text(
            "SELECT * FROM orders"
        )
    )
    for row in query_1.mappings():
        id = row["id"]
        cost = row["cost"]
        name = row["name"]
        client_id = row["client_id"]
        global ord
        print(
            f"id: {id}\n name: {name}\n cost: {cost}\n client_id: {client_id}"
        )
        ord.append(Orders(id, cost, name, client_id))
    connection.close()

if __name__ == "__main__":
    initDB()
    app.run(debug=True)
