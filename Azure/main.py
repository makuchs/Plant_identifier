from fastapi import FastAPI, File, UploadFile 
import tensorflow as tf
import numpy as np
from PIL import Image
import os
from tensorflow.keras.models import load_model

app = FastAPI()

model = load_model(os.path.join(os.path.dirname(__file__), "model", "Flower.keras"))

class_labels = ['Stokrotka', 'Mniszek lekarski', 'Róża', 'Słonecznik', 'Tulipan']

def preprocess_image(image_data, target_size=(224, 224)):
    image = Image.open(image_data)
    image = image.convert("RGB")
    resized_image = image.resize(target_size)
    processed_image = np.array(resized_image) / 255.0
    processed_image = np.expand_dims(processed_image, axis=0).astype(np.float32)
    return processed_image

@app.get("/")
async def read_root():
    return {"message": "Hello, Azure!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        processed_image = preprocess_image(file.file)
        
        predictions = model.predict(processed_image)
        
        predicted_class = np.argmax(predictions, axis=1)

        sorted_indices = np.argsort(predictions[0])[::-1]
        sorted_predictions = [
            {'class': class_labels[i], 'confidence': float(predictions[0][i] * 100)}
            for i in sorted_indices
        ]

        result = {
            'predicted_class': class_labels[predicted_class[0]],
            'sorted_predictions': sorted_predictions,
        }

    except Exception as e:
        result = {'error': str(e)}

    return result