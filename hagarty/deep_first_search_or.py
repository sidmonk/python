M = [[False, True, True, False, False],
     [True, False, True, False, False],
     [True, True, False, True, False],
     [False, False, True, False, False],
     [False, False, False, False, False]]




def do_dfs(M):
     n = len(M)
     visited = [False for i in range(n)]

     def dfs(i):
          visited[i] = True
          for j in range(n):
               if M[i][j] and not visited[j]:
                    dfs(j)

     for i in range(n):
          if not visited[i]:
               dfs(i)
     return visited

# color
def do_cdfs(M):
     n = len(M)
     colors = ['white' for i in range(n)]

     def cdfs(i):
          colors[i] = 'gray'
          for j in range(n):
               if M[i][j] and colors[j] == 'white':
                    cdfs(j)
          colors[i] = 'black'

     for i in range(n):
          if colors[i] == 'white':
               cdfs(i)
     return colors

print(do_cdfs(M))