Selenium Login Test

A simple automated login test for the Accelerate web app using Python and Selenium. It opens the login page in Firefox, fills in your credentials, clicks the login button, and checks whether you land on the Dashboard.


What You Need Before Starting


Python 3.8 or higher
Firefox browser installed
Git (optional, just to clone the repo)



Setup

1. Clone the repository

bashgit clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Create a virtual environment

bashpython -m venv .venv

Activate it:


Windows: .venv\Scripts\activate
Mac/Linux: source .venv/bin/activate


3. Install dependencies

bashpip install selenium

4. Download GeckoDriver

GeckoDriver is what lets Selenium control Firefox.


Go to https://github.com/mozilla/geckodriver/releases
Download the version that matches your operating system
Extract it and place geckodriver.exe (Windows) or geckodriver (Mac/Linux) in the project folder



Update the GeckoDriver path if yours is in a different location:

pythonservice = Service(executable_path=r"C:\path\to\geckodriver.exe")


Running the Test

Make sure your virtual environment is active, then run:

bashpython logintestemail.py


Project Structure

selenium-testing-project/
│
├── logintestemail.py       # The main test script
├── geckodriver.exe     # Firefox WebDriver (not committed to Git)
├── .venv/              # Virtual environment (not committed to Git)
└── README.md           # This file





This test was built for the staging environment at https://staging--accelerate-02-web.netlify.app
The script does not store or log your credentials anywhere
Do not commit your real email and password to GitHub — consider using environment variables if sharing this publicly
