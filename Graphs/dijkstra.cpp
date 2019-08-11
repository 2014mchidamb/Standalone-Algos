/*
 * As close to a line by line translation of dijkstra.py as I could get.
 * This one passes all of CF's test cases.
 */
#include <algorithm>
#include <iostream>
#include <queue>
#include <tuple>
#include <vector>

using namespace std;

void dijkstra(int start, int end, const vector<tuple<int, int> > adj_list[], int paths[]) {
        // Cost, current node, previous node.
        using CNP = tuple<int, int, int>;
        priority_queue<CNP, vector<CNP>, greater<CNP> > q;
        q.push(make_tuple(0, start, 0));
        while (!q.empty()) {
                auto cnp = q.top();
                q.pop();

                auto cost = get<0>(cnp), node = get<1>(cnp);
                if (paths[node] >= 0) continue;
                paths[node] = get<2>(cnp);

                if (node == end) return;

                for (const auto& nbr : adj_list[node]) {
                        if (paths[get<1>(nbr)] >= 0) continue;
                        q.push(make_tuple(cost + get<0>(nbr), get<1>(nbr), node));
                }
        }
}

int main() {
        int N, M;
        cin >> N >> M;

        vector<tuple<int, int> > adj_list[N + 1];
        for (int i = 0; i < M; ++i) {
                int a, b, w;
                cin >> a >> b >> w;
                adj_list[a].push_back(make_tuple(w, b));
                adj_list[b].push_back(make_tuple(w, a));
        }

        int paths[N + 1];
        for (int i = 0; i <= N; ++i) paths[i] = -1;
        dijkstra(1, N, adj_list, paths);

        vector<int> optimal_path;
        int cur = N;
        while (cur > 0) {
                optimal_path.push_back(cur);
                cur = paths[cur];
        }

        if (cur != 0) {
                cout << "-1\n";
                return 0;
        }
        for (int i = optimal_path.size() - 1; i > 0; --i) cout << optimal_path[i] << " ";
        cout << N << "\n";

        return 0;
}
