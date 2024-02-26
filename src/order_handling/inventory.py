import pandas as pd
import logging
from utils.logging_utils import setup_logging, end_logging_execution


_PRODUCT_DF = pd.DataFrame({
    "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
    "quantity": [3, 10, 0, 5]
})


def is_product_available(product_name, quantity, attempt=1, max_attempts=3):
    try:
        product = _PRODUCT_DF[_PRODUCT_DF['product_name'] == product_name] # encuentro el producto en el DataFrame

        if product.empty:
            logging.error(f"Producto {product_name} no encontrado.")
            return False
        
        result = not product.empty and product.iloc[0]['quantity'] >= quantity
        logging.info(f"Procesando Test: '{product_name}, {quantity}, {attempt}'. Resultado: {result}")

        if attempt > max_attempts:
            logging.info(f"Intento {attempt}: Demasiados intentos para {product_name}.")
            return False
        
        return result
    except Exception as e:
            logging.error(f"Error al procesar el pedido: {e}")
            return False

