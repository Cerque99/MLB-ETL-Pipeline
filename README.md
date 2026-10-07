# MLB Daily Analytics Pipeline ⚾📊

**Video Demo:**: https://youtu.be/LW1WXNXjRwE

## 📌 Project Overview
This project is an automated ETL (Extract, Transform, Load) pipeline built in Python. It extracts raw daily game data from the public Major League Baseball (MLB) API, processes the results to calculate key statistics, and generates a structured, easy-to-read daily analytics report. 

This tool was developed as the Final Project for Harvard University's **CS50 Introduction to Programming with Python (CS50P)**. It bridges the gap between raw API data and actionable insights, showcasing core data analysis and software engineering skills.

## ⚙️ Features
* **Automated Data Extraction:** Uses the `requests` library to fetch real-time game schedules and scores from the official MLB Stats API.
* **Data Transformation & Cleaning:** Filters out unplayed or postponed games and restructures complex nested JSON data into a clean, flat format.
* **Statistical Computation:** Calculates daily metrics such as total runs scored, average runs per game, and identifies the highest-scoring matchups.
* **Report Generation:** Automatically exports the processed data and calculated metrics into a structured `.txt` report file (`mlb_report.txt`).
* **Robust Testing:** Includes a comprehensive suite of unit tests built with `pytest` to ensure data integrity and reliable function execution.

## 🛠️ Technologies & Tools
* **Language:** Python 3
* **Libraries:** `requests`, `pytest`, `json`, `sys`, `datetime`
* **Concepts Applied:** ETL processes, API consumption, Error Handling, File I/O, Unit Testing.

## 🚀 Installation and Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Cerque99/MLB-ETL-Pipeline.git](https://github.com/Cerque99/MLB-ETL-Pipeline.git)
   cd MLB-ETL-Pipeline
