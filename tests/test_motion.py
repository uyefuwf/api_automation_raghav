from api.get_api import DeviceAPI
import pytest


def test_get_motion_config(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_motion_config("/motion/config")
    assert response.status_code == 200, "incorrect status code"
    data = response.json()
    config = device_data["motion_config"]["config"]
    assert config["enabled"] is True
    assert config["sensitivity"] == data["sensitivity"]


def test_post_motion_config(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    config = device_data["motion_config"]["config"]
    response = client.post_motion_config("/motion/config", config)
    assert response.status_code == 200, "incorrect status code"
    assert "false" not in response.text, "motion config update failed"


def test_get_motion_events(apiclient):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_motion_events("/motion/events")
    assert response.status_code == 200, "incorrect status code"
    assert "motion" in response.text.lower(), "motion events data not found"


def test_post_clear_motion_events(apiclient):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.post_clear_motion_events("/motion/events/clear")
    assert response.status_code == 200, "incorrect status code"
    assert "false" not in response.text, "clear motion events failed"


def test_get_motion_status(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_motion_status("/motion/status")
    assert response.status_code == 200, "incorrect status code"
    data = response.json()
    expected_status = device_data["motion_config"]["expected_status"]
    assert expected_status["motionTransitionId"] == data["motionTransitionId"]
