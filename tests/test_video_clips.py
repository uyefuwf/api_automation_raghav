from api.get_api import DeviceAPI
import pytest


def test_post_generate_video_clip(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    stream_id = device_data["video_clips"]["generate"]["stream_id"]
    payload = device_data["video_clips"]["generate"]["payload"]
    response = client.post_generate_video_clip(
        f"/video/streams/{stream_id}/clip", payload
    )
    assert response.status_code == 200, "incorrect status code"
    assert "false" not in response.text, "video clip generation failed"


def test_get_clip_status(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    clip_id = device_data["video_clips"]["clip_id"]
    response = client.get_clip_status(f"/video/clips/{clip_id}/status")
    assert response.status_code == 200, "incorrect status code"
    assert "clip" in response.text.lower() or "status" in response.text.lower(), "clip status not found"


def test_get_download_video_clip(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)
    clip_id = device_data["video_clips"]["clip_id"]
    response = client.get_download_video_clip(f"/video/clips/{clip_id}/download")
    assert response.status_code == 200, "incorrect status code"
