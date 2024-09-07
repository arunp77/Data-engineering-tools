import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Load Data
df = pd.read_excel('supermarkt_sales.xlsx', skiprows=3)

# Preprocess Data
df_encoded = pd.get_dummies(df, columns=['Branch', 'City', 'Customer_type', 'Gender', 'Product line', 'Payment'], drop_first=True)

X = df_encoded[['Quantity', 'Unit price', 'gross income']]
y = df_encoded['Total']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Streamlit App

st.title('Supermarket Sales Dashboard')

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Select Analysis", ('Data Overview', 'Actual vs Predicted', 'Residual Plot', 'Residuals Distribution', 'Model Performance', 'Learning Curve'))

# 1. Data Overview
if option == 'Data Overview':
    st.header('Data Overview')
    st.write(df.head())
    st.write(df.describe())

    # Gender Distribution Plot
    st.subheader('Gender Distribution')
    fig, ax = plt.subplots()
    sns.countplot(x='Gender', data=df, ax=ax)
    st.pyplot(fig)

    # Sales by City
    st.subheader('Sales by City')
    city_sales = df.groupby('City')['Total'].sum()
    fig, ax = plt.subplots()
    city_sales.plot(kind='bar', ax=ax)
    ax.set_title('Total Sales by City')
    st.pyplot(fig)

# 2. Actual vs Predicted Plot
if option == 'Actual vs Predicted':
    st.header('Actual vs Predicted Sales')
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred)
    ax.set_xlabel('Actual Total Sales')
    ax.set_ylabel('Predicted Total Sales')
    ax.set_title('Actual vs Predicted Sales')
    st.pyplot(fig)

# 3. Residual Plot
if option == 'Residual Plot':
    st.header('Residual Plot')
    residuals = y_test - y_pred
    fig, ax = plt.subplots()
    ax.scatter(y_pred, residuals)
    ax.axhline(0, color='red', linestyle='--')
    ax.set_xlabel('Predicted Total Sales')
    ax.set_ylabel('Residuals')
    ax.set_title('Residual Plot')
    st.pyplot(fig)

# 4. Residual Distribution
if option == 'Residuals Distribution':
    st.header('Distribution of Residuals')
    residuals = y_test - y_pred
    fig, ax = plt.subplots()
    sns.histplot(residuals, kde=True, ax=ax)
    ax.set_title('Distribution of Residuals')
    st.pyplot(fig)

# 5. Model Performance
if option == 'Model Performance':
    st.header('Model Performance Metrics')
    r_squared = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    st.write(f"**R-squared:** {r_squared:.3f}")
    st.write(f"**Mean Squared Error (MSE):** {mse:.3f}")

    # Bar plot for R-squared and MSE
    metrics = {'R-squared': r_squared, 'MSE': mse}
    fig, ax = plt.subplots()
    ax.bar(metrics.keys(), metrics.values(), color=['blue', 'green'])
    ax.set_title('Model Performance Metrics')
    st.pyplot(fig)

# 6. Learning Curve (optional if you've implemented it)
if option == 'Learning Curve':
    from sklearn.model_selection import learning_curve

    st.header('Learning Curve')
    train_sizes, train_scores, test_scores = learning_curve(model, X, y, cv=5, scoring='r2', n_jobs=-1)

    train_scores_mean = train_scores.mean(axis=1)
    test_scores_mean = test_scores.mean(axis=1)

    fig, ax = plt.subplots()
    ax.plot(train_sizes, train_scores_mean, label='Training Score')
    ax.plot(train_sizes, test_scores_mean, label='Cross-Validation Score')
    ax.set_xlabel('Training Size')
    ax.set_ylabel('R-squared Score')
    ax.set_title('Learning Curve')
    ax.legend()
    st.pyplot(fig)

