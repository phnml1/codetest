n = int(input());
arr = list(map(int,input().split()));
dp = [n+1] * n;
dp[0] = 0;
for i in range(n):
  for j in range(1,arr[i]+1):
    if i+j<=n-1:
      dp[i+j] = min(dp[i+j], dp[i]+1);
print(dp[n-1]);