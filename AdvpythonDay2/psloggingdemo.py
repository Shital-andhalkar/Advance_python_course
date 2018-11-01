import logging

fmt_str='%(asctime)s:%(levelname)s:%(name)s:%(process)s:%(filename)s:%(message)s'
fmt=logging.Formatter(fmt_str)

sh=logging.StreamHandler()
fh=logging.FileHandler('error.log')

sh.setFormatter(fmt)
fh.setFormatter(fmt)

logger=logging.getLogger('emc')
logger.setLevel(logging.DEBUG)

logger.addHandler(sh)
logger.addHandler(fh)