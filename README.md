# MLB Daily Analytics Pipeline

#### Video Demo: https://youtu.be/LW1WXNXjRwE

#### Description:

This project automatically pulls data for Major League Baseball (MLB) and analyzes it in a structured format. It creates an introductory data pipeline. The script uses the public MLB API to retrieve data for a given date, filters the data, processes it and creates an analysis report.

The primary goal of this project is to apply modular programming concepts, create and manage complex data structures (JSON), and make HTTP requests to set the foundation for data analysis and data engineering projects.

## Project Structure

The main files for this project are as follows:

*  "project.py": This file contains the core of this project and consists of the 'main' function and is broken into four modular functions that separate the business logic:

   1. 'get_mlb_data(date)': Manages the HTTP connection using the 'requests' library and returns the raw JSON.

   2. 'filter_and_process_games(json_data)': Filters data, processes it, and extracts relevant information.

   3. 'calculate_matchday_metrics(games)': Performs statistical calculations on the processed data to retrieve relevant aggregations and detect the highest scoring game.

   4. 'export_summary_report(date, games, analysis)': Renders a '.txt' file with a structured summary of the analysis for a given date.

*  "test_project.py": Contains a unit testing framework built to be executed using 'pytest'.

*  "requirements.txt": A config file that lists the project's external dependencies.

## How to Run the Project

1.  Install dependencies: Make sure to install the required libraries by running the following command in your terminal:
    ```bash
    pip install -r requirements.txt
    ```

2.  Run the program: Launch the main Python script:
    ```bash
    python project.py
    ```

3.  Enter the date: The terminal will prompt you to enter a specific date using the YYYY-MM-DD format (for example 2024-07-01).

4.  View the results: Once the data is processed, open the 'reporte_mlb.txt' file generated in your directory to review the analytics for the date requested.

5.  Run tests (Optional): To verify that all the logic works without errors, run the unit test with:
    ```bash
    pytest test_project.py
    ```

## 📬 Contact & Credentials
* **LinkedIn:** [www.linkedin.com/in/francisco-cerqueiras-dieguez-62b607422]
* **CS50 Certificate:** [https://cs50.harvard.edu/certificates/211ad164-b004-47ff-af44-35bc1f08f8e1]







