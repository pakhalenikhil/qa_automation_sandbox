from playwright.sync_api import Page

class AgentOnboardingPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Selectors (using clear Playwright locators)
        self.full_name_input = page.locator("#fullName")
        self.email_input = page.locator("#email")
        self.pan_input = page.locator("#pan")
        self.agent_type_dropdown = page.locator("#agentType")
        self.submit_button = page.locator("button[type='submit']")
        self.success_message = page.locator(".success-msg")

    def navigate_to_portal(self, url: str):
        """Navigates to the agent onboarding UI."""
        self.page.goto(url)

    def fill_onboarding_form(self, full_name: str, email: str, pan: str, agent_type: str):
        """Fills and submits the agent onboarding form."""
        self.full_name_input.fill(full_name)
        self.email_input.fill(email)
        self.pan_input.fill(pan)
        self.agent_type_dropdown.select_option(agent_type)
        self.submit_button.click()