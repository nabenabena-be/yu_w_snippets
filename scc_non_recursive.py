# https://github.com/nabenabena-be/yu_w_snippets/blob/main/scc_non_recursive.py

# G = [[] for i in range(N)]
# G_INV = [[] for i in range(N)]
# for u,v in AB:
#     G[u-1].append(v-1)
#     G_INV[v-1].append(u-1)

def scc_decomposition_non_recursive(G, G_INV):
    N = len(G)

    #順番付け========================
    visited = [False] * N
    pos = [0] * N  # 各頂点で次に調べる辺の位置
    t = []

    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        stack = [i]

        while stack:
            x = stack[-1]

            if pos[x] == len(G[x]):
                t.append(stack.pop())
                continue

            y = G[x][pos[x]]
            pos[x] += 1

            if not visited[y]:
                visited[y] = True
                stack.append(y)

    #逆グラフの探索==================
    visited = [False] * N
    SCCs = []

    while t:
        x = t.pop()
        if visited[x]:
            continue

        visited[x] = True
        stack = [x]
        scc = []

        while stack:
            x = stack.pop()
            scc.append(x)

            for i in G_INV[x]:
                if visited[i]:
                    continue
                visited[i] = True
                stack.append(i)

        SCCs.append(scc)

    return SCCs
