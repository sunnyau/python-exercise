from unittest import TestCase
from src import sample1


class TestSample1(TestCase):
    def test_sample1(self):
        self.assertEqual(sample1.sumthemup(3, 4), 7)

    def test_sample1_again(self):
        self.assertEqual(sample1.sumthemup(5, 7), 12)