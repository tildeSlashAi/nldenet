#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------
# nldenet (c) 2020 Dominique F. Garmier MIT licence
# ----------------------------------------------------

'''
this is a sample model for code style references

Models should inherit form ModelClass class.
They should be designed similarly to SampleModel
'''

# local imports
from nldenet.utils.logger import global_logger as global_logger
from nldenet.utils.config import global_config as global_config

# 3rd party imports
import tensorflow as tf
import numpy as np


class ModelClass():
    '''
    Parent Class for ml models
    '''

    id_Counter = 1
    

    def __init__(self):
        '''
        gives model id
        '''

        # unique identifier for each nn
        self.id = ModelClass.id_Counter
        ModelClass.id_Counter += 1

    def build(self):
        '''
        builds a tensorflow function based on some given architecture
        needs to be called before calling the nn

        define this function to determine how architectures should be interpreted
        '''


        raise NotImplementedError

    
    def __call__(self):
        '''
        returns the value of the nn wrt to some given inputs and parameters
        '''
        raise NotImplementedError