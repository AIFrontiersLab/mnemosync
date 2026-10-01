"""Tests for Mnemosync MVP."""
import pytest
from fastapi.testclient import TestClient
from main import app, MemoryManager, demo

client = TestClient(app)

def test_demo_runs():
    """Prove core capability works."""
    demo()

def test_add_memory():
    """Happy path: add a memory."""
    res = client.post("/memories", json={"user_id": "u1", "content": "hello"})
    assert res.status_code == 200
    assert res.json()["content"] == "hello"

def test_get_memory():
    """Happy path: retrieve memory."""
    client.post("/memories", json={"user_id": "u2", "content": "data"})
    res = client.get("/memories/u2")
    assert res.status_code == 200
    assert len(res.json()) == 1

def test_get_empty_memory():
    """Failure path: non-existent user."""
    res = client.get("/memories/nonexistent")
    assert res.status_code == 200
    assert res.json() == []

def test_invalid_json():
    """Failure path: missing fields."""
    res = client.post("/memories", json={"user_id": "u1"})
    assert res.status_code == 422