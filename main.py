import os
from linkedin_api import Linkedin
from dotenv import load_dotenv


# Authenticate using any Linkedin account credentials
load_dotenv()

linkedin_username = os.getenv("LINKEDIN_USERNAME")
linkedin_password = os.getenv("LINKEDIN_PASSWORD")

scraper = Linkedin(linkedin_username, linkedin_password)

