# TrendPulse Project 🚀

## 📌 Overview

TrendPulse is a data pipeline project that collects and analyzes trending stories from the HackerNews API.
The project is divided into 4 tasks: data collection, cleaning, analysis, and visualization.

---

## 🧩 Tasks

### 🔹 Task 1: Data Collection

* Fetches top trending stories from HackerNews API
* Categorizes stories into:

  * Technology
  * World News
  * Sports
  * Science
  * Entertainment
* Saves data in JSON format

### 🔹 Task 2: Data Cleaning

* Loads JSON data
* Cleans missing/invalid values
* Converts data into CSV format

### 🔹 Task 3: Data Analysis

* Uses Pandas for analysis
* Finds:

  * Total stories
  * Category distribution
  * Top stories by score
  * Average comments

### 🔹 Task 4: Data Visualization

* Visualizes data using graphs
* Shows category distribution

---

## 🛠️ Technologies Used

* Python
* Requests
* JSON
* Pandas
* Matplotlib

---

## 📂 Project Structure

trendpulse-meghana/
│
├── task1_data_collection.py
├── task2_data_cleaning.py
├── task3_analysis.py
├── task4_visualization.py
│
├── data/
│   ├── trends_YYYYMMDD.json
│   └── cleaned_trends.csv

---

## ▶️ How to Run

1. Run Task 1:
   python task1_data_collection.py

2. Run Task 2:
   python task2_data_cleaning.py

3. Run Task 3:
   python task3_analysis.py

4. Run Task 4:
   python task4_visualization.py

---

## 📊 Output

* JSON file with trending stories
* Cleaned CSV file
* Analysis results in terminal
* Graph visualization

---

## 👩‍💻 Author

Meghana Samudrala
