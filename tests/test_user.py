from api.get_api import *
import pytest
import json

def test_pwd_change(apiclient, device_data):
    session, base_url = apiclient
    client = DeviceAPI(session, base_url)

    response = client.post_user("/users/default/password/change",device_data["pwd_change"]
    )
    data= response.json()
    print(data)
    assert response.status_code == 200 , "incorrect data"
    assert "updated" in response.text


def test_add_usr(apiclient,device_data):
    session,base_url=apiclient
    client= DeviceAPI(session,base_url)
    response = client.post_user("/users/add",device_data["add_usr"][0])
    data = response.json()
    print(data)
    assert response.status_code == 200,"incorrect status code"
    assert "success" in response.text or data.get("success") is True

@pytest.mark.pwd
def test_update_usr(apiclient,device_data):
    session,base_url=apiclient
    client = DeviceAPI(session,base_url)
    response = client.post_user("/users/update",device_data["add_usr"][1])
    data = response.json()
    print("Status:", response.status_code)
    print("Response headers:", response.headers)
    print("Response text:", response.text)
    print(data)
    assert response.status_code==200,"inncorrect status code"
    assert "User added successfully" in response.text


def test_delete_usr(apiclient,device_data):
    session,base_url=apiclient
    client = DeviceAPI(session,base_url)
    response = client.post_user("/users/delete",device_data["delete_usr"][1])
    data = response.json()
    assert response.status_code == 200,"incorrect status code"
    assert "success" in response.text or data.get("success") is True
