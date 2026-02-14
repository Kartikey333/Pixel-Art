# 🎨 Pixel Mosaic Generator

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-orange)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> Transform high-resolution images into artistic pixel mosaics using Computer Vision and Machine Learning.

---

## ✨ Overview

**Pixel Mosaic Generator** is a Python-based image processing project that recreates images as mosaics by replacing pixel blocks with visually similar image tiles.

The system preserves the original structure while generating a creative, pixel-art reinterpretation.

---

## 🧠 How It Works

### 1️⃣ Image Preprocessing
- Resize input image  
- Divide into fixed-size blocks  
- Normalize pixel values  

### 2️⃣ Feature Extraction
- Extract RGB color vectors  
- Apply **K-Means clustering** to determine dominant colors  

### 3️⃣ Tile Matching
- Compute Euclidean distance between block color and tile dataset  
- Select closest matching tile  

### 4️⃣ Mosaic Reconstruction
- Replace each block with the best matching tile  
- Merge all tiles to form final mosaic  

---

## 🚀 Features

- 📸 High-resolution image support  
- 🎛 Adjustable block size (pixelation level)  
- 🎨 Dominant color extraction (K-Means)  
- 🔍 Similarity matching via color distance  
- ⚡ Optimized NumPy-based computations  
- 🧩 Custom tile dataset support  

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core implementation |
| NumPy | Efficient array operations |
| Pandas | Data handling |
| OpenCV | Image processing |
| Pillow | Image manipulation |
| Scikit-learn | Clustering & similarity |

---

## 📂 Project Structure

Pixel-Mosaic-Generator/
│
├── dataset/ # Tile images
├── input/ # Input images
├── output/ # Generated mosaics
├── src/
│ ├── preprocessing.py
│ ├── feature_extraction.py
│ ├── tile_matching.py
│ └── main.py
│
└── README.md
