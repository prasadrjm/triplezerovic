# Selenium-Pytest Automation Framework

This project is an automated testing framework using Selenium WebDriver with Pytest in Python. It follows the Page Object Model (POM) design pattern for maintainability and scalability.

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver compatible with your Chrome version

### Installation

1. Create a virtual environment 
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

2.Install dependencies:
pip install -r requirements.txt

3.Running the Tests
pytest tests/ --html=report.html

   3.1  Run a specific test module:
        pytest tests/test_login.py


## 🧱 4. Design Details

### 🎯 Objective

Develop a robust, maintainable, and scalable test automation framework for web applications using Selenium WebDriver and Pytest in Python.

### 🧩 Design Patterns and Practices

- **Page Object Model (POM):** Encapsulates page elements and actions within classes, promoting reusability and readability.
- **Pytest Fixtures:** Manages setup and teardown processes, such as initializing and quitting the WebDriver.
- **Modular Test Structure:** Separates test cases, page objects, and configurations for better organization.
- **Explicit Waits:** Utilizes Selenium's WebDriverWait to handle dynamic web elements effectively.
- **Test Reporting:** Integrates `pytest-html` to generate detailed HTML reports after test execution.

### 🔧 Technologies Used

- **Python 3.7+**
- **Selenium WebDriver**
- **Pytest**
- **pytest-html** for reporting

### 📈 Benefits

- **Maintainability:** Changes in the UI require updates only in the corresponding page object classes.
- **Scalability:** New test cases can be added with minimal effort due to the modular structure.
- **Readability:** Clear separation of concerns makes the codebase easier to understand and manage.
- **Reusability:** Common functionalities are encapsulated within page objects and fixtures, reducing code duplication.


