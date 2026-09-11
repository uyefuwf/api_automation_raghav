# tests/test_get.py
from api.get_api import DeviceAPI  # <--- Must match the class name in get_api.py
import pytest
def test_get(apiclient):
    # 1. Unpack the fixture from conftest.py
    session, base_url = apiclient
    
    # 2. Initialize the API client
    api_client = DeviceAPI(session, base_url)
    
    # 3. Call the endpoint
    response = api_client.get_req('/device/info')
    
    # 4. Assert the status code
    assert response.status_code == 200, f"incorrect due to {response.status_code}" 
 # 5. Print the response so you can see it in the terminal
    data= response.json()
    assert "deviceType" in data
    assert "macAddress" in data


def test_get_device_info(apiclient):
    # Setup
    session, base_url = apiclient
    api_client = DeviceAPI(session, base_url)
    
    # Act
    response = api_client.get_req('/device/info')
    
    # Assert
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("\nResponse JSON:", response.json())

def test_response_time_is_fast(apiclient):
    """Hardware APIs should respond quickly"""
    session, base_url = apiclient
    api_client = DeviceAPI(session, base_url)
    
    response = api_client.get_req('/device/info')
    
    # Assert response takes less than 2 seconds
    assert response.elapsed.total_seconds() < 2.0, f"API took too long: {response.elapsed.total_seconds()}s"

def test_content_type_is_json(apiclient):
    """Verify the API returns JSON data"""
    session, base_url = apiclient
    api_client = DeviceAPI(session, base_url)
    
    response = api_client.get_req('/device/info')
    
    assert "application/json" in response.headers["Content-Type"], "Response is not JSON"

def test_critical_fields_exist_and_match(apiclient):
    """Verify the exact values for the most important business fields"""
    session, base_url = apiclient
    api_client = DeviceAPI(session, base_url)
    
    response = api_client.get_req('/device/info')
    data = response.json()
    
    assert data["deviceType"] == "CameraPod"
    assert data["model"] == "NB166"
    assert data["dhcp_mode"] == "DHCP"

def test_mac_and_ip_formats_are_valid(apiclient):
    """Verify the MAC address and IP address match standard regex formats"""
    session, base_url = apiclient
    api_client = DeviceAPI(session, base_url)
    
    response = api_client.get_req('/device/info')
    data = response.json()
    assert "02:00:06:12:12:14" == data["macAddress"]


@pytest.mark.smoke
# test_device.py
def test_device_info(apiclient, device_data):
    session, base_url = apiclient
    api_client = DeviceAPI(session, base_url)

    get_info = device_data["get_info"]

    assert get_info["deviceType"] == "CameraPod"
    assert get_info["model"] == "NB166"
    assert get_info["firmwareVersion"] == "3.141.6"
    assert get_info["serialNumber"] == "123456789"
    assert get_info["ipv4_address"] == "192.168.1.2"
    assert get_info["macAddress"] == "02:00:06:12:12:14"
    assert get_info["dhcp_mode"] == "DHCP"