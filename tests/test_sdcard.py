from api.get_api import DeviceAPI
import pytest

def test_get_sd_status(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_sd_status("/storage/sd/status")
    assert response.status_code == 200, "incorrect status code"
    data = response.json()
    expected_status = device_data["sd_card"]["expected_status"]
    assert expected_status == data["status"]


def test_get_sd_usage(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_sd_usage("/storage/sd/usage")
    assert response.status_code == 200, "incorrect status code"
    data = response.json()
    print(data)
    # expected_usage = device_data["sd_card"]["expected_usage"]
    # assert expected_usage["totalBytes"] == data["totalBytes"]
    # assert expected_usage["usedBytes"] == data["usedBytes"]


def test_post_sd_mount(apiclient):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.post_sd_mount("/storage/sd/mount")
    assert response.status_code == 200, "incorrect status code"
    assert "accepted" in response.text, "SD card mount failed"
    print (response.text)


def test_post_sd_unmount(apiclient):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.post_sd_unmount("/storage/sd/unmount")
    assert response.status_code == 200, "incorrect status code"
    assert "accepted" in response.text, "SD card unmount failed"
    print(response.text)


def test_post_sd_format(apiclient):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.post_sd_format("/storage/sd/format")
    assert response.status_code == 200, "incorrect status code"
    assert "status" in response.text, "SD card format failed"

@pytest.mark.sdcard

def test_post_sd_recover(apiclient):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.post_sd_recover("/storage/sd/recover")
    assert response.status_code == 200, "incorrect status code"
    assert "accepted" in response.text, "SD card recover failed"
