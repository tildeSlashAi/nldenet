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

class ModelClass:

    def __init__(self):
        #TODO
        pass

    def build(self):
        raise NotImplemented

class SampleModel(ModelClass):

    def __init__(self, input):
        # implement arg check
        super().__init__()
        self._net = tf.linalg.transpose(input)


    def add_sigmoid_layer(self, w, b):
        '''
        adds a sigmoid layer to DebugModel
        '''

        self._net = self._net * w
        self._net = self._net + b
        self._net = tf.math.sigmoid(self._net)


    def build(self):
        '''
        functions that returns compute graph

        raises error if there is a shape missmatch pre runtime
        '''
        # check shape matching
        return self._net
