import json
from unittest.mock import mock_open, patch
from dataStore import DataStore


def test_init_read():
  fake_json = '{"id": 1}'
  m = mock_open(read_data=fake_json)
  with patch("builtins.open", m), \
    patch("json.load", return_value=json.loads(fake_json)):
    ds = DataStore()
  assert ds.data == {"id": 1}


def test_init_create():
  m = mock_open()
  m.side_effect = [FileNotFoundError(), m.return_value]
  with patch("builtins.open", m):
    ds = DataStore()
  assert ds.data == {}


def test_create():
  m = mock_open()
  with patch("builtins.open", m), \
    patch("json.load", return_value={}):
    ds = DataStore()
  with patch("builtins.open", m):
    key = ds.create({"x": 1})
  assert key in ds.data
  assert ds.data[key] == {"x": 1}


def test_get():
  with patch("builtins.open", mock_open()), \
    patch("json.load", return_value={"k": "v"}):
    ds = DataStore()
  assert ds.get("k") == "v"


def test_update():
  m = mock_open()
  with patch("builtins.open", m), \
    patch("json.load", return_value={"k": "old"}):
    ds = DataStore()
  with patch("builtins.open", m):
    old = ds.update("k", "new")
  assert old == "old"
  assert ds.data["k"] == "new"

def test_delete():
  m = mock_open()
  with patch("builtins.open", m), \
    patch("json.load", return_value={"x": 1}):
    ds = DataStore()
  with patch("builtins.open", m):
    key = ds.delete("x")
  assert key not in ds.data