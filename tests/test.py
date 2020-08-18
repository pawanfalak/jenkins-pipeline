import sys
sys.path.append("..")
from meetings import find_meeting_timeline
import unittest

class MyTest(unittest.TestCase):
    def test1(self):
        arr=[900,940]
        dep=[910,1200]
        self.assertEqual(find_meeting_timeline(arr,dep,2), 1)
    def test2(self):
        arr = [900, 940, 950, 1100, 1500, 1800] 
        dep = [910, 1200, 1120, 1130, 1900, 2000]
        self.assertEqual(find_meeting_timeline(arr,dep,len(arr)), 3)
    def test3(self):
        arr = [900, 1100, 1300, 1000, 500] 
        dep = [1200, 1400, 1600, 1500, 700]
        self.assertEqual(find_meeting_timeline(arr,dep,len(arr)), 3)
