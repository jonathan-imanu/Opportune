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

unformatted_onsite_jobs = linkedin_scraper.search_jobs(keywords="Software",
                     location_name="Canada",
                     experience=["1"],
                     remote=["1"],
                     listed_at=7200)

unformatted_remote_jobs = linkedin_scraper.search_jobs(keywords="Software",
                     location_name="Canada",
                     experience=["1"],
                     remote=["2"],
                     listed_at=7200)

unformatted_hybird_jobs = linkedin_scraper.search_jobs(keywords="Software",
                     location_name="Canada",
                     experience=["1"],
                     remote=["3"],
                     listed_at=7200)

# Each job is the following format:

# {'trackingUrn': 'urn:li:jobPosting:4011258684', 'repostedJob': False, 
# 'title': 'Journeyperson Heavy Equipment Technicians (3rd year Truck and Transport Apprentices, or 4th year Heavy Equipment Apprentices will be considered) - 50037', 
# '$recipeTypes': ['com.linkedin.deco.recipe.anonymous.Anon1578943416'], 'posterId': '1028006840', '$type': 'com.linkedin.voyager.dash.jobs.JobPosting', 
# 'contentSource': 'JOBS_PREMIUM_OFFLINE', 'entityUrn': 'urn:li:fsd_jobPosting:4011258684'}

# The url for this job would be https://www.linkedin.com/jobs/view/4011258684/, a parsed version of the trackingUrn

# Notice that there is no infomation about the 

gc = gspread.service_account(filename=service_path)
sh = gc.open(tracker_sheet)


