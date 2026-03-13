📌 Project Objective
Automate the testing of the GUVI web application by simulating user actions and validating key UI functionalities — including page behavior, accessibility of critical elements, navigation flows, and login/logout logic.
________________________________________
📁 Project Structure
Guvi-final-project-1/
│
├── pages/                  # Page Object Model classes
│   ├── BasePage.py         # Base class with common methods (wait, click, etc.)
│   ├── HomePage.py         # Home page interactions
│   ├── LoginPage.py        # Login page interactions
│   └── DashboardPage.py    # Dashboard page interactions
│
├── tests/                  # Test cases
│   └── guvi_test.py        # Main test file
│
├── utils/                  # Utility/helper functions
│
├── reports/                # HTML test execution reports
│
├── conftest.py             # Pytest fixtures and browser setup
├── guvi.ini                # Pytest configuration
├── main.py                 # Entry point
├── node.py                 # Node utilities
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
________________________________________
✅ Test Cases Covered
#	Scenario	Expected Result
TC01	Verify URL https://www.guvi.in is valid	Page loads without errors
TC02	Verify webpage title	Title matches "GUVI | learn to code in your native language"
TC03	Verify Login button visibility & clickability	Login button visible and navigates to login page
TC04	Verify Sign-up button visibility & clickability	Sign-up button visible and redirects to /register/
TC05	Verify navigation via Sign-up button	Redirected URL should be https://www.guvi.in/register/
TC06	Login with valid credentials	User redirected to profile dashboard
TC07	Login with invalid credentials	Login fails with appropriate error message
TC08	Verify menu items (Courses, LIVE Classes, Practice)	All menu items visible and accessible
TC09	Validate Dobby GUVI assistant presence	Dobby assistant widget displayed on page
TC10	Validate logout functionality	User logged out and redirected to homepage
________________________________________
🛠️ Tech Stack
•	Language: Python
•	Framework: Playwright
•	Test Runner: Pytest
•	Reporting: pytest-html
•	Design Pattern: Page Object Model (POM)
________________________________________
⚙️ Setup & Installation
1. Clone the repository
git clone https://github.com/vkarthikvenkatachalam-dev/Guvi-final-project-1.git
cd Guvi-final-project-1
2. Create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
playwright install
________________________________________
▶️ Running Tests
Run all tests
pytest tests/guvi_test.py
Run with HTML report
pytest tests/guvi_test.py --html=reports/report.html --self-contained-html
Run on a specific browser
pytest tests/guvi_test.py --browser chromium
pytest tests/guvi_test.py --browser firefox
pytest tests/guvi_test.py --browser webkit
________________________________________
📊 Test Reports
HTML reports are generated in the reports/ folder after each test run.
To generate:
pytest tests/guvi_test.py --html=reports/report.html --self-contained-html
________________________________________
🌐 Cross-Browser Support
Tests are validated across:
•	✅ Chrome (Chromium)
•	✅ Firefox
•	✅ Safari (WebKit)
•	✅ Microsoft Edge
________________________________________
📋 Requirements
playwright
pytest
pytest-html
Install all via:
pip install -r requirements.txt
________________________________________
📝 Notes
•	OOP principles are followed throughout the codebase using the Page Object Model
•	Exception handling is implemented to ensure test resilience
•	Browser is properly closed after all test cases are executed
•	Both positive and negative test scenarios are covered
________________________________________
👤 Author
Karthik V
GitHub: @vkarthikvenkatachalam-dev

