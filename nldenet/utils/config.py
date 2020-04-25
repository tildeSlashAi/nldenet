#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------
# nldenet (c) 2019 Dominique F. Garmier MIT licence
#-----------------------------------------------------

'''
Description...
'''

# local imports
from nldenet.utils.logger import global_logger as logger

# standard lib imports
import os
from datetime import datetime


class Config:
    '''
    this class interacts with a config.txt file, stored in the same directory
    '''

    def __init__(self, config_path = '../config.txt', wipe=False):

        # get path realtive to __file__
        dir = os.path.dirname(__file__)
        __config_path__ = os.path.join(dir, config_path)
        self.__config_path = __config_path__

        config_exists = self.__config_exists()

        self.__config = open(self.__config_path, 'w')

        if not config_exists or wipe:
            self.__create_default_config()

    def __config_exists(self):
        return os.path.exists(self.__config_path)

    def __create_default_config(self):
        default_config = """
        this is the default config
        line2
        line3
        """
        self.__config.write(default_config)
        self.__config.flush()
        os.fsync(self.__config.fileno())

    def read_config(self):
        pass

    def write_to_config(self):
        pass
