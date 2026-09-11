from api.get_api import DeviceAPI
import pytest


def test_get_webui(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_webui("/network/webui")
    assert response.status_code == 200, "incorrect status code"
    webui = device_data["webui_mode"][0]
    data = response.json()
    assert webui["enabled"] is True


def test_post_webui(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    webui = device_data["webui_mode"][1]
    response = client.post_webui("/network/webui", webui)
    assert response.status_code == 200, "incorrect status code"
    assert webui["enabled"] is False
