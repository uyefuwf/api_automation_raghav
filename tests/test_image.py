from api.get_api import DeviceAPI
import pytest


def test_get_image_settings(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_image_settings("/image/settings")
    assert response.status_code == 200, "incorrect status code"
    data = response.json()
    image = device_data["image_settings"]
    assert image["brightness"] == data["brightness"]
    assert image["contrast"] == data["contrast"]
    assert image["dayNightMode"] == data["dayNightMode"]


def test_post_image_settings(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    image = device_data["image_settings"]
    response = client.post_image_settings("/image/settings", image)
    assert response.status_code == 200, "incorrect status code"
    assert "false" not in response.text, "image settings update failed"


def test_post_restore_image_defaults(apiclient):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.post_restore_image_defaults("/image/settings/restore_default")
    assert response.status_code == 200, "incorrect status code"
    assert "false" not in response.text, "restore image defaults failed"


def test_get_roi_exposure(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_roi_exposure("/image/roi_exposure")
    assert response.status_code == 200, "incorrect status code"
    data = response.json()
    roi = device_data["roi_exposure"][0]
    assert roi["xStart"] == data["xStart"]
    assert roi["yStart"] == data["yStart"]


def test_post_roi_exposure(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    roi = device_data["roi_exposure"][1]
    response = client.post_roi_exposure("/image/roi_exposure", roi)
    assert response.status_code == 200, "incorrect status code"
    assert roi["xStart"] == 0
    assert roi["yStart"] == 0


def test_get_image_frame(apiclient):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_image_frame("/image/frame")
    assert response.status_code == 200, "incorrect status code"


def test_get_overlay(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_overlay("/image/overlay")
    assert response.status_code == 200, "incorrect status code"
    data = response.json()
    overlay = device_data["overlay_settings"][0]
    assert overlay["timestampEnabled"] is True
    assert overlay["position"] == data["position"]


def test_post_overlay(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    overlay = device_data["overlay_settings"][1]
    response = client.post_overlay("/image/overlay", overlay)
    assert response.status_code == 200, "incorrect status code"
    assert overlay["position"] == "bottom-left"
