# logger.py

import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("todo.log"),
        logging.StreamHandler()
    ]
)

# Create a logger object
logger = logging.getLogger('todo_app')
