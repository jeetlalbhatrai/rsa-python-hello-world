from flask import Flask, request, jsonify
from classify import classify_value

app = Flask(__name__)

@app.route("/classify")
def classify():
    try:
        value = int(request.args.get("value"))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid or missing 'value' parameter"}), 400
    return jsonify(classify_value(value))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
