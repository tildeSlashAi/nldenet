#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------
# nldenet (c) 2020 Dominique F. Garmier MIT licence
#-----------------------------------------------------

'''
this file wraps all models in functions for easy importing
'''

#local imports
from nldenet.utils.config import global_config as global_config
from nldenet.utils.logger import global_logger as global_logger
from nldenet.machinelearning.models._model_class import ModelClass

# 3rd party imports
import tensorflow as tf
import numpy as np

class MultiSequential(ModelClass):
    '''
    Multi Sequential Model for fitting solutions to nonlinear differential equation solutions

    flagship network architecture of nldenet (NonLinear Differential Equation net)

    Parallel feedforward networks with backwards skip connections to adjacent feedforward branch.
    '''

    def __init__(self, input):
        '''
        check input shape
        '''
        super().__init__()
        self._net = tf.transpose(input)
        global_logger.info('Multi Sequential Model created!')
        

    def build(self):
        '''
        conduct shape match checks ahead of runtime

        returns: tensorflow computational graph
        '''
        # run shape match checks
        return self._net

    def add_parallel_layer(self, skip_activation='relu'):
        pass


    def add_sequential_layer(self, activation='relu'):
        pass
