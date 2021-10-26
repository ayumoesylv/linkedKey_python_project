# write a python program to remove duplicates from dictionary
def remove_duplicates(dct):
    new_dct = {}

    for i in dct:
        x = dct[i]


# write a program to combine two dictionary adding values for common keys.
def merge_dictionaries(dct1, dct2):
    final = {}
    # if the key is the same, add the values
    for i in dct1:
        if i in dct2:
            final[i] = dct1[i] + dct2[i]
        else:
            final = dct1[i]

    return final


#driver code
#question 8
d1 = {1:1, 2:4, 3:9, 4:10, 5:10, 6:4}


#question 9
d2 = {'a': 100, 'b':200, 'c':300}
d3 = {'a':300, 'b':200, 'd':400}

print(merge_dictionaries(d2, d3))

