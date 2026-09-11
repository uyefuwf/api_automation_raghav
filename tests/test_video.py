from api.get_api import DeviceAPI
import pytest

def test_get_video_common(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_video_common("/video/common")
    assert response.status_code == 200, "incorrect status code"
    data = response.json()
    video_common = device_data["video_common"][0]
    assert video_common["frameRateFps"] == data["frameRateFps"]


def test_post_video_common(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    video_common = device_data["video_common"][0]
    response = client.post_video_common("/video/common", video_common)
    assert response.status_code == 200, "incorrect status code"
    assert video_common["frameRateFps"] != 25
    assert video_common["frameRateFps"] == 30
    data = response.json()
    print(data)


def test_get_video_streams(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_video_streams("/video/streams")
    assert response.status_code == 200, "incorrect status code"
    data = response.json()
    print(data)
    # stream_list = device_data["video_streams"]["stream_list"]
    # assert stream_list[1]["label"] == data[1]["label"]
    # assert stream_list[0]["enabled"] is True

def test_get_specific_video_stream(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    response = client.get_specific_video_stream(f"/video/streams/1")
    assert response.status_code == 200, "incorrect status code"
    data = response.json()
    payload = device_data["video_streams"]["specific_stream"]["payload"]
    assert payload["encoder"]["codec"] == data["encoder"]["codec"]

@pytest.mark.video

def test_post_specific_video_stream(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    # stream_id = device_data["video_streams"]["specific_stream"]["id"]
    update_payload = device_data["video_streams"]["specific_stream"]["update_payload"]
    response = client.post_specific_video_stream(
        f"/video/streams/3", update_payload
    )
    assert response.status_code == 200, "incorrect status code"
    assert update_payload["encoder"]["codec"] == "h265"
