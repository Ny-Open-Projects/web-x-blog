/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108717090 */
/* 减治策略之详解Dijkstra算法 — C 版（方案1） */
#include <stdio.h> // 引入头文件
static void dijkstra_shortest(const int edges[][6], const int esizes[], int n, int start,
                              int out[]) { // 定义函数/方法 dijkstra_shortest
    int dist[64], visited[64] = {0};       // 把 {0}; 写入 int dist[64], visited[64]
    for (int i = 0; i < n; i++)
        dist[i] = 0x3f3f3f3f; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    dist[start] = 0;          // 把 0; 写入 dist[start]
    while (1) {               // 循环，直到不满足「1」
        int u = -1;           // 把 减 1 存入 节点 u
        for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
            if (!visited[i] && (u < 0 || dist[i] < dist[u]))
                u = i;
        }
        if (u < 0 || dist[u] == 0x3f3f3f3f)
            break;      // 若 节点 u 小于 0 或 dist[节点 u] 等于 0x3f3f3f3f) break;
        visited[u] = 1; // 把 1; 写入 visited[u]
        for (int i = 0; i < esizes[u]; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 esizes[节点 u] 就继续
            int v = edges[u][i * 2], w = edges[u][i * 2 + 1]; // 把 边集[节点 u][下标 i 乘 2], 权重 赋值为
                                                              // 边集[节点 u][下标 i 乘 2 加 1] 存入 值
            if (dist[u] + w < dist[v])
                dist[v] = dist[u] +
                          w; // 若 dist[节点 u] 加 权重 小于 dist[值]) dist[值] 赋值为 dist[节点 u] 加 权重;
        }
    }
    for (int i = 0; i < n; i++)
        out[i] = dist[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
}
int main(void) { // 程序入口：跑内嵌自测用例
    /* 5节点: 0->1(10),0->2(3),1->2(1),1->3(2),2->1(4),2->3(8),3->4(7) */
    static const int edges[5][6] = {{1, 10, 2, 3}, {2, 1, 3, 2}, {1, 4, 3, 8}, {4, 7}, {}};
    static const int esizes[5] = {2, 2, 2, 1, 0}; // 把 {2,2,2,1,0}; 写入 static const int esizes[5]
    int out[64];                                  // int out[64];
    dijkstra_shortest(edges, esizes, 5, 0, out);  // dijkstra_shortest(边集, esizes, 5, 0, out);
    int want[] = {0, 7, 3, 9, 16};                // 把 {0,7,3,9,16}; 写入 int want[]
    for (int i = 0; i < 5; i++)
        if (out[i] != want[i]) {
            printf("FAIL %d\n", i);
            return 1;
        } // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS