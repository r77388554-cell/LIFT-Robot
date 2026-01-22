from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/trigger", methods=["GET", "POST"])
def trigger():
    print("✅ Trigger received!")
    return {"status": "ok", "message": "Trigger confirmed"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)