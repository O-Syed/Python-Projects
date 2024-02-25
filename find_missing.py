from collections import Counter
def solution(A):
    while len(A) > 0: 
        occ=Counter(A)
        for i in range(1,len(A)+1):
            if not occ[i]:
                # print(i)
                return i
            else:
                # print(i)
                continue
        return i+1
    return 1 
