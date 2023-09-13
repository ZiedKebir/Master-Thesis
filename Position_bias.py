from Loading_param import *
import numpy as np

def Position_bias(d):
    # Define the function

    def b1(x):
        return 1 / np.log2(x + 1)

    def b2(x):
        return 1 / x

    def b3(x):
        return 1 / np.sqrt(x)

    def b4(x):
        return 1 / (2 ** x)

    if d["Type_position_bias"]=="1":
        return b1
    elif d["Type_position_bias"]=="2":
        return b2
    elif d["Type_position_bias"] == "3":
        return b3
    elif d["Type_position_bias"] == "4":
        return b4




