import numpy as np

def looper(start, stop, number):
    if (number <= 0):
        return []
    elif (number == 1):
        return [start]
    elif (number == 2):
        return [start,stop]
    else:
        segments = (float) (stop - start) / (number - 1.0)
        return_list = []
        for i in range(0, number - 1):
            num =  float(start) + segments * i
            return_list.append(num)
        return_list.append(float(stop))
        return return_list

if __name__ == "__main__":
    for i in range(1,6):
        print(looper(1,5,i))