import asyncio
from playwright.async_api import async_playwright

# Configuration data
LINKEDIN_URL = "https://www.linkedin.com/login"
USERNAME = "gabriel.vinicius@gmail.com"
PASSWORD = "#Qwlbtp05089909"

# Function to log in to LinkedIn
async def login_to_linkedin(page):
    try:
        # Increase timeout and use wait_until
        await page.goto(LINKEDIN_URL, timeout=30000, wait_until="networkidle")  
        
        # Wait for username field to appear
        await page.wait_for_selector('input#username')

        await page.fill('input#username', USERNAME)  # Enter email
        await page.fill('input#password', PASSWORD)  # Enter password
        await page.click('button[type="submit"]')  # Click login button

        # Wait for the network to stabilize after login
        await page.wait_for_load_state("networkidle")
        print("Login completed.")
        
        # Validate login by checking the presence of some element (like the home icon)
        if await page.is_visible('div.feed-identity-module__actor-meta'):
            print("Login was successful.")
        else:
            print("Login failed or requires additional verification.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to run the Playwright session
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Show browser for debugging (set to True for headless)
        page = await browser.new_page()

        # Call the login function
        await login_to_linkedin(page)

        await browser.close()

# Run the script
asyncio.run(main())
