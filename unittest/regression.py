import unittest
from homepagetests import HomePageTests
from searchtests import SearchTests

# save classes as tests
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
homepage_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTests)

# create a suite from loaded TestCases
regression = unittest.TestSuite([search_tests, homepage_tests])

# execute the test
unittest.TextTestRunner(verbosity=2).run(regression)
