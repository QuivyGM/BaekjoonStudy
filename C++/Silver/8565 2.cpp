#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 1001

int n;
int graph[MAX][MAX]; // graph[u][v] == 1 if u can beat v
int adj_count[MAX];  // adjacency count per node
int visited[MAX];

void dfs(int u) {
    for (int i = 0; i < adj_count[u]; i++) {
        int v = graph[u][i];
        if (!visited[v]) {
            visited[v] = 1;
            dfs(v);
        }
    }
}

int main() {
    scanf("%d", &n);

    // 역방향 그래프 구성: winner -> loser
    for (int loser = 1; loser <= n; loser++) {
        int m;
        scanf("%d", &m);
        for (int j = 0; j < m; j++) {
            int winner;
            scanf("%d", &winner);
            graph[winner][adj_count[winner]++] = loser; // winner beats loser
        }
    }

    int result = 0;

    for (int i = 1; i <= n; i++) {
        memset(visited, 0, sizeof(visited));
        visited[i] = 1;
        dfs(i);

        int count = 0;
        for (int j = 1; j <= n; j++) {
            if (visited[j])
                count++;
        }

        if (count == n)
            result++;
    }

    printf("%d\n", result);
    return 0;
}
