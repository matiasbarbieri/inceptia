import unittest
from src.weather_api import GeoAPI

class TestWeatherAPI(unittest.TestCase):

    def test_is_hot_in_pehuajo(self):
        result = GeoAPI.is_hot_in_pehuajo()
        self.assertIsNotNone(result)  # Verificar que se obtiene un resultado (True o False)
        print(result)  # Opcional: Imprimir el resultado para depuración

if __name__ == "__main__":
    unittest.main()