# Plant Identifier

This project was developed as part of the course **Digital Image Processing** at the Wrocław University of Environmental and Life Sciences. The goal of the project is to create a web-based plant identification system that allows users to upload an image of a flower and receive its classification into one of five predefined classes. The system is implemented using two cloud platforms, **Azure** and **AWS**, and consists of three main components, each organized into separate folders.

## Folder Structure

### 1. **AWS**
The `AWS` folder contains the necessary files and configurations for hosting the web interface of the application on an Amazon EC2 instance. The Flask-based application provides users with a friendly interface to upload flower images and view classification results. It includes:
- The `app.py` file, which defines the Flask application that handles user interaction.
- HTML and CSS files for the web interface, enabling image uploads and displaying predictions.
- Deployment scripts and instructions for setting up the AWS EC2 instance to run the Flask application.

### 2. **Azure**
The `Azure` folder contains all the components needed to deploy the classification model on Microsoft Azure. This part of the system handles image processing and classification. It includes:
- A **FastAPI**-based API that accepts image uploads, processes them, and runs predictions using a pre-trained model.
- Scripts and configurations for deploying the API on Azure App Service.
- Documentation on how to connect the Azure API with the AWS front end for seamless communication.

### 3. **Model_generation**
The `Model_generation` folder contains the code and resources used to train the classification model. This folder includes:
- Jupyter notebooks for preprocessing image datasets and training a TensorFlow-based model.
- Scripts for model evaluation and saving the trained model in a format compatible with the Azure API.
- Additional documentation and instructions for retraining or updating the model with new data.

## How It Works
1. **Model Training**: The TensorFlow model is trained on a dataset of flower images and saved in the `Model_generation` folder.
2. **Azure Deployment**: The trained model is deployed on Azure using a FastAPI-based API that handles image classification. Users can send images to the API, which returns the classification results in JSON format.
3. **AWS Deployment**: The user interface, hosted on AWS, allows users to upload images and receive classification results. The AWS front end communicates with the Azure API to retrieve predictions.

## Technologies Used
- **Python**: The primary programming language for all components.
- **FastAPI**: Used for building the Azure-based classification API.
- **Flask**: Used for the AWS web application interface.
- **TensorFlow**: For training and running the image classification model.
- **Microsoft Azure**: Hosts the FastAPI classification API.
- **Amazon AWS**: Hosts the Flask-based web application.

This project demonstrates the integration of cloud services to create a scalable and modular solution for image classification, with the potential for further extensions and enhancements.
