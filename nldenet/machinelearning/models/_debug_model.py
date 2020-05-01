#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------
# nldenet (c) 2020 Dominique F. Garmier MIT licence
#-----------------------------------------------------

'''
this is a sample model for code style references

Models should be defined as one callable function.
The model i.e. the callable function should have the same name as the file.

The arguments of that models function can contain hyperparameters of the model (# of layers etc.)

The Function must return a tensorflow compute graph.
'''

# local imports
from nldenet.utils.logger import global_logger as global_logger
from nldenet.utils.config import global_config as global_config

# 3rd party imports
import tensorflow as tf
import numpy as np

def debug_model(x, w, b, id=0):
    '''
    a simple example model
    this function could also contain shape checks for inputs, to then give relvant debug information

    returns: compute graph for: sigmoid(x^T*w + b)
    '''
    net = tf.linalg.transpose(x)
    net = tf.linalg.matmul(net, w)
    net = tf.math.add(net, b)
    net = tf.math.sigmoid(net)

    return net

