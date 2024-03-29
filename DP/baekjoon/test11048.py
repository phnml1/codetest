# 준규는 N×M 크기의 미로에 갇혀있다. 미로는 1×1크기의 방으로 나누어져 있고, 각 방에는 사탕이 놓여져 있다. 미로의 가장 왼쪽 윗 방은 (1, 1)이고, 가장 오른쪽 아랫 방은 (N, M)이다.

# 준규는 현재 (1, 1)에 있고, (N, M)으로 이동하려고 한다. 준규가 (r, c)에 있으면, (r+1, c), (r, c+1), (r+1, c+1)로 이동할 수 있고, 각 방을 방문할 때마다 방에 놓여져있는 사탕을 모두 가져갈 수 있다. 또, 미로 밖으로 나갈 수는 없다.

# 준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수의 최댓값을 구하시오.

n,m = map(int, input().split());
miro = [] 
for i in range(n):
  miro.append(list(map(int,input().split())));
for i in range(n):
  for j in range(m):
    if i-1>=0 and j-1<0:
      miro[i][j] = miro[i-1][j] + miro[i][j];
    if j-1>=0 and i-1<0:
      miro[i][j] = miro[i][j-1] + miro[i][j];
    if i-1>=0 and j-1>=0: 
      miro[i][j] = max(miro[i-1][j],miro[i][j-1],miro[i-1][j-1])+ miro[i][j];
print(miro[n-1][m-1]);