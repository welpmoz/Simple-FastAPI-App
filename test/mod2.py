import os
if os.getenv("UNIT_TEST"):
  import test.fake_mod1 as mod1
else:
  from test import mod1

def summer(x: int, y: int) -> str:
  return mod1.preamble() + f"{x + y}"