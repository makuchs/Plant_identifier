Flower Classification Using Deep Learning

This project implements a deep learning pipeline to classify flowers into various categories using a Convolutional Neural Network (CNN). 
It uses transfer learning with the MobileNetV2 model, fine-tuned for flower classification. 
Below is a detailed guide to the project's structure, data preprocessing, model training, evaluation, and predictions.

Table of Contents
1. Project Overview
2. Directory Structure
3. Data Preprocessing
4. Model Training
5. Model Evaluation
6. Predictions
7. Requirements
8. Usage
9. Output and Model Saving
10. Acknowledgments

1. Project Overview
	This project classifies flowers into the following categories:
		Daisy
		Dandelion
		Roses
		Sunflowers
		Tulips
	
	The deep learning pipeline includes:
		Data Augmentation: Enhancing the dataset with transformations like rotation, flipping, zooming, etc.
		Transfer Learning: Using the pre-trained MobileNetV2 model for feature extraction.
		Fine-Tuning: Customizing the model to improve accuracy on the flower dataset.
		Evaluation Metrics: Accuracy, precision, recall, and AUC.

2. Directory Structure
	archive/flower_photos: Folder containing the dataset organized by subfolders for each class.
	path/to/save_model: Directory where the trained model is saved.
	path/to/test_image_folder: Folder containing test images for predictions.

3. Data Preprocessing
	Dataset Splitting:
		The dataset is split into training (80%), validation (10%), and test (10%) sets using train_test_split with stratification.
	Image Augmentation:
		Techniques like rotation, width/height shifting, zoom, and brightness adjustments are applied using ImageDataGenerator.
	Normalization:
		All pixel values are scaled to the range [0, 1].
	
4. Model Training
	Model Architecture:
		The MobileNetV2 model (pre-trained on ImageNet) is used as the base model.
		Additional layers include Batch Normalization, Dense layers, and Dropout for regularization.
	Optimization:
		The Adamax optimizer is used with a learning rate of 0.0001.
	Early Stopping:
		Monitors validation loss to prevent overfitting.
	
5. Model Evaluation
	Metrics include:
		Accuracy
		Precision
		Recall
		AUC-ROC
	A confusion matrix and classification report are generated to evaluate performance.
	Calibration using temperature scaling is applied to improve confidence scores.

6. Predictions
	A function is implemented to make predictions on new flower images.
	Predictions are displayed with probabilities for all classes in descending order.
	Visualized predictions include the image with the predicted class and corresponding confidence.
	
7. Requirements
	Python Libraries
	tensorflow
	numpy
	pandas
	opencv-python
	matplotlib
	seaborn
	scikit-learn
	Pillow

8. Usage
	Prepare the Dataset:
		Ensure the dataset is organized into subfolders for each class under archive/flower_photos.
	Run Training:
		Execute the script to preprocess the data and train the model.
	Save Model:
		The trained model is saved as model.keras in the specified folder.
	Make Predictions:
		Place test images in the designated folder and run the prediction script.
		
9. Output and Model Saving
	The trained model is saved at the path: path/to/save_model/model.keras
	Model performance is visualized through plots of loss, accuracy, precision, recall, and AUC metrics.
	
10. Acknowledgments
	The primary dataset used in this project is sourced from the Flowers Dataset, available on Kaggle: 
	https://www.kaggle.com/datasets/rahmasleam/flowers-dataset. 
	Additionally, the dataset has been extended with free flower images collected from various sources on the internet to enhance 
	diversity and robustness. These supplemental images were carefully selected to align with the existing categories: 
	Daisy, Dandelion, Roses, Sunflowers, and Tulips.

	Special thanks to platforms providing free-to-use images, such as Pexels, and Pixabay, 
	for their contributions to the extended dataset.
			
	Pre-trained weights for MobileNetV2 are from the ImageNet dataset.
	
	This project is designed to demonstrate the effectiveness of transfer learning and data augmentation in image classification tasks.
