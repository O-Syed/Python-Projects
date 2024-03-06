import re

n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
s = "".join(["".join(col) for col in zip(*matrix)])
print(re.sub(r"(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])", " ", s))
