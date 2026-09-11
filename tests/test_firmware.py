from api.get_api import DeviceAPI
import pytest


def test_get_firmware_version(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_firmware_version("/firmware/version")
    assert response.status_code == 200, "incorrect status code"
    data = response.json()
    expected_version = device_data["firmware"]["version"]
    assert expected_version == data["version"]

def test_post_firmware_upload(apiclient):

    session, base_url = apiclient

    client = DeviceAPI(session, base_url)

    response = client.post_firmware_image(
        "/firmware/image/upload",
        "KAVRO_Firmware_3.141.6.img"
    )
    print("Status:", response.status_code)
    print("Response:", response.text)

    assert response.status_code == 200, "incorrect status code"
    assert "false" not in response.text.lower(), "firmware upload failed"

@pytest.mark.start

def test_post_firmware_update(apiclient):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.post_firmware_update("/firmware/update/start")
    assert response.status_code == 200, "incorrect status code"
    assert "false" not in response.text, "firmware update failed"

@pytest.mark.status
def test_get_firmware_update_status(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_firmware_update_status("/firmware/update-status")
    assert response.status_code == 200, "incorrect status code"
    data = response.json()
    # update_status = device_data["firmware"]["update_status"]
    # assert update_status["status"] == data["status"]
    # assert update_status["lastFirmwareVersion"] == data["lastFirmwareVersion"]