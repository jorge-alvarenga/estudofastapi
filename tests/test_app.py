from fastapi.testclient import TestClient

from estudofastapi.app import app

client = TestClient(app)
