import sys; 
input = sys.stdin.readline;
# 비슷한문제
n = int(input());
arr = list(map(int,input().split()));
dp = [[0]*21 for _ in range(n-1)];
dp[0][arr[0]] = 1;
result = arr[0];
for i in range(1,n-1):
  for j in range(21):
    if dp[i-1][j]:
      if 0<=j + arr[i]<=20:
        dp[i][j+arr[i]] += dp[i-1][j];
      if 0<=j - arr[i]<=20:
        dp[i][j-arr[i]] += dp[i-1][j];
print(dp[-1][arr[-1]]);