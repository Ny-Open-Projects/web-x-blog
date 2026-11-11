/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108013114
 * LeetCode 108013114. 贪心策略之BST&BBST_hashtable+dictionary+map — C 版（贪心策略之 BST/BBST/哈希表：Kruskal
 * 最小生成树（并查集 + 排序））
 */
#include <stdio.h> // 引入头文件

#define MAX_NODES 100 // #define MAX_NODES 100

static int parent[MAX_NODES + 1]; // static int parent[MAX_NODES 加 1];

static int find(int x) { // 定义函数/方法 find
    if (parent[x] == -1)
        parent[x] = x;                 // 若 parent[x] 等于 减 1) parent[x] 赋值为 x;
    while (parent[x] != x) {           // 循环，直到不满足「parent[x] 不等于 x」
        parent[x] = parent[parent[x]]; // 把 parent[parent[x]]; 写入 parent[x]
        x = parent[x];                 // 把 parent[x]; 写入 x
    }
    return x; // 返回 x
}

static int kruskal_mst(const int edges[][3], int n) { // 定义函数/方法 kruskal_mst
    /* 按权重的简单选择排序（保持稳定足够） */
    int idx[64]; // int idx[64];
    for (int i = 0; i < n; i++)
        idx[i] = i; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (int i = 0; i < n - 1; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 减 1 就继续
        for (int j = 0; j < n - 1 - i;
             j++) // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 减 1 减 下标 i 就继续
            if (edges[idx[j]][2] >
                edges[idx[j + 1]][2]) { // 若 边集[idx[下标 j]][2] 超过 边集[idx[下标 j 加 1]][2]
                int t = idx[j];
                idx[j] = idx[j + 1];
                idx[j + 1] = t;
            }
    for (int i = 0; i <= MAX_NODES; i++)
        parent[i] = -1;           // 让 下标 i 从 0 开始计数，下标 i 不超过 MAX_NODES 就继续
    int total = 0;                // 把 0 存入 总和
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        int u = edges[idx[i]][0], v = edges[idx[i]][1], w = edges[idx[i]][2];
        int ru = find(u), rv = find(v); // 把 find(节点 u), rv 赋值为 find(值) 存入 ru
        if (ru != rv) {                 // 若 ru 不等于 rv
            parent[ru] = rv;            // 把 rv; 写入 parent[ru]
            total += w;                 // 总和累加 权重
        }
    }
    return total; // 返回 总和
}

int main(void) { // 程序入口：跑内嵌自测用例
    int e0[5][3] = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};
    int e1[4][3] = {{0, 1, 1}, {1, 2, 2}, {2, 3, 3}, {3, 4, 4}};
    int e2[2][3] = {{0, 1, 2}, {1, 2, 3}};     // 把 {{0, 1, 2}, {1, 2, 3}}; 写入 int e2[2][3]
    int ws[4] = {19, 10, 5, 0};                // 把 {19, 10, 5, 0}; 写入 int ws[4]
    int ns[4] = {5, 4, 2, 0};                  // 把 {5, 4, 2, 0}; 写入 int ns[4]
    const int(*es[4])[3] = {e0, e1, e2, NULL}; // 把 {e0, e1, e2, NULL}; 写入 const int (*es[4])[3]
    for (int i = 0; i < 4; i++) {            // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
        int got = kruskal_mst(es[i], ns[i]); // 把 kruskal_mst(es[下标 i], ns[下标 i]) 存入 got
        if (got != ws[i]) {
            printf("case %d failed: got %d want %d\n", i, got, ws[i]);
            return 1;
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
