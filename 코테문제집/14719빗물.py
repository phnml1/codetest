import sys
input = sys.stdin.readline
h,w = map(int,input().split());
block = list(map(int,input().split()));
result = 0;
for i in range(1,w-1):
  left_max = max(block[:i])
  right_max = max(block[i+1:]);
  compare = min(left_max,right_max);
  if compare>block[i]:
    result += compare - block[i];
print(result);