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
from nldenet.utils.config import global_config as global_config  # noqa

# 3rd party imports
import tensorflow as tf  # noqa
import numpy as np  # noqa


class ModelClass():
    '''
    Parent Class for nn models

    this class implements base features of any nn model class
    '''

    id_Counter = 1

    def __init__(self, name=None, description=None):
        '''
        generates a unique model id
        assigns / generates nn name
        assigns description for the nn
        '''

        # unique identifier for each nn
        self.id = ModelClass.id_Counter
        ModelClass.id_Counter += 1

        if name is not None:
            self.name = name
        else:
            self.name = 'NN_Model__' + str(self.id)

        if description is not None:
            self.description = description
        else:
            self.description = 'no description was provided'

    def __str__(self):
        '''
        string representation of the model, this includes a title,
        name and id, aswell as some representation of the architecture
        '''
        title = '| ' + self.name + ' | id: ' + self.id + ' |\n'

        try:
            architecture = self._architecture_to_string()
        except NotImplementedError:
            global_logger.warning(
                '_architecture_to_string() function is not defined ' +
                'for {}'.format(self.name))
        else:
            architecture = None

        if architecture is not None:
            return title + self.description + '/n' + architecture
        else:
            return title + self.description

    def _architecture_to_string(self):
        '''
        returns string representing the architecture of the model

        define this function in the parent class,
        else it will raise NotImplementedError
        '''

        raise NotImplementedError

    def build(self):
        '''
        builds a tensorflow function based on some given architecture
        needs to be called before calling the nn

        define this function to determine how architectures
        should be interpreted
        '''

        raise NotImplementedError

    def __call__(self):
        '''
        returns the value of the nn wrt to some given inputs and parameters
        '''
        raise NotImplementedError
