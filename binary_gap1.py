def solution(N):
  '''
  the function takes a number, converts it in binary, and return the maximum binary Gap the number has
  '''
    bin_num= str(bin(N))[2:]
    gaps={0}
    count=0
    for i in bin_num:
        if i=='0':
            count+=1
        elif i=='1' and count!=0:
            gaps.add(count)
            count=0
        else:
            continue
    return max(gaps)
    # Implement your solution here
