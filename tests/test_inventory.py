import unittest
import logging
from utils.logging_utils import setup_logging, end_logging_execution
from src.order_handling.inventory import is_product_available, _PRODUCT_DF


class TestInventory(unittest.TestCase):

    def test_product_available(self):
        # Test para verificar si el producto está disponible en la cantidad solicitada
        self.assertTrue(is_product_available("Chocolate", 2, 1))

    def test_product_not_available(self):
        # Test para comprobar si el producto no está disponible en la cantidad solicitada
        self.assertFalse(is_product_available("Limon", 1, 1))

    def test_max_attempts_reached(self):
        # Test para verificar que se devuelve False cuando se supera el límite máximo de intentos
        self.assertFalse(is_product_available("Chocolate", 6, 4))
