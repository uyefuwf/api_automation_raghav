from api.get_api import DeviceAPI
import pytest

@pytest.mark.rtp
def test_get_rstp(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_rstp("/network/rstp")
    assert response.status_code == 200, "incorrect status code"
    rstp = device_data["rstp_config"][0]
    data = response.json()
    assert rstp["enabled"] is True
    print(data)


def test_post_rstp(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    rstp = device_data["rstp_config"][1]
    response = client.post_rstp("/network/rstp", rstp)
    assert response.status_code == 200, "incorrect status code"
    assert rstp["enabled"] is False
    data = response.json()
    print(data)

