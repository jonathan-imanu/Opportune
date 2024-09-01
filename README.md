# 🚀 Opportune 🚀

Opportune is a simple project that fetches the latest software internships in Toronto from LinkedIn using an Tom Quirk's [linkedin-api](https://github.com/tomquirk/linkedin-api) and records them in a Google Sheet. Currently the following keywords are tracked across on-site, hybrid and remote internship postings:

- Software Developer
- Software Engineer
- Data Engineer 
- Data Scientist
- Machine Learning Engineer

## 🕒 Automation

Opportune runs automatically every 2 hours using GitHub Actions. It updates this [Google Sheet](https://docs.google.com/spreadsheets/d/1Zr8g0dNSZ3Ty1LCo_NL4CNLRcFSjKfUt7sM1STkyfzQ/edit?gid=0#gid=0) with the latest internship listings.

## Make your own spreadsheet

To use Opportune to update your own spreadsheet, you must set it up on your local machine. Follow these steps to set up your environment and start the script. Refer to [linkedin-api](https://github.com/tomquirk/linkedin-api) to make any ammendments to job search queries or any concerns regarding LinkedIn usage.

### Prerequisites

Ensure you have the following in place:

1. **.env File**: Create a `.env` file in the root directory with your LinkedIn credentials:

    ```bash
    LINKEDIN_USERNAME="your_linkedin_username"
    LINKEDIN_PASSWORD="your_linkedin_password"
    SHEET_NAME="your_sheet_name"
    SERVICE_JSON='contents of credentials.json'
    ```

**You need a valid [`credentials.json`](https://docs.gspread.org/en/v6.0.1/oauth2.html#for-bots-using-service-account) file for Google Sheets access.**

### Getting Started

1. **Set Up a Virtual Environment**: Create and activate a virtual environment to manage dependencies.

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. **Install Dependencies**: Install the required Python packages.

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Script**: Execute the script to start fetching and uploading job listings.

    ```bash
    python -u "path/to/main.py"
    ```

### Sample bash scripts

To automate the script execution, sample Bash scripts are provided that include cron commands. You can use these scripts to schedule the script to run at regular intervals. 
