from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    with open("/data/orders.txt", "a") as f:
        f.write("Order saved\n")
    return "Order Stored!"

app.run(host="0.0.0.0", port=5002)
