from flask import Flask, request, jsonify
import os
from ultralytics import YOLO
import cv2

model = YOLO("Server/best.pt")

app = Flask(__name__)

@app.route('/analyze-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join("Files", filename))
    model(source=f"D:/Projects/Python/Elktrify/Elktrify/Files/{filename}", conf=0.4, show=True, save=True, project="D:/Projects/Python/Elktrify/Elktrify/Outputs", name=f"{filename}")
    return jsonify({"Message": "File succesfully uploaded and analyzed"})

@app.route('/generate-plan', methods=['POST'])
def generate_plan():
    data = request.get_json()
    plan = {"suggestion": "Use washing machine during off-peak hours"}
    return jsonify({"plan": plan})

if __name__ == "__main__":
    app.run(debug=True)