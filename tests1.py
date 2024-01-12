import unittest

from ddcSelenium import get_jobs

class TestGetJobs(unittest.TestCase):

    def test_get_jobs(self):
        jobs = get_jobs()
        self.assertTrue(jobs)

    def test_get_jobs_empty(self):
        driver = webdriver.Chrome()
        driver.get("https://www.dunedin.govt.nz/jobs")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "jobs")))
        jobs = get_jobs(driver)
        self.assertFalse(jobs)

if __name__ == "__main__":
    unittest.main()
