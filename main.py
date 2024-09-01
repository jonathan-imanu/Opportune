import os
import logging
from linkedin_api import Linkedin
from dotenv import load_dotenv
import pandas as pd
import gspread

from utils import update_env_variable
from jobs import format_jobs

load_dotenv()

linkedin_username = os.getenv("LINKEDIN_USERNAME")
linkedin_password = os.getenv("LINKEDIN_PASSWORD")
service_path = os.getenv("SERVICE_PATH")
tracker_sheet = os.getenv("SHEET_NAME")
current_row_number = int(os.getenv("CURRENT_ROW_NUMBER"))

linkedin_scraper = Linkedin(linkedin_username, linkedin_password)

# Get latest internships in Toronto from LinkedIn

keywords = ["Software Developer", "Software Engineer", "Data Engineer", "Data Scientist", "Machine Learning Engineer"]
to_upload = []
urns = set() # Each urn is unqiue so we can use this to check for duplicates

for keyword in keywords:
    unformatted_onsite_jobs = linkedin_scraper.search_jobs(keywords=keyword,
                        location_name="Toronto",
                        experience=["1"],
                        remote=["1"],
                        listed_at=7200)

    unformatted_remote_jobs = linkedin_scraper.search_jobs(keywords=keyword,
                        location_name="Toronto",
                        experience=["1"],
                        remote=["2"],
                        listed_at=7200)

    unformatted_hybrid_jobs = linkedin_scraper.search_jobs(keywords=keyword,
                        location_name="Toronto",
                        experience=["1"],
                        remote=["3"],
                        listed_at=7200)

    formatted_onsite_jobs = format_jobs(unformatted_onsite_jobs, keyword, 'On-site', urns)
    formatted_remote_jobs = format_jobs(unformatted_remote_jobs, keyword, 'Remote', urns)
    formatted_hybird_jobs = format_jobs(unformatted_hybrid_jobs, keyword, 'Hybrid', urns)

    to_upload.extend(formatted_onsite_jobs)
    to_upload.extend(formatted_remote_jobs) 
    to_upload.extend(formatted_hybird_jobs)

total = len(to_upload)
new_start = current_row_number + total

# Upload to Google Sheets

gc = gspread.service_account(filename=service_path)
sh = gc.open(tracker_sheet)
worksheet = sh.worksheet('Tracker')  


# Update .env file for next run

os.environ["CURRENT_ROW_NUMBER"] = str(new_start)
# Use if working with a local .env file: update_env_variable("CURRENT_ROW_NUMBER", str(new_start))