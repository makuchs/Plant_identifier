# 🌸 Flower Classification Using Deep Learning 🌼

This project implements a deep learning pipeline to classify flowers into various categories using a Convolutional Neural Network (CNN).  
It leverages transfer learning with the **MobileNetV2** model, fine-tuned for flower classification.  

Below is a detailed guide to the project's structure, data preprocessing, model training, evaluation, and predictions.

---

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Directory Structure](#directory-structure)
3. [Data Preprocessing](#data-preprocessing)
4. [Model Training](#model-training)
5. [Model Evaluation](#model-evaluation)
6. [Predictions](#predictions)
7. [Requirements](#requirements)
8. [Usage](#usage)
9. [Output and Model Saving](#output-and-model-saving)
10. [Acknowledgments](#acknowledgments)

---

## 1. 📌 Project Overview

This project classifies flowers into the following categories:
- 🌼 **Daisy**
- 🌻 **Dandelion**
- 🌹 **Roses**
- 🌞 **Sunflowers**
- 🌷 **Tulips**

### Key Features:
- **Data Augmentation**: Enhancing the dataset with transformations like rotation, flipping, zooming, etc.
- **Transfer Learning**: Using the pre-trained **MobileNetV2** model for feature extraction.
- **Fine-Tuning**: Customizing the model to improve accuracy on the flower dataset.
- **Evaluation Metrics**: Accuracy, precision, recall, and AUC-ROC.

---

## 2. 📁 Directory Structure

```plaintext
archive/flower_photos    # Folder containing the dataset organized by subfolders for each class.
path/to/save_model        # Directory where the trained model is saved.
path/to/test_image_folder # Folder containing test images for predictions.
