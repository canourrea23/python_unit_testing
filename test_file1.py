import unittest
from caps import caps


class TestCalc(unittest.TestCase):
    def test_caps(self):
        self.assertEqual(caps.to_caps("HeLlO"), "Should return HELLO")
