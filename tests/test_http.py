import pytest
from api.get_api import DeviceAPI

def test_http_mode(apiclient):
    session,base_url = apiclient
    client = DeviceAPI(session,base_url)
    response = client.get_http('/network/http')
    data = response.json()
    print(data)
    assert response.status_code == 200 , "incorrect status code"
    assert "http" in response.text , "incorrect status code"
@pytest.mark.http

def test_http_post(apiclient,device_data):
    session,base_url = apiclient
    client = DeviceAPI(session,base_url)
    response = client.post_http('/network/http',device_data["http_mode"][0])
    data = response.json()
    assert response.status_code == 200 , "incorrect status code"
    assert "false" in response.text , "incorrect status code"
    print(data)

def test_http_post(apiclient,device_data):
    session,base_url = apiclient
    client = DeviceAPI(session,base_url)
    response = client.post_http('/network/http',device_data["http_mode"][1])
    data = response.json()
    assert response.status_code == 200 , "incorrect status code"
    assert "false" not in response.text , "incorrect status code"
    print(data)    



