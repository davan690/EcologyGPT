import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a webdriver.
driver = webdriver.Chrome()

# Get the URL of the target website.
url = "https://www.dunedin.govt.nz/jobs"

# Navigate to the target website.
driver.get(url)

# Wait for the page to load.
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "jobs")))

# Find all of the job listings.
jobs = driver.find_elements(By.XPATH, "//div[@class='job-listing']")

# Save the job listings to a CSV file.
with open("jobs.csv", "w") as f:
    f.write("Title,Department,Location,Description\n")
    for job in jobs:
        title = job.find_element(By.XPATH, "//h3[@class='job-title']").text
        department = job.find_element(By.XPATH, "//span[@class='job-department']").text
        location = job.find_element(By.XPATH, "//span[@class='job-location']").text
        description = job.find_element(By.XPATH, "//p[@class='job-description']").text
        f.write(f"{title},{department},{location},{description}\n")

# Close the webdriver.
driver.close()
