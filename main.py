import os
from linkedin_api import Linkedin
from dotenv import load_dotenv


load_dotenv()

linkedin_username = os.getenv("LINKEDIN_USERNAME")
linkedin_password = os.getenv("LINKEDIN_PASSWORD")

linkedin_scraper = Linkedin(linkedin_username, linkedin_password)

# Get latest software jobs in Ontario 

jobs = linkedin_scraper.search_jobs(keywords="Software",
                     location_name="Ontario, Canada",
                     experience=["1"],
                     remote=["1", "2", "3"],
                     listed_at=720000)
                     