#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------
# nldenet (c) 2019 Dominique F. Garmier MIT licence
#-----------------------------------------------------

import tensorflow as tf
import numpy as np

import nldenet
from nldenet.machinelearning.models import debug_model

x = np.ones((1))
w = np.ones((1))
b = np.ones((1))

net = debug_model(x, w, b, id=1)
# test