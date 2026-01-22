from flask import Flask
import requests

# -----------------------------
# Your Make.com webhook URL
MAKE_WEBHOOK_URL = "https://wirily-compartmental-tobie.ngrok-free.dev/trigger"  # replace with YOUR webhook URL
# -----------------------------

app = Flask(__name__)

# -----------------------------
# Trigger route
@app.route("/trigger", methods=["GET", "POST"])
def trigger():
    print("✅ Trigger received!")   # THIS STAYS THE SAME
    
    # ---------- ADD THIS PART ----------
    try:
        response = requests.get(MAKE_WEBHOOK_URL)  # Python calls Make.com
        print("✅ Make.com triggered, status code:", response.status_code)
    except Exception as e:
        print("❌ Failed to trigger Make.com:", e)
    # ---------- END OF NEW PART ----------
    
    return {"status": "ok", "message": "LIFT system triggered"}  # you can keep or change message
# -----------------------------

# -----------------------------
# Main block — KEEP THIS EXACTLY
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# -----------------------------
