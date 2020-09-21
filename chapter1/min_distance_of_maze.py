from collections import deque
file = 'maze.txt'

N = 10
M = 10

maze = []
with open(file, 'r') as f:
    for line in f.readlines():
        maze.append(list(line))


dist = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(-1)
    dist.append(row)

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
start = (0, 1)
end = (9, 8)

que = deque()
que.append(start)
dist[start[0]][start[1]] = 0


while len(que)>0:
    p = que.popleft()
    print('p:', p)
    if p == end:
        break
    for (x,y) in direct:
        nx = p[0] + x
        ny = p[1] + y
        if 0<=nx<N and 0<=ny<M and maze[nx][ny]!='#' and dist[nx][ny]==-1:
            dist[nx][ny] = dist[p[0]][p[1]]+1
            que.append((nx, ny))
for i in dist:
    print(i)
print(dist[end[0]][end[1]])
