#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------
# nldenet (c) 2020 Dominique F. Garmier MIT licence
#-----------------------------------------------------

import tensorflow as tf
import numpy as np

import nldenet
from nldenet.machinelearning.models import MultiSequential


model_1 = MultiSequential(None)
model_2 = MultiSequential(None)

print(model_1._id)
print(model_2._id)
