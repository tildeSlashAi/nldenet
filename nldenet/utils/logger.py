#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------
# nldenet (c) 2019 Dominique F. Garmier MIT licence
#-----------------------------------------------------

'''
Description...
'''

# standard lib imports
import os
import shutil
import logging
from logging.handlers import RotatingFileHandler
from logging import NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
from datetime import datetime

class Log:
    '''
    '''
    def __init__(self, logger_name=None, file_path=None, clog_level=WARNING, flog_level=INFO, fmt_string=None, debugger=True, log_byte_size=40*1024*1024):
        '''
        '''
        self._log_byte_size = log_byte_size
        self._has_debugger = debugger
        self._logger_name = logger_name
        self._absolute_path = file_path
        self._fmt_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

        if logger_name is None:
            self._logger_name = 'logger'
    
        if file_path is None:
            file_path = '../logs'
            dir = os.path.dirname(__file__)
            self._absolute_path = os.path.join(dir, file_path)

        if not os.path.exists(self._absolute_path):
            os.mkdir(self._absolute_path)

        self._debug_path = os.path.join(self._absolute_path, 'nldenetDEBUG.log')
        self._log_path = os.path.join(self._absolute_path, 'nldenetLOG.log')

        if fmt_string is not None:
            self._fmt_string = fmt_string

        self._logger = logging.getLogger(logger_name)
        self._logger.setLevel(logging.DEBUG)

        self._formatter = logging.Formatter(self._fmt_string)

        self._file_handler = RotatingFileHandler(self._log_path, mode='a', maxBytes=self._log_byte_size, backupCount=2, encoding=None, delay=0)
        self._file_handler.setLevel(flog_level)
        self._file_handler.setFormatter(self._formatter)

        if self._has_debugger:
            self._file_handler_debug = RotatingFileHandler(self._debug_path, mode='a', maxBytes=self._log_byte_size, backupCount=2, encoding=None, delay=0)
            self._file_handler_debug.setLevel(DEBUG)
            self._file_handler_debug.setFormatter(self._formatter)

        self._console_handler = logging.StreamHandler()
        self._console_handler.setLevel(clog_level)
        self._console_handler.setFormatter(self._formatter)

        self._logger.addHandler(self._console_handler)
        self._logger.addHandler(self._file_handler)
        self._logger.addHandler(self._file_handler_debug)

    def set_levels(self, clog_level=None, flog_level=None):
        if clog_level is not None:
            self._console_handler.setLevel(clog_level)

        if flog_level is not None:
            self._file_handler.setLevel(flog_level)

    def debug(self, message, *args, **kwargs):
        self._logger.debug(message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        self._logger.info(message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        self._logger.warning(message, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        self._logger.critical(message, *args, **kwargs)

    def log(self, level, message, *args, **kwargs):
        self._logger.log(level, message, *args, **kwargs)


def init():
    global_logger = Log()
    return global_logger
       

if __name__ == '__main__':
    print('this is the wrong file to run')
else: #TODO
    args = ()
    kwargs = {}
    global_logger = init(*args, **kwargs)

