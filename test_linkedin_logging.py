import asyncio
import logging
from playwright.async_api import async_playwright
from linkedin_page import LinkedInLoginPage  # Import the Page Object class

# Configure logging (this can be customized)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration data
USERNAME = "your_email_here"
PASSWORD = "your_password_here"

async def test_linkedin_login():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Launch the browser (set headless=True to run without GUI)
        page = await browser.new_page()

        # Step 1: Instantiate the LinkedInLoginPage object
        linkedin_login = LinkedInLoginPage(page)
        
        # Step 2: Navigate to the LinkedIn login page
        logging.info(f"Navigating to: {linkedin_login.url}")
        await linkedin_login.navigate()
        
        # Step 3: Perform login
        logging.info(f"Filling username: {USERNAME}")
        logging.info("Filling password: [HIDDEN]")  # Hiding actual password
        await linkedin_login.login(USERNAME, PASSWORD)
        
        # Step 4: Validate the login result
        if await linkedin_login.is_login_successful():
            logging.info("Login was successful.")
        else:
            logging.warning("Login failed or additional verification required.")

        await browser.close()

# Run the test
asyncio.run(test_linkedin_login())
