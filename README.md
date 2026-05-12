# 🧠 PCOS Detection using CNN (Ultrasound Images)

## 📌 Project Overview

This project uses Convolutional Neural Networks (CNN) to detect Polycystic Ovary Syndrome (PCOS) from ultrasound images.

The model classifies images into:

* ✅ PCOS Detected
* ❌ No PCOS Detected

This demonstrates the use of Deep Learning in healthcare imaging.

---

## 🎯 Objectives

* Build an image classification model using CNN
* Detect PCOS from ultrasound images
* Improve performance using Transfer Learning (MobileNetV2)
* Deploy using Streamlit

---

## 🗂️ Project Structure

PCOS_CNN_Project/

│
├── dataset/
│   ├── train/
│   │   ├── pcos/
│   │   └── no_pcos/
│   ├── test/
│   │   ├── pcos/
│   │   └── no_pcos/

│
├── model/
│   └── cnn_model.h5

│
├── train_cnn.ipynb
├── app.py
├── requirements.txt
└── README.md

---

## 📊 Dataset

* Source: Kaggle (PCOS Ultrasound Dataset)
* Classes:

  * pcos → PCOS present
  * no_pcos → PCOS absent

Note: Dataset size is small, so results may vary.

---

## 🧠 Model Architecture

### Base Model

* MobileNetV2 (Pretrained)

### Custom Layers

* GlobalAveragePooling2D
* Dense Layer (64 neurons, ReLU)
* Dropout (0.5)
* Output Layer (Sigmoid)

---

## ⚙️ Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Pillow
* Streamlit

---

## 🚀 How to Run

### 1. Install Dependencies

pip install -r requirements.txt

### 2. Train Model

Run train_cnn.ipynb

### 3. Run App

streamlit run app.py

---

## 💻 Web App Features

* Upload ultrasound image
* Real-time prediction
* Confidence percentage
* Clean UI

---

## 📈 Sample Output

* No PCOS Detected (92%)
* PCOS Detected (78%)

---

## ⚠️ Disclaimer

This project is for educational purposes only and not a medical diagnosis tool.

---

## 🚧 Limitations

* Small dataset
* Possible overfitting
* Not clinically validated

---

## 🔮 Future Improvements

* Use larger dataset
* Apply advanced augmentation
* Use Grad-CAM for explainability
* Deploy on cloud

---

## 💼 Resume Line

Developed a CNN-based medical image classifier using transfer learning (MobileNetV2) to detect PCOS from ultrasound images and deployed it using Streamlit.
