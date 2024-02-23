#A non-empty array A consisting of N integers is given.
# The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value,
 # except for one element that is left unpaired.
from collections import Counter
def solution(A):
    # Implement your solution here
    occur = Counter(A)
    num = [i for i in occur.keys() if occur[i]%2 != 0]
    return num[0]
