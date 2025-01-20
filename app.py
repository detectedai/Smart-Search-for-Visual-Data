from flask import Flask, request, jsonify
import os
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the AI-Powered Smart Search for Visual Data!"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    # Save the uploaded file temporarily
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)

    # Process the image (convert to grayscale)
    image = cv2.imread(file_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_file_path = os.path.join("uploads", "gray_" + file.filename)
    cv2.imwrite(processed_file_path, gray_image)

    return jsonify({"message": "File uploaded and processed successfully!", "processed_file": processed_file_path})

if __name__ == "__main__":
    app.run(debug=True)
