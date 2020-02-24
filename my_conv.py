import numpy as np
def  myconv(x,h):

############################################################################
# A function to generate the output signal y as convolution of input signal
# x and impulse response signal h
############################################################################

# INPUT PARAMETERS---------------------------------------------------------
# x: input signal
# h: impulse response
    len_x = len(x) # length of x
    len_h = len(h) # length of h
############################################################################
# Data processing: convolution (TO BE COMPLETED BY STUDENTS)
############################################################################
# OUTPUT PARAMETERS--------------------------------------------------------
# y: output signal as convolution of input signal x and impulse response h
# length of output array
    len_out = len_x + len_h - 1
    #declare y as empty list
    y = []
    #iterate from 0 to length of y
    for i in range(0,len_out):
        #iteration variable 
        shift = i
        #initiate out
        out = 0
        #iterate over impulse response array
        for j in range(0,len_h):
            #shift h over x
            if (shift >= 0 and shift < len_x):
                out =  out + (x[shift]*h[j])
            #shifts down x until h is completely iterated
            shift = shift-1
        y.append(out)


    return y
