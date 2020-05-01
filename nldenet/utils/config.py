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
import configparser
from datetime import datetime


class _Config:
    '''
    this class interacts with a config.txt file, stored in the same directory
    '''

    def __init__(self, config_path = '../config.ini', wipe=False):
        '''
        there should only be one instance of this class and it is create in this file.
        '''
        # create config parser
        self._config = configparser.ConfigParser()


        # get path realtive to __file__
        _ = os.path.dirname(__file__)
        self._config_path = os.path.join(_, config_path)

        config_exists = self.__config_exists()

        # either create new config file / reset to default or read existing one
        if not config_exists or wipe:
            self.__create_default_config()
        else:
            self._config.read(self._config_path)


    def __config_exists(self):
        '''
        returns: Bool, does config exist?
        '''
        return os.path.exists(self._config_path)


    def __create_default_config(self):
        '''
        creates config file at _config_path with default entries.
        '''
        # default config, with section main
        self._config['main'] = {
            'foo':'bar'
        }

        # write to config_file
        with open(self._config_path, 'w+') as config_file:
            self._config.write(config_file)


    def fetch_value(self, key, section='main'):
        '''
        read config file and return value belonging to the key

        returns: string or None if key not found
        '''
        self._config.read(self._config_path)
        return self._config.get(section=section, option=key, fallback=None) #TODO raise a warning or error if None is returned
        

    def write_value(self, key, value, section='main'):
        '''
        write key value pair to config

        transforms value to string
        '''
        self._config[section][key] = str(value)

        with open(self._config.read(self._config_path)) as config_file:
            self._config.write(config_file)


    def get_path(self):
        return self._config_path


    def change_path(self, new_config_path):
        # get new path realtive to __file__
        _ = os.path.dirname(__file__)
        new_config_path = os.path.join(_, new_config_path)

        # move file and change __config_path
        os.rename(self._config_path, new_config_path)
        self._config_path = new_config_path
        

if __name__ == '__main__':
    print('this is the wrong file to run')
else: #TODO
    # grab args from sysargs...
    args = ()
    kwargs = {}
    global_config = _Config()