from api.get_api import DeviceAPI
import pytest


def test_get_rtp_sessions(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_rtp_sessions("/rtp/sessions")
    assert response.status_code == 200, "incorrect status code"
    data = response.json()
    expected = device_data["rtp_sessions"]["expected_sessions"]
    assert expected[0]["protocol"] == data[0]["protocol"]
    assert expected[0]["clientIp"] == data[0]["clientIp"]


def test_terminate_rtp_session(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    terminate_id = device_data["rtp_sessions"]["terminate_id"]
    response = client.post_terminate_rtp_session(
        f"/rtp/sessions/{terminate_id}/terminate"
    )
    assert response.status_code == 200, "incorrect status code"
    assert "false" not in response.text, "termination failed"
