import os
from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route("/")
def home():
    return "Merhaba, uygulaman çalışıyor! 🚀"

@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    base64_str = data.get("base64")
    if not base64_str:
        return jsonify({"error": "base64 verisi yok"}), 400

    try:
        img_data = base64.b64decode(base64_str)
        with open("output.jpg", "wb") as f:
            f.write(img_data)
        return jsonify({"status": "success", "message": "Dosya kaydedildi"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
