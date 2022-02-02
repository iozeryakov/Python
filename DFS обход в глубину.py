def dfs(g,s):
    global used
    used[ s] =  1
    q = [s]
    while q:
        v = q[-1]
        q.pop()
        for u in g[v]:
             if used[u] == 0:
                 used[u] = 1
                 q.append(u)
#список смежности
n,m=map(int,input().split())
g=[[] for i in range(n+1)]
used=[0]*(n+1)
for _ in range (m):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)
