from api.get_api import *
import pytest


def test_get_rtsp(apiclient,device_data):
    session,base_url = apiclient
    clint= DeviceAPI(session,base_url)
    response = clint.rtsp_mode("/network/rtp")
    assert response.status_code == 200,"invalid status code"
    data = response.json()
    rtp = device_data["rtsp_mode"][0]
    assert rtp["mode"] == "rtsps"

def test_rtsp_mode(apiclient,device_data):
    session,base_url = apiclient
    clint= DeviceAPI(session,base_url)
    rtp = device_data["rtsp_mode"][1]
    response = clint.post_rtsp_mode("/network/rtp",rtp)
    assert response.status_code == 200,"invalid status code"
    data = response.json()
    assert rtp["mode"] == "rtsp"
    
