import pytest
from CompanyApi import CompanyApi

@pytest.fixture
def client():
    return CompanyApi("https://x-clients-be.onrender.com")