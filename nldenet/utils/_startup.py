#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------
# vislib (c) 2019 Dominique F. Garmier MIT licence
#-----------------------------------------------------

'''
Description...
'''

# local imports
import nldenet.setup as setup
from nldenet.utils.logger import global_logger as logger


def print_logo():
    '''
    this functions prints out an ascii art text of 'nldenet'
        
    Args: None

    Returns: None
    
    Raises: None
    '''

    print('       _     _      _   _      _   ')
    print('      | |   | |    | \ | |    | |  ')
    print(' _ __ | | __| | ___|  \| | ___| |_ ')
    print('| \'_ \| |/ _` |/ _ \ . ` |/ _ \ __|')
    print('| | | | | (_| |  __/ |\  |  __/ |_ ')
    print('|_| |_|_|\__,_|\___|_| \_|\___|\__|')
    
    return

def print_info(version, licence):
    '''
    this functions prints out an ascii art text of 'nldeNet'
        
    Args: takes two string Type arguments
    version: the nldenet version
    licence: nldenet's licence

    Returns: None
    
    Raises: None
    '''

    print('running:', version)
    print('nldeNet (c) 2020 Dominique F. Garmier', licence)
    print('GitLab: (https) https://gitlab.com/dotslashai/dsai-nldenet.git')
    print('         (ssh)  git@gitlab.com:dotslashai/dsai-nldenet.git')

    return

