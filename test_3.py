# write unit test for the func in main.py
# this unit test should use the name_to_number() func
# to convert the name to number
# and then compare the number with the expected output
# check the output of the func for several different inputs
# to make sure it is producing the correct output
#  use the unittest module
#  use the main() func to run the test
#  use the assertEqual() func to test the output of the func
#  use the __name__ == "__main__" block to run the main() func
#  use the unittest.main() func to run the test
#  use the -v flag for verbose output to see the result of the test
#  use the -b flag to suppress output from passing tests
#  use the -f flag to stop the test on the first failure
#  use the -c flag to show output for each test

import unittest
from main import name_to_number

class TestNameToNumber(unittest.TestCase):
    # test name_to_number func
    def test_name_to_number(self):
        self.assertEqual(name_to_number('rock'), 0)
        self.assertEqual(name_to_number('Spock'), 1)
        self.assertEqual(name_to_number('paper'), 2)
        self.assertEqual(name_to_number('lizard'), 3)
        self.assertEqual(name_to_number('scissors'), 4)
        self.assertEqual(name_to_number('test'), 0)

    


    
if __name__ == "__main__":
    unittest.main()









