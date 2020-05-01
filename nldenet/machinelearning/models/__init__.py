#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------
# nldenet (c) 2020 Dominique F. Garmier MIT licence
#-----------------------------------------------------

'''
this file wraps all models in functions for easy importing
'''

# local imports
from nldenet.machinelearning.models._model_class import SampleModel
from nldenet.machinelearning.models._multi_sequential import MultiSequential

#def debug_model(x, w, b, id=0):
#    return nldenet.machinelearning.models._debug_model.debug_model(x, w, b, id)