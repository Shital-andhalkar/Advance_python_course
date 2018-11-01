import logging

fmt_str='%(asctime)s:%(levelname)s:%(name)s:%(process)s:%(filename)s:%(message)s'
logging.basicConfig(level=logging.DEBUG, format=fmt_str, filename='access.log')

logging.debug('debug message')
logging.info('confirmation note')
logging.warning('warning msg')
logging.critical('panic erros')
