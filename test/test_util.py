import unittest

from synthme import util

class TestUtil(unittest.TestCase):
  def test_get_pronunciation(self):
    self.assertEqual(util.get_pronunciation("me"), [28, 7])