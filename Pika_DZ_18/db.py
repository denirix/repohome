from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select, text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

connection_string = "sqlite:///DZ_Pika_15.sqlite"
engine = create_engine(connection_string)

class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, autoincrement=True, primary_key=True)
    cost = Column(Integer)
    name = Column(String(20))
    client_id = Column(Integer, ForeignKey("clients.id"))

    def __init__(self, cost, name, client_id):
        self.cost = cost
        self.name = name
        self.client_id = client_id

    def __init__(self, cost, name, id):
        self.cost = cost
        self.name = name
        self.id = id

    def __str__(self):
        return f"{self.name} {self.cost}"

    def __repr__(self):
        return f"{self.name} {self.cost}"


connection_string = "sqlite:///DZ_Pika_15.sqlite"
engine = create_engine(connection_string)


def get_orders():
    orders = []
    connection = engine.connect()
    query_1 = connection.execute(
    text(
        "SELECT * FROM orders "
        )
    )
    for row in query_1.mappings():
        id = row["id"]
        name = row["name"]
        cost = row["cost"]
        orders.append(Orders(cost, name, id))

    connection.close()
    return orders

def get_order_by_id(id):
    connection = engine.connect()
    query_1 = connection.execute(
    text(
        f"SELECT * FROM orders WHERE id={id}"
        )
    )
    order = query_1.fetchone()
    id,cost,name = (order[0],order[1], order[2])
    connection.close()
    return Orders(cost, name, id)

def updateOrder(id,name,cost):
    connection = engine.connect()
    query_1 = connection.execute(
    text(
        f"UPDATE orders SET name='{name}', cost={cost} WHERE id={id}"
        )
    )
    connection.commit()
    connection.close()

def deleteOrder(id):
    connection = engine.connect()
    query_1 = connection.execute(
    text(
        f"DELETE FROM orders WHERE id={id}"
        )
    )
    connection.commit()
    connection.close()

def addOrder(client_id,name,cost):
    connection = engine.connect()
    query_1 = connection.execute(
    text(
        f"INSERT INTO orders (client_id, name, cost) values ({client_id}, '{name}', {cost})"
        )
    )
    connection.commit()
    connection.close()
