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
        _ = os.path.dirname(__file__)
        self.__config_path = os.path.join(_, config_path)

        config_exists = self.__config_exists()

        self.__config = open(self.__config_path, 'w+')

        if not config_exists or wipe:
            self.__create_default_config()

    def __config_exists(self):
        '''
        returns: Bool, does config exist?
        '''
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

    def read(self):
        pass

    def write(self):
        pass

    def get_path(self):
        return self.__config_path

    def change_path(self, new_config_path):
        # get new path realtive to __file__
        _ = os.path.dirname(__file__)
        new_config_path = os.path.join(_, new_config_path)

        # close config so it can copy
        self.__config.close()

        # move file and change __config_path
        os.rename(self.__config_path, new_config_path)
        self.__config_path = new_config_path

        # reopen config
        self.__config = open(self.__config_path, 'w+')
        

def init():
    global_config = Config()
    return global_config
       

if __name__ == '__main__':
    print('this is the wrong file to run')
else: #TODO
    args = ()
    kwargs = {}
    global_config = init(*args, **kwargs)