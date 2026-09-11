from api.get_api import DeviceAPI
import pytest

from urllib3 import response


def test_onvif(apiclient,device_data):
    session,base_url = apiclient
    client = DeviceAPI(session,base_url)
    response=client.get_onvif("/network/onvif")
    onvif = device_data["onvif_mode"][0]
    assert onvif["enabled"] is True

def test_post_onvif(apiclient,device_data):
    session,base_url = apiclient
    client = DeviceAPI(session,base_url)
    onvif = device_data["onvif_mode"][1]
    response = client.post_onvif("/network/onvif",onvif)
    assert response.status_code == 200, "invalid status code"
    assert onvif["enabled"] is False
