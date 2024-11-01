import asyncio
from playwright.async_api import async_playwright
from linkedin_page import LinkedInLoginPage  # Import the LinkedIn page object class

# Configuration data
USERNAME = "gabriel.vinicius@gmail.com"
PASSWORD = "12345678910"

async def test_linkedin_login():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Use headless=True for headless mode
        page = await browser.new_page()

        # Step 1: Instantiate the LinkedInLoginPage object
        linkedin_login = LinkedInLoginPage(page)
        
        # Step 2: Navigate to the LinkedIn login page
        await linkedin_login.navigate()
        
        # Step 3: Perform login
        await linkedin_login.login(USERNAME, PASSWORD)
        
        # Step 4: Validate the login result
        if await linkedin_login.is_login_successful():
            print("Login was successful.")
        else:
            print("Login failed or additional verification required.")

        await browser.close()

# Run the test
asyncio.run(test_linkedin_login())
