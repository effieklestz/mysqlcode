

from mysqlcode.main import do_stuff


def test_main():
  result = do_stuff()
  assert result is not None