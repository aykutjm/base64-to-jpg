from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    base64_str = data.get("base64")
    if not base64_str:
        return jsonify({"error": "base64 verisi yok"}), 400

    img_data = base64.b64decode(base64_str)
    with open("output.jpg", "wb") as f:
        f.write(img_data)

    return jsonify({"status": "success", "message": "Dosya kaydedildi"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
