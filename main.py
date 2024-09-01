import os
from linkedin_api import Linkedin
from dotenv import load_dotenv
import pandas as pd
import gspread


load_dotenv()

linkedin_username = os.getenv("LINKEDIN_USERNAME")
linkedin_password = os.getenv("LINKEDIN_PASSWORD")
service_path = os.getenv("SERVICE_PATH")
tracker_sheet = os.getenv("SHEET_NAME")

linkedin_scraper = Linkedin(linkedin_username, linkedin_password)

# Get latest software jobs in Ontario 
jobs = linkedin_scraper.search_jobs(keywords="Software",
                     location_name="Ontario, Canada",
                     experience=["1"],
                     remote=["1", "2", "3"],
                     listed_at=720000)


gc = gspread.service_account(filename=service_path)
sh = gc.open(tracker_sheet)

print(sh.sheet1.get('A1'))

