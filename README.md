# Offline Weather API Response Simulator & Analyzer
by Anish K M

## Project Overview

This project is designed to simulate an API interaction for weather data analysis using a local JSON file. It includes a basic classification system that categorizes temperatures into "Hot", "Warm", or "Cold" based on predefined thresholds. The entire process is handled offline, making it a practical tool for understanding how to work with simulated API data without requiring internet access.

## Features

- **Offline Simulation**: No internet connection is needed; the tool works entirely offline by using locally stored JSON data.
- **Temperature Classification**: Classifies temperatures into categories such as "Hot", "Warm", or "Cold" using simple logic.
- **Simple and Lightweight**: Minimalistic code, focusing on basic functionality and easy understanding.
- **Flexible File Path**: Easily configurable file path to load JSON data from any location on your system.

## Steps

1. **Create Local JSON Data**
   - Prepare a JSON file containing simulated weather data. This file acts as if it's the response from a real weather API.
   - Example of the JSON format:
     ```json
     [
         {"city": "New York", "temperature": 30, "humidity": 80},
         {"city": "London", "temperature": 15, "humidity": 65},
         {"city": "Tokyo", "temperature": 25, "humidity": 70},
         {"city": "Delhi", "temperature": 40, "humidity": 20}
     ]
     ```

2. **Load Weather Data**
   - Use the provided Python script to read the JSON file. This simulates fetching data from an API.

3. **Classify Temperature**
   - Implement a basic classification logic to categorize temperatures:
     - "Hot" for temperatures 30°C and above.
     - "Warm" for temperatures between 20°C and 30°C.
     - "Cold" for temperatures below 20°C.

4. **Display Results**
   - The script outputs each city’s temperature and its classification to the console.

## How to Use

1. **Clone the Repository**
   - Download or clone the repository to your local machine:
     ```bash
     git clone https://github.com/yourusername/weather-analyzer.git
     cd weather-analyzer
     ```

2. **Create the JSON File**
   - Create a file named `test.json` in the specified directory with the example data provided above.

3. **Update File Path in Script**
   - Ensure that the `file_path` variable in `source.py` is set to the location of your `test.json` file. Example path:
     ```python
     file_path = r'C:\Users\saral\Kong\test.json'
     ```

4. **Run the Python Script**
   - Execute the Python script to load and analyze the data:
     ```bash
     python source.py
     ```

5. **View Results**
   - The script will print the classification of each city's temperature to the console.

## Outputs

- **Temperature Classification**: Console output showing each city's temperature and its classification.
  - Example output:
    ```
    Analyzing Weather Data:
    City: New York
    Temperature: 30°C - Condition: Hot
    ----------------------------------------
    City: London
    Temperature: 15°C - Condition: Cold
    ----------------------------------------
    City: Tokyo
    Temperature: 25°C - Condition: Warm
    ----------------------------------------
    City: Delhi
    Temperature: 40°C - Condition: Hot
    ----------------------------------------
    ```

- **Local JSON File**: Contains the simulated API data used for analysis.

## Applications

- **Educational Tool**: Helps understand how to process and analyze JSON data offline, which can be useful for learning purposes and basic data handling skills.
- **Prototype Development**: Serves as a starting point for developing more advanced data analysis tools and applications that do not rely on real-time internet connections.
- **Offline Data Testing**: Allows developers to test their data processing and classification logic without needing to connect to live APIs, useful for environments with limited internet access.

## Project Insights

This project demonstrates how to simulate API interactions and perform basic data classification offline. It provides a simple yet effective example of handling local data and classifying it using basic logic. This approach can be expanded to include more complex data and classifications as needed.

## Note

This project is a prototype meant for educational purposes and simulates real-world API data interactions. The classification logic is basic and can be enhanced for more sophisticated analyses.

## Links

- [Project Code on GitHub](https://github.com/yourusername/weather-analyzer)
- **JSON Data Example**: [test.json](./test.json)
