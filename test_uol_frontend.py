from playwright.sync_api import sync_playwright
from uol_homepage import UOLHomePage

def test_uol_frontend():
    with sync_playwright() as p:
        # Launch browser and set up page
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Initialize the Page Object for UOL homepage
        uol_homepage = UOLHomePage(page)
        
        # Navigate to the homepage and perform validations
        uol_homepage.goto()
        
        results = []  # Store results in this list

        # Validate title
        if uol_homepage.validate_page_title():
            results.append("Page title validation passed.")
        else:
            results.append("Page title validation failed.")

        # Check if logo is visible
        if uol_homepage.is_logo_visible():
            results.append("Logo visibility check passed.")
        else:
            results.append("Logo visibility check failed.")

        # Check if main content is visible (additional validation)
        if uol_homepage.is_main_content_visible():
            results.append("Main content visibility check passed.")
        else:
            results.append("Main content visibility check failed.")
        
        # Take a screenshot for reference
        page.screenshot(path="uol_homepage.png")

        # Close the browser
        browser.close()

        # Save results to a txt file
        with open("frontend_validation_results.txt", "w") as file:
            for line in results:
                file.write(line + "\n")
            file.write("Screenshot saved as uol_homepage.png\n")

# Run the test function
test_uol_frontend()
