import datetime

# Each job is the following format:

# {'trackingUrn': 'urn:li:jobPosting:4011258684', 'repostedJob': False, 
# 'title': 'Journeyperson Heavy Equipment Technicians (3rd year Truck and Transport Apprentices, or 4th year Heavy Equipment Apprentices will be considered) - 50037', 
# '$recipeTypes': ['com.linkedin.deco.recipe.anonymous.Anon1578943416'], 'posterId': '1028006840', '$type': 'com.linkedin.voyager.dash.jobs.JobPosting', 
# 'contentSource': 'JOBS_PREMIUM_OFFLINE', 'entityUrn': 'urn:li:fsd_jobPosting:4011258684'}

# The url for this job would be https://www.linkedin.com/jobs/view/4011258684/, a parsed version of the trackingUrn
urns = set()

def format_jobs(unformatted_jobs, keyword, location, urns):
    formatted_jobs = []
    
    for job in unformatted_jobs:
        tracking_urn = job['trackingUrn'].split(':')[-1]
        
        if tracking_urn in urns or job['repostedJob']:
            continue
        else:
            urns.add(tracking_urn)


        formatted_jobs.append(['Fetched ',
            keyword,
            job['title'],
            location,
            "Toronto",
            f"https://www.linkedin.com/jobs/view/{tracking_urn}",
            
            ])
        
    return formatted_jobs
