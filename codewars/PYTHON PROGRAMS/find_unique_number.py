'''
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance
'''


def find_uniq(arr):
    # your code here
    '''
    for i in arr:
        if (arr.count(i)==1):
            n=i
            break
    '''
    a=max(arr)
    b=min(arr)
    if (arr.count(a)==1):
        n=a
    else:
        n=b
    return n   # n: unique integer in the array
