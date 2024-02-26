import os
from datetime import datetime
import logging


def setup_logging() -> None:
    """
    Set up the logging configuration for the application.
    """

    # Remove message from googleapliclient INFO
    logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

    # Define the format for Today
    today_format = '%Y-%m-%d'

    # Set today
    today = datetime.now().strftime(today_format)

    # Define the format for datetime
    datetime_format = '%Y-%m-%d %H:%M:%S'

    # Set the execution datetime
    start_time = datetime.now().strftime(datetime_format)

    # Basic logging configuration
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s', 
        datefmt=datetime_format
    )

    # Create log folder
    try:
        create_log_folder()
    except Exception as e:
        raise e

    # Add a file handler to redirect the logs to a file
    file_handler = logging.FileHandler(
        os.path.join('logs', f'{today}.log'), mode='a', encoding="utf-8"
    )
    file_handler.setLevel(logging.INFO)

    # Adding the file handler to the logging configuration
    logging.getLogger('').addHandler(file_handler)

    # Start execution log
    logging.info('--------------------------------------------------')
    logging.info(f'Start execution: {start_time}\n')


def create_log_folder() -> None:
    """
    Create a folder logs folder if it doesn't exist.

    Raises:
        Exception: IF the folder creation fails.
    """
    try:
        log_path =os.path.join('logs')
        os.makedirs(log_path, exist_ok=True)
    except Exception as e:
        logging.error('ERROR -> Failed to create logs folder.')
        raise e


def end_logging_execution() -> None:
    """ Log the end of execution
    """
    end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f'\nEnd execution: {end_time}')
    logging.info('--------------------------------------------------\n\n')