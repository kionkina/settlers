'''
['00', '22', '44', '66', '88']
arr = [str(2*x) + str(2*x) for x in range(5)]

[7, 17, 27, 37, 47]
arr = [int((str(x) + '7')) for x in range(5)]
arr = [x*10 + 7 for x in range(5)]

[0,0,0,0,1,2,0,2,4]
'''
def union(A,B):
    '''
    A u B, is the set of all objects that are a member of A, or B, or both. 
    The union of {1, 2, 3} and {2, 3, 4} is the set {1, 2, 3, 4} .
    '''
    arr = [x for x in A if x not in B]
    arr += B
    return arr


print union([1,2,3,3,3,4,5],[1,2])


def intersection(A,B):
    '''
    A *sad U*  B, is the set of all objects that are members of both A and B. 
    The intersection of {1, 2, 3} and{2, 3, 4} is the set {2, 3} .
    '''
    arr = [x for x in A if x in B]
    return arr


print intersection([1,2,3,3,3], [1,2,3,7,8,0])
