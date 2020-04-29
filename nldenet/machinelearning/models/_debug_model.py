#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------
# nldenet (c) 2020 Dominique F. Garmier MIT licence
#-----------------------------------------------------

'''
this is a sample model for code style references
'''

# local imports


# standard lib imports


# 3rd party imports
import tensorflow as tf
import numpy as np

def debug_model(x, w, b, id=0):
    with tf.variable_scope('debug_model_{}'.format(id), reuse=tf.AUTO_REUSE):
        net = tf.linalg.transpose(x)
        net = tf.linalg.matmul(net, w)
        net = tf.math.add(net, b)
        net = tf.math.sigmoid(net)

    return net

