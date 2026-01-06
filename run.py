# run.py

from flask import Flask, request, jsonify
import os   # necessário para pegar a porta do Heroku

app = Flask(__name__)

# ---------------------------
# Calculator logic
# ---------------------------
def calculate_logic(option, num1=None, num2=None):
    """
    Receives an option ("1"-"4") and two numbers.
    Returns result or error message.
    """
    try:
        num1 = float(num1)
        num2 = float(num2)
    except (TypeError, ValueError):
        return "❌ Invalid numbers"

    if option == "1":
        return num1 + num2
    elif option == "2":
        return num1 - num2
    elif option == "3":
        return num1 * num2
    elif option == "4":
        if num2 == 0:
            return "❌ Error: division by zero."
        return num1 / num2
    else:
        return "❌ Invalid option"

# ---------------------------
# API routes
# ---------------------------
@app.route("/")
def index():
    return "Calculator API is running!"

@app.route("/calculate", methods=["POST"])
def calculate():
    """
    Receives JSON with:
    {
        "option": "1",
        "num1": "10",
        "num2": "5"
    }
    Returns JSON:
    {
        "result": 15
    }
    """
    data = request.json
    option = data.get("option")
    num1 = data.get("num1")
    num2 = data.get("num2")
    result = calculate_logic(option, num1, num2)
    return jsonify({"result": result})

# ---------------------------
# Run locally or on Heroku
# ---------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Heroku fornece a porta
    app.run(host="0.0.0.0", port=port, debug=True)