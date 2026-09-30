# 🚗 Vehicle Fuel Economy Prediction

An end-to-end Machine Learning project that predicts a vehicle's **Highway Fuel Economy (MPG)** based on vehicle specifications such as manufacturer, model, engine characteristics, transmission, drivetrain, and fuel type.

## 🎯 Objective

The goal of this project is to build a regression model that can estimate a vehicle's **highway fuel economy (MPG)** from its available specifications.

## 📊 Dataset

* **Rows:** 33,442
* **Original Features:** 12
* **Target:** `highway_mpg`
* **Problem Type:** Regression

### Features Used

* Manufacturer
* Vehicle Model
* Vehicle Class
* Transmission
* Drivetrain
* Fuel Type
* Model Year
* Cylinders
* Engine Displacement

### Features Removed

* `id` → Unique identifier, not useful for prediction
* `city_mpg` → Excluded to avoid target leakage because it is another fuel-economy measurement strongly related to highway MPG

## 🔄 Machine Learning Workflow

```text
Data Collection
      ↓
Data Understanding
      ↓
Data Preprocessing
      ↓
Missing Value Handling
      ↓
Categorical Encoding
      ↓
Feature Transformation
      ↓
Feature Scaling
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Model Comparison
      ↓
Hyperparameter Tuning
      ↓
Feature Importance
      ↓
Final Model
      ↓
Streamlit Deployment
```

## ⚙️ Preprocessing

### Numerical Features

* Median imputation
* Power Transformation
* Standard Scaling

### Categorical Features

* Most-frequent imputation
* One-Hot Encoding
* `handle_unknown='ignore'`

## 🤖 Models Compared

The following regression models were evaluated:

1. Linear Regression
2. Random Forest Regressor
3. Gradient Boosting Regressor
4. XGBoost Regressor
5. LightGBM Regressor

Random Forest achieved the strongest test-set performance among the evaluated base models.

## 🎯 Final Model

The final model uses a **tuned Random Forest Regressor**.

Hyperparameters:

```text
n_estimators = 100
max_depth = 30
min_samples_split = 5
min_samples_leaf = 1
max_features = 1.0
```

## 📈 Final Test Performance

| Metric |     Score |
| ------ | --------: |
| MAE    | 0.699 MPG |
| RMSE   | 1.102 MPG |
| R²     |     0.969 |

The model explains approximately **96.9% of the variation in highway MPG on the test set**.

## 🔍 Feature Importance

The most influential features included:

* Engine Displacement
* Drivetrain
* Fuel Type
* Model Year
* Cylinders
* Transmission

Feature importance was obtained from the trained Random Forest model.

## 💾 Model Saving

The complete preprocessing pipeline and trained model were saved using **Joblib**:

```text
vehicle_fuel_economy_model.pkl
```

The pipeline contains both:

```text
Preprocessing
     ↓
Random Forest Model
```

This allows new vehicle data to go through the same preprocessing steps automatically during prediction.

## 🌐 Streamlit Application

A Streamlit web application was created where users can enter vehicle specifications and receive a predicted highway fuel economy value.

### Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* LightGBM
* Joblib
* Streamlit
* Git
* GitHub
* Git LFS

## 📁 Project Structure

```text
Vehicle Fuel Economy Prediction/
│
├── app.py
├── requirements.txt
├── README.md
└── vehicle_fuel_economy_model.pkl
```

## 🚀 Future Improvements

* Add model monitoring
* Improve feature engineering
* Experiment with advanced boosting models
* Add prediction confidence/range
* Improve Streamlit UI
* Deploy the application publicly

## 👨‍💻 Author

**Harish**

AI/ML | Data Science | Python | Machine Learning | GenAI
