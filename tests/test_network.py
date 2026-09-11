from api.get_api import *
import pytest
import json

from urllib3 import response


def test_network_ipv4(apiclient,device_data):
    session,base_url = apiclient
    client = DeviceAPI(session,base_url)
    response=client.get_ipv4("/network/ipv4")
    data = response.json()
    network_ipv4 = device_data["network_ipv4"][0]
    assert network_ipv4["dhcpEnabled"] is True
    assert network_ipv4["address"] == data["address"]

@pytest.mark.skip("device ip will change")
def test_network_post(apiclient,device_data):
    session,base_url = apiclient
    client = DeviceAPI(session,base_url)
    network_ipv4 = device_data["network_ipv4"][1]
    response= client.post_ipv4("/network/ipv4",network_ipv4)
    data = response.json()
    assert response.status_code == 200,"ip not set"
    assert network_ipv4["dhcpEnabled"] is False
    assert network_ipv4["address"] == data["address"]


def test_network_ipv6(apiclient,device_data):
    session,base_url = apiclient
    client = DeviceAPI(session,base_url)
    response=client.get_ipv4("/network/ipv6")
    data = response.json()
    assert response.status_code == 200,"ip not set"
    assert "linkLocal" in response.text




