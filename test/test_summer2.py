from unittest import mock
from test import mod2

def test_summer_a():
  with mock.patch("test.mod1.preamble", return_value=""):
    assert "11" == mod2.summer(5, 6)
    
def test_summer_b():
  with mock.patch("test.mod1.preamble") as mock_preamble:
    mock_preamble.return_value = ""
    assert "11" == mod2.summer(5, 6)
    
@mock.patch("test.mod1.preamble", return_value="")
def test_summer_c(mock_preamble):
  assert "11" == mod2.summer(5, 6)
  
@mock.patch("test.mod1.preamble")
def test_caller_d(mock_preamble):
  mock_preamble.return_value = ""
  assert "11" == mod2.summer(5, 6)