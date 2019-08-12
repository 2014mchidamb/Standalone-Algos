'''
This is an implementation of Edmonds-Karp for max flow, tuned to the 
specifications of the following Kattis problem:
    https://open.kattis.com/problems/mincostmaxflow

Unfortunately, this Python implementation gets TLE (although according
to Kattis, there have been some successful Python 2 submissions).
'''

import heapq

def min_cost_max_flow(s, t, n, cap_matrix, cost_matrix):
    # Returns (max flow, min cost of max flow).
    max_flow, min_cost, df = 0, 0, 0
    prev = [-1 for i in range(n)]

    def find_path():
        nonlocal min_cost, df
        # Find the minimum cost path from s to t using Dijkstra's.
        # Tuple is (cost, current node, previous node, min capacity so far).
        q = [(0, s, n, 1e6)]
        while q:
            cost, v, p, min_cap = heapq.heappop(q)
            if prev[v] >= 0:
                continue
            prev[v] = p

            if v == t:
                # Update flow and cost trackers.
                df = min_cap
                min_cost += min_cap * cost
                return True

            for i in range(n):
                if prev[i] >= 0 or cap_matrix[v][i] == 0:
                    continue
                heapq.heappush(q, (cost + cost_matrix[v][i], i, v, min(min_cap, cap_matrix[v][i])))
        return False

    while find_path():
        cur = t
        while prev[cur] < n:
            cap_matrix[prev[cur]][cur] -= df
            cap_matrix[cur][prev[cur]] += df # Reverse flow.
            cur = prev[cur]
        max_flow += df
        prev = [-1 for i in range(n)]

    return (max_flow, min_cost)

def main():
    n, m, s, t = map(int, input().split())

    # Adjacency matrix representations.
    cap_matrix = [[0 for j in range(n)] for i in range(n)]
    cost_matrix = [[0 for j in range(n)] for i in range(n)]
    for i in range(m):
        u, v, c, w = map(int, input().split())
        cap_matrix[u][v] = c
        cost_matrix[u][v] = w
        cost_matrix[v][u] = -1 * w # Negative cost for reverse edge.

    max_flow, min_cost = min_cost_max_flow(s, t, n, cap_matrix, cost_matrix)
    print(max_flow, min_cost)

if __name__ == '__main__':
    main()
