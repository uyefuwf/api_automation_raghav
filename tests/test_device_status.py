from api.get_api import DeviceAPI  # <--- Must match the class name in get_api.py
import pytest
@pytest.mark.func
def test_device_status(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_device('/device/status')
    assert response.status_code==200, "invalid status code"
    get_status = device_data["get_status"]
    assert get_status["uptimeSeconds"] == 100581
    assert get_status["cpuLoad"] == 1.6000000238418579
    assert get_status["memoryUsedBytes"] == 651968512
    assert get_status["temperatureC"] == 41
