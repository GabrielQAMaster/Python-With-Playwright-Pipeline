import asyncio
import logging
from playwright.async_api import async_playwright

# Step 1: Set up the logger
logging.basicConfig(
    filename="frontend_validation.log",  # Log file path
    level=logging.INFO,                  # Log level
    format="%(asctime)s - %(levelname)s - %(message)s"  # Log format
)

async def validate_linkedin_login_page():
    logging.info("Starting LinkedIn login page validation")

    async with async_playwright() as p:
        # Launch browser and set up video recording
        browser = await p.chromium.launch(headless=False)  # Set headless=True if you don't need to see the browser
        context = await browser.new_context(record_video_dir="videos/")  # Record videos in the "videos/" folder
        page = await context.new_page()

        # Step 2: Navigate to LinkedIn login page
        await page.goto("https://www.linkedin.com/login", wait_until="networkidle")
        logging.info("Navigated to LinkedIn login page")

        # Step 3: Validate the 'aria-label' of the username input field
        try:
            aria_label_value = await page.get_attribute('input#username', 'aria-label')
            assert "E-mail" in aria_label_value and "telefone" in aria_label_value, "Incorrect aria-label for username input field"
            logging.info("Username input field aria-label is correct")
        except AssertionError as e:
            logging.error(f"Username input field validation failed: {e}")

        # Step 4: Validate the password input field
        try:
            assert await page.is_visible('input#password'), "Password input is missing"
            assert await page.get_attribute('input#password', 'type') == "password", "Incorrect type for password input field"
            logging.info("Password input field validation passed")
        except AssertionError as e:
            logging.error(f"Password input field validation failed: {e}")

        # Step 5: Validate the Sign in button (Portuguese version: "Entrar")
        try:
            sign_in_button = page.locator('button[type="submit"]')
            sign_in_button_text = (await sign_in_button.inner_text()).strip()  # Strip extra whitespace
            assert sign_in_button_text == "Entrar", f"Incorrect text on the Sign in button: got '{sign_in_button_text}'"
            logging.info("Sign in button text is correct")
        except AssertionError as e:
            logging.error(f"Sign in button validation failed: {e}")

        # Step 6: Validate the presence of the 'Forgot password?' link
        try:
            assert await page.is_visible("a[href*='/checkpoint/rp/request-password-reset']"), "Forgot password link is missing"
            logging.info("'Forgot password?' link is present")
        except AssertionError as e:
            logging.error(f"'Forgot password?' link validation failed: {e}")

        # Step 7: Close the browser context (which will save the video)
        await context.close()
        logging.info("Finished LinkedIn login page validation and saved video")

# Run the test
asyncio.run(validate_linkedin_login_page())