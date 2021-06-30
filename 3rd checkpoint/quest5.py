# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random =  [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

# sort list with key
random.sort(key=takeSecond)
random.sort(reverse=True)

# print list
print('Sorted list:', random)