from utils.logging_utils import setup_logging, end_logging_execution
import unittest
from tests.test_inventory import TestInventory

if __name__ == '__main__':
    setup_logging()

    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestInventory) # ejecuto tests
    unittest.TextTestRunner().run(test_suite)

    end_logging_execution()
