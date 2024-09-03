import os
import logging
from linkedin_api import Linkedin
from dotenv import load_dotenv
import pandas as pd
import gspread
import json

from utils import get_row_number, update_row_number
from jobs import format_jobs


# Configure logging

logger = logging.getLogger("Opportune")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs.txt")
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%m/%d/%H:%M')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.info("Process Started")

load_dotenv()

linkedin_username = os.getenv("LINKEDIN_USERNAME")
linkedin_password = os.getenv("LINKEDIN_PASSWORD")
credentials_path = os.getenv("SERVICE_JSON_PATH")
# credentials = json.loads(os.getenv("SERVICE_JSON"))
tracker_sheet = os.getenv("SHEET_NAME")
current_row_number = get_row_number()

# Get latest internships in Toronto from LinkedIn

linkedin_scraper = Linkedin(linkedin_username, linkedin_password)
logger.info("Logged in to LinkedIn")

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

# Upload to Google Sheets

total = len(to_upload)
logger.info("Fetched %d jobs", total)

end = current_row_number + total
cell_range = f"A{current_row_number}:G{end}"

gc = gspread.service_account(filename=credentials_path)
# gc = gspread.service_account_from_dict(credentials)

sh = gc.open(tracker_sheet)
worksheet = sh.worksheet('Tracker')  
worksheet.update(range_name=cell_range, values=to_upload)

# Update .env file for next run

update_row_number(end)
logger.info("Updated row number to %d", end)
# If working with a local .env file, you can update_env_variable("CURRENT_ROW_NUMBER", str(end + 1)) from utils.py