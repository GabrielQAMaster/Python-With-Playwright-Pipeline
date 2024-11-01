import asyncio
from playwright.async_api import async_playwright
from linkedin_page import LinkedInLoginPage  # Import the Page Object class

# Configuration data
USERNAME = "gabriel.vinicius@gmail.com"
PASSWORD = "12345678910"

async def test_linkedin_login():
    async with async_playwright() as p:
        # Set up video recording in the context
        browser = await p.chromium.launch(headless=False)
        
        # Enable video recording
        context = await browser.new_context(record_video_dir="videos/")  # Videos will be saved in the "videos" folder
        page = await context.new_page()

        # Step 1: Instantiate the LinkedInLoginPage object
        linkedin_login = LinkedInLoginPage(page)
        
        # Step 2: Navigate to the LinkedIn login page
        print(f"Navigating to: {linkedin_login.url}")
        await linkedin_login.navigate()
        
        # Step 3: Perform login
        print(f"Filling username: {USERNAME}")
        print("Filling password: [HIDDEN]")  # Hiding actual password
        await linkedin_login.login(USERNAME, PASSWORD)
        
        # Step 4: Validate the login result
        if await linkedin_login.is_login_successful():
            print("Login was successful.")
        else:
            print("Login failed or additional verification required.")
        
        # Step 5: Close the browser and save the video
        await context.close()  # Video is saved when context is closed

# Run the test
asyncio.run(test_linkedin_login())
