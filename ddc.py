import bs4
import requests
from bs4 import BeautifulSoup

# Get the HTML from the target website.
response = requests.get("https://www.dcc.jobs/")

# Parse the HTML.
soup = BeautifulSoup(response.content, "html.parser")

# Extract the job listings.
jobs = soup.find_all("div", class_="job-listing")

# Save the job listings to a CSV file.
with open("jobs.csv", "w") as f:
    f.write("Title,Department,Location,Description\n")
    for job in jobs:
        title = job.find("h3", class_="job-title").text
        department = job.find("span", class_="job-department").text
        location = job.find("span", class_="job-location").text
        description = job.find("p", class_="job-description").text
        f.write(f"{title},{department},{location},{description}\n")
