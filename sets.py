"""
Team Settlers
Queenie Xiang and Karina Ionkina 
SoftDev2 pd7
HW16 -- Ready, Set, Math!
2018-04-26
"""

'''
2018-04-25 DO NOW: 
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

print "\n***UNION***"
print union([1,2,3,4,5],[1,2])
print union([2, 4], [1, 3])
print union([1, 2, 10], [92, 43, 29]) 


def intersection(A,B):
    '''
    A *sad U*  B, is the set of all objects that are members of both A and B. 
    The intersection of {1, 2, 3} and{2, 3, 4} is the set {2, 3} .
    '''
    arr = [x for x in A if x in B]
    return arr

print "\n***INTERSECTION***"
print intersection([1,2,3], [1,2,3,7,8,0])
print intersection([0, 2, 1], [1, 9, 10])
print intersection([67, 24, 15, 90], [31, 24, 87, 67]) 

def set_diff(U,A):
    '''
    set of all members of U that are not members of A. 
    The set difference {1, 2, 3} \ {2, 3, 4} is {1}
    The set difference {2, 3, 4} \ {1, 2, 3} is {4}
    '''
    arr = [x for x in U if x not in A]
    return arr

print "\n***SET DIFF***"
print set_diff([1,2,3], [2,3,4])
print set_diff([2,3,4], [1,2,3])
print set_diff([2,5,6], [1, 2, 4]) 
    
    
def sym_diff(A,B):
    '''
    set of all objects that are a member of exactly one of A and B
    for the sets {1, 2, 3} and {2, 3, 4} , the symmetric difference set is {1, 4}
    '''

    arr = [x for x in A if x not in B]
    arr += [x for x in B if x not in A]
    return arr

print "\n***SYM DIFF***"
print sym_diff([1,2,3], [2,3,4])
print sym_diff([29, 2, 9], [1, 3, 9])
print sym_diff([67, 24, 1], [24, 5, 90])


def cartesian_product(A,B):
    ''' 
    set whose members are all possible ordered pairs (a, b) where a is a member of A and b is a member of B. 
    The cartesian product of {1, 2} and {red, white} is {(1, red), (1, white), (2, red), (2, white)}.
    '''

    arr = [[x,y] for x in A for y in B]
    return arr

print "\n***CARTESIAN PRODUCT***"
print "#1: ['red', 'white'], [1, 2]" 
print cartesian_product(["red", "white"], [1, 2])
print "\n#2: ['red', 'white'], [1, 2, 3])"
print cartesian_product(["red", "white"], [1, 2, 3])
print "\n#3: ['x', 'y', 'z'], [1, 2, 3])"
print cartesian_product(["x", "y", "z"], [1, 2, 3])

