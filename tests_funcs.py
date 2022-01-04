import funcs
import unittest
import math

class TestFuncs(unittest.TestCase):

	def test_max_int(self):
		self.assertEqual(funcs.max_int(0,2),2)
		self.assertEqual(funcs.max_int(-1,-5),-1)
		self.assertEqual(funcs.max_int(-1,2),2)
		self.assertEqual(funcs.max_int(0,0),0)

	def test_min_int(self):
		self.assertEqual(funcs.min_int(0,2),0)
		self.assertEqual(funcs.min_int(-1,-5),-5)
		self.assertEqual(funcs.min_int(-1,2),-1)
		self.assertEqual(funcs.min_int(0,0),0)

	def test_mean_int(self):
		self.assertEqual(funcs.mean_int([1,2,3,4,5]),3.0)
		self.assertEqual(funcs.mean_int([-2,-1,0,1,2]),0.0)
		self.assertEqual(funcs.mean_int([-2,-1,0,1,2,3]),0.5)
		self.assertEqual(funcs.mean_int([0,0,0]),0.0)

	def test_median_int(self):
		self.assertEqual(funcs.median_int([1,2,5,4,3]),3)
		self.assertEqual(funcs.median_int([-2,-1,0,1,2]),0)
		self.assertEqual(funcs.median_int([-2,-1,0,1,2,3,4]),1)
		self.assertEqual(funcs.median_int([0,1,2,3]),1)
		self.assertEqual(funcs.median_int([0,0,0,0]),0)
		self.assertEqual(funcs.median_int([]),None)

	def test_std_dev(self):
		self.assertEqual(funcs.std_dev([1,2,5,4,3]),math.sqrt(2))
		self.assertEqual(funcs.std_dev([-2,-1,0,1,2]),math.sqrt(2))
		self.assertEqual(funcs.std_dev([-2,-1,0,1,2,3,4]),2)
		self.assertEqual(funcs.std_dev([0,1,2,3]),math.sqrt(1.25))

	def test_is_geo_progression(self):
		self.assertEqual(funcs.is_geo_progression([1,2,5,4,3]),False)
		self.assertEqual(funcs.is_geo_progression([-2,-1,0,1,2]),False )
		self.assertEqual(funcs.is_geo_progression([-2,-1,0,1,2,3,4]),False)
		self.assertEqual(funcs.is_geo_progression([1,2,4,8,16]),True)

if __name__ == '__main__':
	unittest.main()
