def bfs( g, s):
    global used
    used[s]=1
    q=[s]
    while q:
        v=q[0]
        q.pop(0)
        for u in g[v]:
            if used[u]==0:
                used[u]=1
                q.append(u)
#список смежности
n,m=map(int,input().split())
g=[[] for i in range(n+1)]
used=[0]*(n+1)
for _ in range (m):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)
for i in range(1,n+1):
    print (g[i])
# 5 8
# 1 2
# 1 5
# 1 3
# 1 4
# 2 4
# 5 4
# 4 3
# 3 5