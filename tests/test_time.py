from api.get_api import DeviceAPI
import pytest


def test_get_time_clock(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_time_clock("/time/clock")
    assert response.status_code == 200, "incorrect status code"
    data = response.json()
    # system_time = device_data["system_time"]
    # assert system_time["timeZoneOffset"] == data["timeZoneOffset"]
    # assert system_time["localTimeString"] == data["localTimeString"]


def test_post_time_clock(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    system_time = device_data["system_time"]
    response = client.post_time_clock("/time/clock", system_time)
    assert response.status_code == 200, "incorrect status code"
    assert "false" not in response.text, "time clock update failed"


def test_get_time_settings(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_time_settings("/time/settings")
    assert response.status_code == 200, "incorrect status code"
    data = response.json()
    print(data)
    # time_settings = device_data["time_settings"][0]
    # assert time_settings["source"] == data["source"]
    # assert time_settings["timeZoneOffset"] == data["timeZoneOffset"]


def test_post_time_settings(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    time_settings = device_data["time_settings"][1]
    response = client.post_time_settings("/time/settings", time_settings)
    assert response.status_code == 200, "incorrect status code"
    assert "false" not in response.text, "time settings update failed"
