import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Function to fetch data from the API
def fetch_api_data():
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}"  # Example API URL
    response = requests.get(url)  # Make a GET request to the API
    data = response.json()  # Parse the JSON response
    return data

# Function to display the fetched data
def display_data(data):
    df = pd.DataFrame([data])  # Convert the data to a DataFrame
    print("API Data:")  # Print a header
    print(df.head())  # Display the first few rows of the DataFrame

# Function to analyze the data and provide summary statistics
def analyze_data(data):
    df = pd.DataFrame([data])  # Convert the data to a DataFrame
    print("\nSummary Statistics:")  # Print a header
    print(df.describe())  # Display summary statistics of the DataFrame

# Function to predict future API usage using a linear regression model
def predict_usage(data):
    df = pd.DataFrame([data])  # Convert the data to a DataFrame
    X = np.array(df.index).reshape(-1, 1)  # Reshape the index to be used as features
    y = df['usage'].values  # Extract the 'usage' column as the target variable
    model = LinearRegression()  # Create a Linear Regression model
    model.fit(X, y)  # Fit the model to the data
    future = np.array([[len(df) + i] for i in range(1, 6)])  # Create future indices for prediction
    predictions = model.predict(future)  # Predict future usage
    print("\nPredicted Usage for Next 5 Days:")  # Print a header
    print(predictions)  # Display the predictions

# Main function to run the script
if __name__ == "__main__":
    data = fetch_api_data()  # Fetch the API data
    display_data(data)  # Display the fetched data
    analyze_data(data)  # Analyze the data
    predict_usage(data)  # Predict future usage
