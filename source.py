import json

# Function to load weather data from a local JSON file
def load_weather_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to classify temperature
def classify_temperature(temp):
    if temp >= 30:
        return "Hot"
    elif 20 <= temp < 30:
        return "Warm"
    else:
        return "Cold"

# Function to simulate API response and analyze data
def simulate_and_analyze(file_path):
    weather_data = load_weather_data(file_path)
    
    print("Analyzing Weather Data:")
    for entry in weather_data:
        city = entry['city']
        temperature = entry['temperature']
        condition = classify_temperature(temperature)
        
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C - Condition: {condition}")
        print("----------------------------------------")

# Main function to run the script
if __name__ == "__main__":
    # Path to the local JSON file
    file_path = 'weather_data.json'
    
    simulate_and_analyze(file_path)
