from api.get_api import DeviceAPI
import pytest

@pytest.mark.skip
def test_factory_reset(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    payload = device_data["system_control"]["factory_reset"]
    response = client.post_factory_reset("/device/factory_reset", payload)
    assert response.status_code == 200, "incorrect status code"
    assert "false" not in response.text, "factory reset failed"

@pytest.mark.reboot
def test_reboot(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    payload = device_data["system_control"]["reboot"]
    response = client.post_reboot("/device/reboot", payload)
    assert response.status_code == 200, "incorrect status code"
    assert "false" not in response.text, "reboot failed"
