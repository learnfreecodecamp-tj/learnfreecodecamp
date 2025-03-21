'''
Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.
'''
import numpy as np

def caculation(lst):
    #check if the string is 9 digits
    if(len(lst)) != 9:
        raise  ValueError("List must contain nine numbers.")

    #convert list to 3*3 Numpy array
    arr = np.array(lst).reshape(3,3)
    
    result = {
        'mean':[arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(),arr.mean().tolist()],
        'variance':[arr.var(axis=0).tolist(), arr.var(axis=1).tolist(),arr.var().tolist()],
        'standard deviation':[arr.std(axis=0).tolist(), arr.std(axis=1).tolist(),arr.std().tolist()],
        'max':[arr.max(axis=0).tolist(), arr.max(axis=1).tolist(),arr.max().tolist()],
        'min':[arr.min(axis=0).tolist(), arr.min(axis=1).tolist(),arr.min().tolist()],
        'sum':[arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(),arr.sum().tolist()]
    }
    return result




    