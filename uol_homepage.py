from playwright.sync_api import Page

class UOLHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.logo = page.locator("img[alt='UOL']")  # Locator for the UOL logo
        self.main_content = page.locator("div.main-content")  # Example locator for main content

    def goto(self):
        self.page.goto("https://www.uol.com.br")

    def validate_page_title(self):
        return "UOL - O melhor conteúdo" in self.page.title()

    def is_logo_visible(self):
        return self.logo.is_visible()

    def is_main_content_visible(self):
        return self.main_content.is_visible()
