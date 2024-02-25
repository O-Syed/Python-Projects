def solution(A):
    sum_total = sum(A)
    sum_elements = []
    sum_tape = 0
    i=0
    if len(A) == 1:
        return A[0]
    elif len(A) == 2:
        return abs(A[0]-A[1])
    else:
        for i in range(len(A)-1):
            sum_tape += A[i]
            sum_elements.append(abs(sum_total-2*(sum_tape)))
        sum_elements.sort()
    return sum_elements[0]
