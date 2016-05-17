from . import functions

def printTop(num_val):
    top_list = functions.getTop(num_val)
    for top in top_list:
        print(top[0] + ": " + top[2])
