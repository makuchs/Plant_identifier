# Plant Identifier

This project, "Automated Flower Species Identification Using Convolutional Neural Networks," was developed as part of the **Digital Image Processing** course at the **Wrocław University of Environmental and Life Sciences**. The objective is to create a scalable and modular application that classifies flower images into one of five predefined species using a deep learning model.

## Key Features
- **Species Identification**: Daisy, Dandelion, Rose, Sunflower, Tulip.
- **Transfer Learning**: Leveraging the MobileNetV2 architecture pre-trained on ImageNet for accurate and efficient classification.
- **Cloud Integration**: Utilizing Microsoft Azure and Amazon AWS for deployment and scalability.
- **User-Friendly Interface**: A simple web application for uploading images and displaying classification results.

## Folder Structure
### 1. **AWS**
The `AWS` folder contains files and configurations for the frontend hosted on an Amazon EC2 instance. 
- **Flask Application**: Handles user interactions, including uploading images and displaying results.
- **Frontend Code**: Includes `index.html`, `CSS`, and JavaScript for a dynamic user interface.

### 2. **Azure**
The `Azure` folder contains the backend API for image classification.
- **FastAPI Application**: A Python-based API that processes uploaded images and performs predictions using the TensorFlow model.
- **Model Integration**: Includes the pre-trained `Flower.keras` model.

### 3. **Model_generation**
The `Model_generation` folder contains code for training and fine-tuning the deep learning model.
- **Data Preparation**: Scripts for processing images and splitting datasets into training, validation, and testing sets.
- **Model Training**: Jupyter notebooks and Python scripts for training the MobileNetV2 model with data augmentation and regularization techniques.
- **Evaluation**: Tools for analyzing model performance and generating metrics.

## How It Works
1. **Model Training**: 
   - Images from multiple sources (Kaggle, Pixabay, Pexels) are preprocessed and augmented.
   - MobileNetV2 is fine-tuned on the dataset to achieve ~97.8% test accuracy.
   - The trained model is exported as `Flower.keras`.

2. **Azure Backend**:
   - A FastAPI-based service accepts images, preprocesses them to 224x224 pixels, and performs classification.
   - Results are returned as a JSON response, detailing class probabilities.

3. **AWS Frontend**:
   - A Flask web app allows users to upload images and interact with the classifier.
   - Images are sent to the Azure API, and results are displayed dynamically.

## Technologies Used
- **Python**: For backend processing and model training.
- **TensorFlow**: Deep learning framework for model development.
- **FastAPI**: Backend API hosted on Azure for processing and predictions.
- **Flask**: Frontend web application hosted on AWS.
- **Microsoft Azure**: Cloud platform for backend processing.
- **Amazon AWS**: Cloud platform for frontend hosting.
- **Image Processing Libraries**: OpenCV, PIL for image preprocessing.

## Results and Insights
- The model achieves **97.8% accuracy** on the test set.
- Incorporates techniques like data augmentation, dropout, and early stopping to avoid overfitting.
- Features a user-friendly interface for easy interaction with the classifier.

## License

This project is licensed under the [Apache License 2.0](LICENSE).  
The dataset is sourced from the Flowers Dataset and extended with additional images.  
See the [NOTICE](NOTICE) file for details.
