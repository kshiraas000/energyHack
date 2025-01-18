import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor

# Load and preprocess the data
energy_data = pd.read_csv(r"C:\Users\mailt\onedrive\desktop\energyhack\energyhack\backend\data\energy_dataset.csv")

# Drop unnecessary columns
columns_to_drop = ['generation hydro pumped storage aggregated', 
                   'forecast wind offshore eday ahead',
                   'time',
                   'generation marine',
                   'generation geothermal',
                   'generation fossil peat',
                   'generation wind offshore',
                   'generation fossil oil shale',
                   'generation fossil coal-derived gas']

energy_data = energy_data.drop(columns_to_drop, axis=1)

# Remove rows with missing values
energy_data = energy_data.dropna()

# Prepare features and target
X = energy_data.drop(['price actual'], axis=1)
y = energy_data['price actual']

# Scale the features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize and train the XGBoost model
xgb_reg = XGBRegressor(random_state=42)
xgb_reg.fit(X_train, y_train)

# Make predictions
y_pred = xgb_reg.predict(X_test)

# Calculate and print metrics
train_accuracy = xgb_reg.score(X_train, y_train)
test_accuracy = xgb_reg.score(X_test, y_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Training Accuracy: {train_accuracy:.4f}")
print(f"Testing Accuracy: {test_accuracy:.4f}")
print(f"Mean Squared Error: {mse:.4f}")
print(f"R-squared score: {r2:.4f}")

# Feature importance
feature_importance = xgb_reg.feature_importances_
feature_names = X.columns
for importance, name in sorted(zip(feature_importance, feature_names), reverse=True):
    print(f"{name}: {importance:.4f}")
