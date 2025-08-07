#include <stdio.h>

// 플레이어수
int players[1001][1001] = {0};
int visited[1001] = {0};

void dfs(int curr, int n) {
    visited[curr] = 1;
    for (int i = 0; i < n; i++) {
        if (players[curr][i] == 1 && !visited[i]) {
            dfs(i, n);
        }
    }
}

int main() {

    // 플레이어 수 입력
    int n = 0;
    scanf("%d", &n);

    int m = 0;
    char string[100];
    int stronger;
    // 데이터 입력 받기
    for (int i = 0; i < n; i++) {

        // 더 약한 입력 받기
        scanf("%d", &m);

        // 더 약한 플레이어 없으면
        if (m == 0)
            continue;
        // 더 약한 플레이어가 있으면
        else {
            for (int j = 0; j < m; j++) {
                scanf("%d", &stronger);
                players[stronger - 1][i] = 1; // stronger player beats i [a][b] a beats b
            }
        }
    }

    // 데이터 판단
    int winner = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            visited[j] = 0; // 방문 초기화
        }
        dfs(i, n);

        int count = 0;
        for (int j = 0; j < n; j++) {
            if (visited[j])
                count++;
        }

        if (count == n)
            winner++;
    }

    printf("%d", winner);
}