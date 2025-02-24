import pytest
import unittest 
from unittest.mock import patch
from io import StringIO
from App.Timer import countdown

@patch("sys.stdout", new_callable=StringIO)
def test_countdown(mock_stdout):
    countdown(1) 
    output = mock_stdout.getvalue().strip()
    assert output == "You want to start the focusing timer?"

    #countdown(2)
    #output = mock_stdout.getvalue().strip()
    #assert output == "⏰ Time's up!"

@pytest.fixture
def mock_stdout(monkeypatch):
    mock_stdout = StringIO()
    monkeypatch.setattr("sys.stdout", mock_stdout)
    return mock_stdout

if __name__=="__main__":
    unittest.main()
