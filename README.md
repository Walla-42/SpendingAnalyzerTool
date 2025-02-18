# Spending Analyzer Tool

<p align="center">
    <img src= "project_images/readme_img.jpeg" width=800 height= 200 alt="spending analyzer image">
</p>

<div align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/Forks-0-blue" alt="Forks">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Stars-0-yellow" alt="Stars">
  </a>
  <a href="https://github.com/Walla-42/SpendingAnalyzerTool/graphs/commit-activity">
    <img src="https://img.shields.io/github/commit-activity/y/Walla-42/SpendingAnalyzerTool" alt="Commits">
  </a>
</div>

## Introduction
The **Spending Analyzer Tool** is a budgeting program designed to help users track expenses, income, and generate insightful financial reports. Users can customize reports, set income sources, and analyze spending trends over different time frames. The program integrates an SQL database for secure data storage and uses a JSON configuration file to store user preferences.

## Creator
Developed by [Walla-42](https://github.com/YourGitHubUsername)

## To-Do List
- [ ] Finish report generation class
    - [ ] Define each of the statistics
    - [ ] Data needs to be selected and loaded when the user selects the timeframe for reports
    - [ ] Need to import Date time to check when reports are generated based on the user default settings. 
- [ ] Finish Expenses child class functions
    - [ ] add expense 
    - [ ] add income - incorporate default salary into this
    - [ ] Does it make sense to have all of these in a separate class? Review the setup
- [ ] Implement a graphical user interface (GUI)
    - [ ] Create window
    - [ ] integrate class functions into GUI interface for easy navigation
    - [ ] find a way to display reports within GUI and download them once generated


## Setup Instructions
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- SQLite 

### Installation
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/YourGitHubUsername/SpendingAnalyzer.git
   cd SpendingAnalyzer
   ```

2. **Install Dependencies:**
   ```sh
   pip install numpy matplotlib pandas sqlite3 json
   ```

3. **Run the Application:**
   ```sh
   python3 main.py
   ```

### Configuration
- Modify `user_preferences.json` to customize reports and income sources.
- Ensure the SQL database is correctly initialized before running reports.

## License
This project is licensed under the MIT License.



