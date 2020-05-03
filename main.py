#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------
# nldenet (c) 2020 Dominique F. Garmier MIT licence
#-----------------------------------------------------

import tensorflow as tf
import numpy as np

import nldenet
from nldenet.machinelearning.models import MultiSequential

def layer(*args):
    _ = 0
    for i in args:
        _ += i
    return tf.square(_)

def run(a,b):

    # layer 1
    l1_in = [a]
    l1_out = []

    output = l1_out

    l1_in.append(b)

    

    #running

    # compute l1
    l1_out.append(layer(*l1_in))
    return output

print(run(tf.constant(1), tf.constant(2))[0].numpy())








