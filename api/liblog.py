import logging

def log_info(s: str):
# {
	logger = _logger()
	logger.info(s)
# }

__logger = None
def _logger():
	global __logger
	if not __logger:
		logging.basicConfig(level=logging.INFO)
		__logger = logging.getLogger(__name__)
	
	return __logger
