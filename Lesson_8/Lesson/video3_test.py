import requests
import pytest

def test_simple_req():
    resp = requests.get('https://x-clients-be.onrender.com/company')
    response_body = resp.json()
    id_company = response_body[5]
    assert id_company["id"] == response_body[5]["id"]
    assert resp.status_code == 200