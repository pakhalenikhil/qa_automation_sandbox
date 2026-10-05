import pytest
import uuid
from utils.api_helper import AgentAPI

@pytest.fixture
def api_client():
    return AgentAPI()

def test_create_agent_api_success(api_client):
    """Validates HTTP 201 response and payload integrity when onboarding an agent via API."""
    unique_id = str(uuid.uuid4())[:5]
    payload = {
        "name": f"Agent {unique_id}",
        "username": f"agent_{unique_id}",
        "email": f"agent_{unique_id}@test.com"
    }

    # 1. Trigger API endpoint
    response = api_client.create_agent_api(payload)

    # 2. Assert HTTP Status Code
    assert response.status_code == 201, f"Expected 201 Created, got {response.status_code}"

    # 3. Assert Response Body Data
    data = response.json()
    assert "id" in data
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]