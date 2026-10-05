import requests

BASE_URL = "https://jsonplaceholder.typicode.com"  # Using public mock REST API for demonstration

class AgentAPI:
    def __init__(self):
        self.headers = {
            "Content-Type": "application/json"
        }

    def create_agent_api(self, agent_payload):
        """POST request to onboard a new agent."""
        response = requests.post(
            f"{BASE_URL}/users", 
            json=agent_payload, 
            headers=self.headers
        )
        return response

    def get_agent_api(self, agent_id):
        """GET request to retrieve agent details by ID."""
        response = requests.get(
            f"{BASE_URL}/users/{agent_id}", 
            headers=self.headers
        )
        return response