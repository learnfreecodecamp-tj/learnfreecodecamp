'''
main.py, entry of the function
'''
from mean_var_std import caculation

#test correct input
try:
    res = caculation([0,1,2,3,4,5,6,7,8])
    print("result for correct input:", res)
except ValueError as expt:
    print(expt)
    print("\n\n")
    
#test incorrect 
try:
    res = caculation([0,1,2,3,4,5,6,7])
    print("result for incorrect input:", res)
except ValueError as expt:
    print("result for incorrect input:", expt)

    