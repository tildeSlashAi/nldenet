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
                    'order': 1,
                    'layers':[],
                    'skip_connections':[]
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
                'order': self._branch_oder,
                'skip_connections': [],
                'layers': []
            }

        self._architectue['branches'].append(new_branch)


    def dense_layer(self, neurons, activation='relu', dropout=False, branch=None):
        '''
        adds dense_layer to architectue
        '''

        new_layer = {
            'neurons': neurons,
            'activation': activation,
            'dropout': dropout
        }

        if branch is None:
            # add layer to all branches
            for branch in self._architectue['branches']:
                branch['layers'].append(new_layer)
        else:
            branch = self._architectue['branches'][branch - 1]
            branch['layers'].append(new_layer)


    def skip_connection(self, form, to, dropout=False, density=1, branch=None):
        '''
        create a dense skip connection between layers "from" to "to".

        densitiy specifies the chance of each connection existing. TODO: deterministic?
        '''

        new_skip_connection = {
            'from': None,
            'to': None,
            'density': density,
            'droput': dropout
        }

        if branch is None:
            for branch in self._architectue['branches']:
                branch['skip_connections'].append(new_skip_connection)

        else:
            branch = self._architectue['branches'][branch - 1]
            branch['skip_connections'].append(new_skip_connection)


    def branch_skip_connection(self):
        '''
        create skip connections between layers of different branches (also backwards)
        can only connect in direction of assending order of branches
        '''
        pass