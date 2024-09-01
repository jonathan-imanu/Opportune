# 🚀 Opportune 🚀

Opportune is a straightforward tool designed to help you stay updated with the latest software internships in Toronto. It does this by using Tom Quirk's [linkedin-api](https://github.com/tomquirk/linkedin-api) to fetch job listings from LinkedIn and then records them in a Google Sheet.

The tool tracks internships based on the following keywords and categorizes them into on-site, hybrid, and remote positions:

- Software Developer
- Software Engineer
- Data Engineer 
- Data Scientist
- Machine Learning Engineer

Every 2 hours, Opportune will update this [Google Sheet](https://docs.google.com/spreadsheets/d/1Zr8g0dNSZ3Ty1LCo_NL4CNLRcFSjKfUt7sM1STkyfzQ/edit?gid=0#gid=0) with the latest internship listings.

## 🕒 Automation

Originally, I planned to run Opportune automatically  using GitHub Actions. However, this approach (and potentially other remote solutions) leads to [CHALLENGE](https://github.com/tomquirk/linkedin-api?tab=readme-ov-file#i-keep-getting-a-challenge) exceptions from the LinkedIn API. This issue is likely due to the difference in IP addresses between the GitHub Actions server and your local machine where you access LinkedIn. To resolve this, Opportune is run on my local machine using cron. 

## Make your own spreadsheet

To use Opportune to update your own spreadsheet, you must set it up on your local machine. Follow these steps to set up your environment and start the script. Refer to [linkedin-api](https://github.com/tomquirk/linkedin-api) to make any ammendments to job search queries or any concerns regarding LinkedIn usage.

### Prerequisites

1. **Create a `.env` File**

   In the root directory of your project, create a `.env` file with the following content:

    ```bash
    LINKEDIN_USERNAME="your_linkedin_username"
    LINKEDIN_PASSWORD="your_linkedin_password"
    SHEET_NAME="your_sheet_name"
    SERVICE_JSON='contents of your_credentials_json'
    ```

2. **Google Sheets Credentials**

   You will need a valid [`credentials.json`](https://docs.gspread.org/en/v6.0.1/oauth2.html#for-bots-using-service-account) file for accessing Google Sheets. Ensure this file is placed in the root directory of your project.

3. **Modify the Code (if needed)**

   Depending on the format of your Google Sheet, you might need to adjust the code in `jobs.py` to ensure it works correctly with your sheet.

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
