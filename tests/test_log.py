from api.get_api import DeviceAPI  # <--- Must match the class name in get_api.py
import pytest


def test_log(apiclient):
    # Destructure the tuple returned by your conftest fixture
    session, base_url = apiclient
    
    # Initialize the cleanly abstracted interface client
    client = DeviceAPI(session, base_url)
    
    # Hit your dynamic logs endpoint
    response = client.get_logs("/device/logs")
    
    # Assert verification
    assert response.status_code == 200, f"Error in fetching logs: {response.text}"


@pytest.mark.log
def test_post(apiclient):
    session, base_url = apiclient
    client = DeviceAPI(session,base_url)
    response = client.post_logs("/device/logs/clear",payload=None)
    assert response.status_code in [200,201]

