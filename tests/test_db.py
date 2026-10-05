import pytest
import uuid
from utils.db_helper import insert_agent, get_agent_by_email, delete_agent_by_email

@pytest.fixture
def test_agent_data():
    """Fixture to generate unique agent test data and clean up after the test finishes."""
    unique_id = str(uuid.uuid4())[:6]
    data = {
        "full_name": f"Test Agent {unique_id}",
        "email": f"agent_{unique_id}@testing.com",
        "pan_number": f"ABCDE{unique_id[:4].upper()}Z",
        "agent_type": "FRESH",
        "status": "PENDING"
    }
    
    yield data  # Hand control over to the test execution
    
    # Teardown / Cleanup step after test completes
    delete_agent_by_email(data["email"])


def test_insert_and_verify_agent(test_agent_data):
    """Verifies inserting an agent into PostgreSQL and retrieving exact matching data."""
    # 1. Insert agent record into DB
    inserted_id = insert_agent(
        full_name=test_agent_data["full_name"],
        email=test_agent_data["email"],
        pan_number=test_agent_data["pan_number"],
        agent_type=test_agent_data["agent_type"],
        status=test_agent_data["status"]
    )
    assert inserted_id is not None, "Failed to retrieve generated agent_id!"

    # 2. Retrieve agent record from DB using email
    db_agent = get_agent_by_email(test_agent_data["email"])
    
    # 3. Assert DB values match inserted test payload
    assert db_agent is not None, "Agent record was not found in the database!"
    assert db_agent["full_name"] == test_agent_data["full_name"]
    assert db_agent["email"] == test_agent_data["email"]
    assert db_agent["pan_number"] == test_agent_data["pan_number"]
    assert db_agent["agent_type"] == test_agent_data["agent_type"]
    assert db_agent["status"] == test_agent_data["status"]