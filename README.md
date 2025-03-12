# Parkinson's Disease Prediction

## Overview
A machine learning model predicting Parkinson's disease based on vocal features.

## Features
- **Input:** This dataset composed of a range of biomedical voice measurements from 31 people, 23 with Parkinson's disease (PD). Each column in the table is a particular voice measure, and each row corresponds one of 195 voice recording from these individuals ("name" column).
- **Model:** Trained model (`best_model.pkl`).
- **Normalization:** Using `normalizer.pkl`.
- **Output:** Predicts **Healthy** or **Parkinson's Disease**.

## Installation
```bash
git clone <repository_url>
cd <repository_name>
python -m venv venv
venv\Scripts\activate
```

Ensure model files are in the `parkinson` directory:
- `parkinson/best_model.pkl`
- `parkinson/normalizer.pkl`

## Usage
Run the prediction script:
```bash
python test.py
```
Follow the prompts to input vocal feature values. The model will predict either **Healthy** or **Parkinson's Disease**.

## Requirements
- Python 3.10+
- Libraries: `joblib`, `pandas`,`scikit-learn`,`pandas`,`numpy`
  
## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
