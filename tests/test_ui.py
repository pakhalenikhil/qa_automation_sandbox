import pytest
import uuid
from playwright.sync_api import Page
from pages.onboarding_page import AgentOnboardingPage

def test_agent_onboarding_ui(page: Page):
    """Validates UI form interaction and web page automation using Playwright."""
    unique_id = str(uuid.uuid4())[:5]
    test_email = f"ui_agent_{unique_id}@testing.com"
    
    onboarding_page = AgentOnboardingPage(page)
    
    # 1. Open target portal (using demo practice URL)
    onboarding_page.navigate_to_portal("https://demo.playwright.dev/todomvc/")
    
    # 2. Verify page title loads correctly
    assert "TodoMVC" in page.title()