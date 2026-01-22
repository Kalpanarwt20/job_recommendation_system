from apify_client import ApifyClient
import os
from dotenv import load_dotenv
load_dotenv()


apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))




# fetch linkedin jobs based on search query and loaction
def fetch_linkedin_jobs(search_query, location="india", num_jobs=60):
    # Mock LinkedIn jobs - generating dynamically
    job_titles = search_query.split(",") if "," in search_query else [search_query] * num_jobs
    companies = ["Tech Company Inc", "Digital Solutions Ltd", "Innovation Hub", "Cloud Systems", "Data Analytics Pro", "Web Innovations", "Software House", "IT Solutions", "Tech Startups", "Enterprise Solutions"]
    salaries = ["₹8-12 LPA", "₹10-15 LPA", "₹12-18 LPA", "₹15-20 LPA", "₹7-11 LPA", "₹9-14 LPA", "₹11-16 LPA", "₹6-10 LPA", "₹13-19 LPA", "₹14-22 LPA"]
    
    mock_jobs = []
    for i in range(num_jobs):
        title = job_titles[i % len(job_titles)].strip() if len(job_titles) > 1 else search_query
        mock_jobs.append({
            "title": f"{title} (Position {i+1})",
            "companyName": companies[i % len(companies)],
            "location": location,
            "url": f"https://linkedin.com/jobs/view/{1234567890 + i}",
            "salary": salaries[i % len(salaries)]
        })
    return mock_jobs[:num_jobs]
    # pass




# fetch naukri jobs based on search query and loaction
def fetch_naukri_jobs(search_query, location="india", num_jobs=60):
    # Mock Naukri jobs - generating dynamically
    job_titles = search_query.split(",") if "," in search_query else [search_query] * num_jobs
    companies = ["Enterprise Solutions", "Cloud Services Corp", "Analytics Pro", "Web Experts", "Mobile Dev House", "AI Solutions", "DevOps Masters", "Security First", "Database Pros", "Open Source Community"]
    salaries = ["₹7-11 LPA", "₹9-14 LPA", "₹11-16 LPA", "₹6-10 LPA", "₹12-17 LPA", "₹8-13 LPA", "₹10-15 LPA", "₹13-18 LPA", "₹9-12 LPA", "₹15-21 LPA"]
    
    mock_jobs = []
    for i in range(num_jobs):
        title = job_titles[i % len(job_titles)].strip() if len(job_titles) > 1 else search_query
        mock_jobs.append({
            "title": f"{title} (Job {i+1})",
            "companyName": companies[i % len(companies)],
            "location": location,
            "url": f"https://naukri.com/job-listings/{2345678901 + i}",
            "salary": salaries[i % len(salaries)]
        })
    return mock_jobs[:num_jobs]
    