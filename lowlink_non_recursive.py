#  ██╗      ██████╗ ██╗    ██╗██╗     ██╗███╗   ██╗██╗  ██╗
#  ██║     ██╔═══██╗██║    ██║██║     ██║████╗  ██║██║ ██╔╝
#  ██║     ██║   ██║██║ █╗ ██║██║     ██║██╔██╗ ██║█████╔╝
#  ██║     ██║   ██║██║███╗██║██║     ██║██║╚██╗██║██╔═██╗
#  ███████╗╚██████╔╝╚███╔███╔╝███████╗██║██║ ╚████║██║  ██╗
#  ╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
#                       N O N - R E C U R S I V E
#
#  File: lowlink_non_recursive.py
#  URL:  https://github.com/nabenabena-be/yu_w_snippets/blob/main/lowlink_non_recursive.py

class LowLink():

    def _build() -> None:
        pass

    def __init__(self,N: int, uv: list) -> None:

        self.order = [-1 for _ in range(N)]
        self.low = [-1 for _ in range(N)]
        self.split_count = [1 for _ in range(N)]
        self.Connected_Component_number = 0

        M = len(uv)
        is_used_edge = [False for _ in range(M)]      
        G = [[] for _ in range(N)]
        visit_ord = 0

        for i in range(M):
            u,v = uv[i]
            G[u].append((v,i))
            G[v].append((u,i))

        for i in range(N):
            if self.order[i] != -1:
                continue

            self.Connected_Component_number += 1
            self.split_count[i] = 0

            dfs_stack = [(~i,-1,-1),(i,-1,-1)]

            while dfs_stack:
                x, px, edge_num = dfs_stack.pop()

                if x < 0:
                    if px == -1:
                        continue
                    if not is_used_edge[edge_num]:
                        continue
                    x = ~x
                    if self.low[px] > self.low[x]:
                        self.low[px] = self.low[x]
                    if self.order[px] <= self.low[x]:
                        self.split_count[px] += 1
                    continue
                
                if self.order[x] != -1:
                    if px == -1:
                        continue
                    if is_used_edge[edge_num]:
                        continue
                    if self.low[px] > self.order[x]:
                        self.low[px] = self.order[x]
                    continue
                    
                if px != -1:
                    is_used_edge[edge_num] = True

                self.order[x] = visit_ord
                self.low[x] = visit_ord
                visit_ord += 1

                for cx,edge_num in G[x]:
                    if cx == px:
                        continue
                    dfs_stack.append((~cx,x,edge_num))
                    dfs_stack.append((cx,x,edge_num))


    def is_bridge(self,u,v):#橋か判定
        if self.order[v] < self.order[u]:#uが親，vが子
            u, v = v, u
        if self.order[u] < self.low[v]:
            return True
        return False

    def is_articulation_point(self,u):#関節点か判定
        if self.split_count[u] >= 2:#split_countが2以上<->関節点
            return True
        return False
