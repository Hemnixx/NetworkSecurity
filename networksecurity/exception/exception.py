import sys
from networksecurity.logging.logger import logger
class NetworkSecurityException(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name,self.linenp,str(self.error_message))