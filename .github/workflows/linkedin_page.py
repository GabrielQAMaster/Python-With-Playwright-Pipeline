from playwright.async_api import Page

class LinkedInLoginPage:
    def __init__(self, page: Page):
        """Initialize the LinkedInLoginPage class with a Playwright Page instance."""
        self.page = page
        self.url = "https://www.linkedin.com/login"
        self.username_input = 'input#username'
        self.password_input = 'input#password'
        self.login_button = 'button[type="submit"]'
    
    async def navigate(self):
        """Navigate to the LinkedIn login page."""
        await self.page.goto(self.url, timeout=30000, wait_until="networkidle")
    
    async def login(self, username: str, password: str):
        """Fill in the username and password fields and submit the login form."""
        await self.page.fill(self.username_input, username)
        await self.page.fill(self.password_input, password)
        await self.page.click(self.login_button)
    
    async def is_login_successful(self):
        """Check if login was successful by verifying if a specific element appears."""
        await self.page.wait_for_load_state("networkidle")
        return await self.page.is_visible('div.feed-identity-module__actor-meta')
