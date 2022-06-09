def quicksorting(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less =[ i for i in array[1:] if i < pivot]
        greater =[ i for i in array[1:] if i > pivot]
        return quicksorting(less) + [pivot] + quicksorting(greater)

print (quicksorting([10, 5, 2, 3, 6, 7, 6]))