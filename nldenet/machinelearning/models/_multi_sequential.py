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
        creates Multi Seq Model
        '''
        super().__init__()
        self._input = input
        self._model = input
        global_logger.info('Multi Sequential Model created!') # better message
        

    def build(self):
        '''
        conduct shape match checks ahead of runtime
        and build compute graph form layer descriptions

        returns: tensorflow computational graph
        '''
        # run shape match checks
        return self._model

    def add_parallel_layer(self, skip_activation='relu'):
        '''
        add parallel network layer
        '''
        #TODO
        # should add parallel duplicate existing layers? Should there be a parallel model class?
        # how should layers be stored? Store layer sizes in Array and only builde the compute
        # when .build is called?
        pass


    def add_sequential_layer(self, activation='relu'):
        pass
