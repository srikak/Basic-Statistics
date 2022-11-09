# Mean 
def mean(array):
    '''
    INPUT
    array : 1D float array, list
    
    OUTPUT
    avg : mean of the 1D array, float
    '''
    
    avg = sum(array)/len(array)
    return avg

# Median
def median(array):
    '''
    INPUT
    array : 1D float array, list
    
    OUTPUT
    med : median of the 1D array, float
    '''
    # Sort the array
    array = sorted(array)
    
    # If array has even number of elements, median = avg(two middle elemnets)
    if len(array)%2 == 0:
        first = int(len(array)/2)    
        med = (array[first] + array[first-1])/2
        
    # If array has odd number of elements, median = middle element    
    else:
        med = array[int((len(array)+1)/2)]
            
    return med 

# Mode
def mode(array):
    '''
    INPUT
    array : 1D float array, list
    
    OUTPUT
    tmode : mode of the 1D array, float
    '''
    # Obtain unique elements in the array and sort them in ascending order
    unique = sorted(list(set(array)))
    
    cnt = [0]*len(unique)
    
    # Find no. of occurences/frequency of each unique element
    for i in range(0,len(unique)):
        c = 0
        for j in array:
            if unique[i] == j:
                c = c+1
        cnt[i] = c
    
    # Check if more than one element has same frequency
    ref = max(cnt)
    
    c = 0
    m = []
    for i in range(0,len(cnt)):
        if cnt[i] == ref:
            c = c+1
            m.append(i)
    
    # If there is only one mode
    if c == 1:
        tmode = unique[cnt.index(ref)]
        
    # If there are more than a mode, it returns the smallest one
    else:
        tmode = unique[m[0]]
        
    return tmode
