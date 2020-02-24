
import numpy as np
def my_diffequation(x, alpha, N):

############################################################################
# A function to generate the output signal y of the system described by a
# diffence equation
############################################################################

# INPUT PARAMETERS---------------------------------------------------------
# x: input signal
# alpha: decreasing amplitude
# N: delay between consecutive echoes

############################################################################
# Data processing (TO BE COMPLETED BY STUDENTS)
############################################################################
# OUTPUT PARAMETERS--------------------------------------------------------
# y: output signal

    L=len(x)
    # Write the code including comments to explain what you are doing
    len_y = L+N-1 #length of output
    y = np.zeros(len_y) #create array of zeroes with length of output
    
    #output before signals are relected and echoes reach location, output just = input
    for i in range(0,N):
        y[i] = x[i]
    #output when input signals are still continuing, but reverberations from previous x[n] are added to signal  
    for j in range(N,L):
        y[j] = x[j] + (alpha+y[j-N])
    #output for when input signal no longer remains, but reverberations and echoes from previous x[n] are still present
    for k in range(L, len_y):
        y[k] = alpha*y[k-N]
        
    
    


    return y


