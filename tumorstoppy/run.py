import numpy as np
import itertools as it
from distances import *
from measures import *
from data import *

cdr3 = CDR3_13
print(error_evaluation(None, cdr3['training'], verbose=True))
