import re 
from playwright.sync_api import sync_playwright


JOB_PATTERNS = [
    "linkedin.com/jobs",
    "indeed.com/viewjob",
    "glassdoor.com/job",
    "greenhouse.io",
    "lever.co"
]

def is_job_page(url: str) -> bool:
    """Check if URL matches known job site patterns or contains keywords."""
    if any(p in url for p in JOB_PATTERNS):
        return True

    # Fetch the page content and look for job-related keywords
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless = no UI
        page = browser.new_page()
        try:
            page.goto(url, timeout=8000)  # 8s timeout
            content = page.content().lower()
            if any(word in content for word in ["apply", "responsibilities", "qualifications", "requirements"]):
                return True
        except Exception as e:
            print("Could not check page:", e)
        finally:
            browser.close()
    return False
