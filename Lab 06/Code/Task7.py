from math import atan2, degrees
"""
Task 7: Angle of Inclination
"""
def AngleOfInclination(image, left, right, top, bottom, cx, cy):
	return abs(degrees(atan2(bottom - top - cy, right - left - cx)))