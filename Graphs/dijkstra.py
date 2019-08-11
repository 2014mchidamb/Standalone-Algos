'''
This is an implementation of Dijkstra's algorithm tuned to the specifications
of the following problem:
    http://codeforces.com/contest/20/problem/C

Python 3 is a little too slow for CF though, so this one gets a TLE.
See the C++ translation for a solution that passes.
'''

import heapq

def dijkstra(start, end, adj_list, paths):
    # Priority queue contrains triplet (cost, cur_node, prev_node).
    priority_q = [(0, start, 0)]
    while priority_q:
        cost, node, prev = heapq.heappop(priority_q)
        if paths[node] >= 0:
            # We've already reached this node.
            continue
        paths[node] = prev

        if node == end:
            break

        for weight, nbr in adj_list[node]:
            if paths[nbr] >= 0:
                continue
            heapq.heappush(priority_q, (cost + weight, nbr, node))

def main():
    n, m = map(int, input().split())

    # Adjacency list stores tuples of (weight, node).
    adj_list = [[] for i in range(n + 1)]
    for i in range(m):
        a, b, w = map(int, input().split())
        adj_list[a].append((w, b))
        adj_list[b].append((w, a))

    # Paths stores the previous node in the optimal path
    # to a given node. 0 is a dummy start node.
    paths = [-1 for i in range(n + 1)]
    dijkstra(1, n, adj_list, paths)

    # Reconstruct optimal path.
    best_path = [n]
    while paths[best_path[-1]] > 0:
        best_path.append(paths[best_path[-1]])

    if best_path[-1] == 1:
        print(*best_path[::-1])
    else:
        print(-1)

if __name__ == '__main__':
    main()
