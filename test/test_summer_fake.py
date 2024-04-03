import os
os.environ["UNIT_TEST"] = "true"
from test import mod2

def test_summer_fake():
  assert "11" == mod2.summer(5, 6)