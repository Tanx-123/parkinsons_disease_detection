import joblib
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

# Load the saved model and normalizer
model = joblib.load('parkinson\\best_model.pkl')
scaler = joblib.load('parkinson\\normalizer.pkl')

# Selected features
selected_features = ['MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
                     'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'PPE']

# Get input from the user for the selected features
user_input = {}
for feature in selected_features:
    value = float(input(f"Enter the value for '{feature}': "))
    user_input[feature] = value

# Create a DataFrame with the user input
user_df = pd.DataFrame([user_input])

# Normalize the user input using the saved normalizer
user_scaled = scaler.transform(user_df)

# Make a prediction using the loaded model
prediction = model.predict(user_scaled)

# Print the result
if prediction[0] == 0:
    print("Status: Healthy")
else:
    print("Status: Parkinson's Disease")