/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133472893 */
/* LeetCode 787. K站中转内最便宜的航班 — C 版（方案5） */
#include <stdio.h>     // 引入头文件
#define INF 0x3f3f3f3f // #define INF 0x3f3f3f3f
static int find_cheapest_price(int n, int flights[][3], int nf, int src, int dst,
                               int k) { // 定义函数/方法 find_cheapest_price
    int dist[128];                      // int dist[128];
    for (int i = 0; i < n; i++)
        dist[i] = INF; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    dist[src] = 0;     // 把 0; 写入 dist[src]
    for (int t = 0; t <= k; t++) { // 让 另一字符串 从 0 开始计数，另一字符串 不超过 下标 k 就继续
        int nd[128];               // int nd[128];
        for (int i = 0; i < n; i++)
            nd[i] = dist[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (int i = 0; i < nf; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 nf 就继续
            int u = flights[i][0], v = flights[i][1], w = flights[i][2];
            if (dist[u] != INF && dist[u] + w < nd[v])
                nd[v] = dist[u] + w;
        }
        for (int i = 0; i < n; i++)
            dist[i] = nd[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    }
    return dist[dst] == INF ? -1 : dist[dst]; // 返回 dist[dst] 等于 INF ? 减 1 : dist[dst]
}
int main(void) { // 程序入口：跑内嵌自测用例
    int f[][3] = {{0, 1, 100}, {1, 2, 100}, {2, 0, 100}, {1, 3, 600}, {2, 3, 200}};
    if (find_cheapest_price(4, f, 5, 0, 3, 1) != 700) {
        printf("FAIL 1\n");
        return 1;
    }
    if (find_cheapest_price(4, f, 5, 0, 0, 1) != 0) {
        printf("FAIL 2\n");
        return 1;
    }
    if (find_cheapest_price(4, f, 5, 0, 3, 2) != 400) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS