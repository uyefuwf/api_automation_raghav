from api.get_api import DeviceAPI
import pytest


def test_get_certificate(apiclient):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_certificate("/system/certificate")
    assert response.status_code == 200, "incorrect status code"
    assert "certificate" in response.text.lower(), "certificate data not found"


def test_get_certificate_pem(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_certificate_pem("/system/certificate/pem")
    assert response.status_code == 200, "incorrect status code"
    # expected_type = device_data["certificates"]["expected_type"]
    # assert expected_type in response.headers.get("Content-Type", ""), "unexpected content type"


def test_post_generate_certificate(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    # payload = device_data["certificates"]["generate"]
    response = client.post_generate_certificate("/system/certificate/generate")
    assert response.status_code == 200, "incorrect status code"
    assert "false" not in response.text, "certificate generation failed"


def test_post_restore_default_certificate(apiclient):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.post_restore_default_certificate("/system/certificate/restore_default")
    assert response.status_code == 200, "incorrect status code"
    assert "false" not in response.text, "restore default certificate failed"
