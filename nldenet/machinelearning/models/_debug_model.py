#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------
# nldenet (c) 2020 Dominique F. Garmier MIT licence
#-----------------------------------------------------

'''
this is a sample model for code style references
'''

# local imports
from nldenet.utils.logger import global_logger as global_logger

# 3rd party imports
import tensorflow as tf
import numpy as np

def debug_model(x, w, b, id=0):
    '''
    a simple example model

    this function could also contain shape checks for inputs, to then give relvant debug information
    '''
    net = tf.linalg.transpose(x)
    net = tf.linalg.matmul(net, w)
    net = tf.math.add(net, b)
    net = tf.math.sigmoid(net)

    return net

