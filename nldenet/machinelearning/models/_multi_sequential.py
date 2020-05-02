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

        # store input
        self._input = input

        # nn architecture
        self._architectue = {
            branches: [{
                    order: 1
                }]
            }

        # highest branch order / number of parallel branches / order of ode
        self._branch_oder = 1

        # print info to log
        global_logger.info('Multi Sequential Model created, model-id: {}'.format(self._id)) # better message
        

    def build(self):
        '''
        conduct shape match checks ahead of runtime
        and build compute graph form layer descriptions

        returns: tensorflow computational graph
        '''
        # run shape match checks

        # compile architectue to compute graph
        # iterate all branches
        # iterate all layers
        # iterate all skip connections

        # print info to log
        global_logger.info('built Multi Sequential Model, model-id: {}'.format(self._id))

        # return compute graph
        return self._model


    def print_model(self):
        '''
        prints / returns diagroam of model
        '''
        print('*a cool diagram*')


    def add_parallel_branch(self, skip_activation='relu'):
        '''
        add parallel branch to multi sequential network
        '''
        
        # increase highest order of branch since new one is created
        self._branch_oder += 1
        
        # TODO add more features to a branch
        new_branch = {
                'order': self._branch_oder
            }

        self._architectue['branches'].append(new_branch)


    def dense_layer(self, neurons, activation='relu', dropout=False, oder_of_branch=None):
        '''
        adds dense_layer to architectue
        '''

        layer = {
            'neurons': neurons,
            'activation': activation,
            'dropout': dropout
        }

        if not parallel_layer:
            # apply layer to all parallel sequential models
            pass


    def skip_connection(self):
        '''
        create skip connection between layers of the same branch (only forward)
        '''
        pass


    def branch_skip_connection(self):
        '''
        create skip connections between layers of different branches (also backwards)
        can only connect in direction of assending order of branches
        '''
        pass 