# Python Backend Challenge
Construcción de un bot para la toma de pedidos.

## Logging
Este proyecto incluye una funcionalidad de logging para registrar eventos importantes durante la ejecución, facilitando la depuración y el seguimiento del funcionamiento del bot. Los logs están organizados por fecha y se guardan en una carpeta logs en el directorio raíz del proyecto.


## Ejecutar Tests

#### Para ejecutar las pruebas de la función is_hot_in_pehuajo, utiliza el siguiente comando desde la raíz del proyecto:
python -m src.main

#### Para ejecutar las pruebas de la función is_product_available, usa el siguiente comando:
python -m src.order_handling.main

## Estructura del Proyecto
El proyecto está estructurado de la siguiente manera:

* `src/`: Contiene el código fuente principal.
  * `main.py`: Script principal para ejecutar la funcionalidad de clima.
  * `weather_api.py`: Módulo para manejar la API del clima.
  * `order_handling/`: Módulos para manejar la lógica de pedidos.
    * `main.py`: Script principal para las pruebas de manejo de pedidos.
    * `inventory.py`: Funciones relacionadas con la gestión de inventario.
* `tests/`: Pruebas unitarias para las funcionalidades.
  * `test_weather_api.py`
  * `test_inventory.py`
* `utils/`: Utilidades generales.
  * `exceptions.py`
  * `logging_utils.py`
* `requirements.txt/`: Dependencias del proyecto.
* `env/`: Este proyecto utiliza variables de entorno para manejar configuraciones sensibles como claves API. Actualmente están visibles porque es un Challenge.



## Contacto
matias.nbarbieri@gmail.com

