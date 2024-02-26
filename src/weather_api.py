import requests
import os
import logging
from dotenv import load_dotenv


load_dotenv()

class GeoAPI:
    API_KEY = os.getenv('API_KEY')
    URL_SITE = os.getenv('URL_SITE')
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

    @classmethod
    def is_hot_in_pehuajo(cls):
        try:
            url = f"{cls.URL_SITE}weather?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}&units=metric"
            response = requests.get(url)
            response.raise_for_status()
            weather_data = response.json()

            current_temp = weather_data['main']['temp']
            is_hot = current_temp > 28

            # Registro de la temperatura actual
            logging.info(f"Temperatura actual en Pehuajó: {current_temp} °C")

            # Registro del resultado de si hace calor o no
            logging.info(f"Hace calor en Pehuajó (mayor a 28°C): {is_hot}")

            return is_hot
        except requests.exceptions.RequestException as e:
            logging.error(f"Error al realizar la solicitud HTTP: {e}")
            return False