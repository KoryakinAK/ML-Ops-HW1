from flask import Flask

app = Flask("ML-OPS")

availableModels = [
    "model1",
    "model2"
]

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/getAvailableModels")
def getAvailableModels():
    return availableModels
