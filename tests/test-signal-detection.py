import unittest
import matplotlib.pyplot as plt
import copy
from scripts.signal_detection import SignalDetection

class TestSignalDetection(unittest.TestCase):
    sdt1 = SignalDetection(133, 431, 7, 23)
    def test_init_values_are_numeric(self):
        self.hits = hits
        self.misses = misses
        self.false_alarms = false_alarms
        self.correct_rejections = correct_rejections
        attributes = [hits, misses, false_alarms, correct_rejections]
        for x in attributes:
             expected = isinstance(x, (int, float))
             actual = isinstance(x, (int, float))
                                  
    def test_init_values_are_nonnegative(self):
        self.assertTrue(self.hits >= 0)
        self.assertTrue(self.misses >= 0)
        self.assertTrue(self.false_alarms >= 0)
        self.assertTrue(self.correct_rejections >= 0)

    def test_add(self, other):
        sdt_copy = copy.deepcopy(self)
        sdt_add = self.hits + self.misses
        self.assertEqual(sdt_add.hits, sdt_copy.hits, "self.hits was mutated")
        self.assertEqual(sdt_add.misses, sdt_copy.misses, "self.misses was mutated")
        return
    
    def test_sub(self, other):
        sdt_copy = copy.deepcopy(self)
        sdt_sub = self.hits - self.misses
        self.assertEqual(sdt_sub.hits, sdt_copy.hits, "self.hits was mutated")
        self.assertEqual(sdt_sub.misses, sdt_copy.misses, "self.misses was mutated")
        return
    
    def test_multi(self, factor):
        sdt_copy = copy.deepcopy(self)
        sdt_multi = self * factor
        self.assertEqual(sdt_multi.hits, sdt_copy.hits, "self.hits was mutated")
        self.assertEqual(sdt_multi.misses, sdt_copy.misses, "self.misses was mutated")

        return
    

    def check_plot_sdt(self):
        fig, ax = sdt1.plot_sdt()
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_xlabel(), 'False Alarm Rate')
        self.assertEqual(ax.get_ylabel(), 'Hit Rate')

    

