import pytest
from fastapi.testclient import TestClient

from estudofastapi.app import app


@pytest.fixture
def client():
    return TestClient(app)
