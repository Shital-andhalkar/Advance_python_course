from psloggingdemo import logger
from time import sleep

if __name__ == '__main__':
    for item in range(5):
        logger.debug('a dummy log content')
        sleep(.5)

