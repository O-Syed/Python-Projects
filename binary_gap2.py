def solution(N):
    gaps = bin(N)[2:].strip('0').split('1')
    # Find the length of the longest gap
    longest_gap = max(len(gap) for gap in gaps)
    return longest_gap
