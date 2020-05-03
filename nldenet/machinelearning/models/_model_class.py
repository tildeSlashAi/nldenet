#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------
# nldenet (c) 2020 Dominique F. Garmier MIT licence
#-----------------------------------------------------

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

        self._id = ModelClass.id_Counter
        ModelClass.id_Counter += 1

    def build(self):
        raise NotImplemented