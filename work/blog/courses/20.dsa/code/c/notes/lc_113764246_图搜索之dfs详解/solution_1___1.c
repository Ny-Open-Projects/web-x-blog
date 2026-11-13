/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113764246 */
/* 图搜索之DFS详解 — C 版（方案1） */
#include <stdio.h>                         // 引入头文件
static int visited_g[64];                  // static int visited_g[64];
static int order_g[64];                    // static int order_g[64];
static int on_g;                           // static int on_g;
static const int (*graph_g)[8];            // static const int ( 乘 graph_g)[8];
static const int *gsize_g;                 // static const int 乘 gsize_g;
static void go(int c) {                    // 定义函数/方法 go
    visited_g[c] = 1;                      // 把 1; 写入 visited_g[c]
    order_g[on_g++] = c;                   // 把 字符; 写入 order_g[on_g++]
    for (int i = 0; i < gsize_g[c]; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 gsize_g[字符] 就继续
        if (!visited_g[graph_g[c][i]])
            go(graph_g[c][i]); // 若 取反 visited_g[graph_g[字符][下标 i]]) go(graph_g[字符][下标 i]);
    }
}
int main(void) { // 程序入口：跑内嵌自测用例
    static const int graph[6][8] = {{1, 2}, {3, 4}, {5}, {}, {}, {}};
    static const int gsize[6] = {2, 2, 1, 0, 0, 0}; // 把 {2,2,1,0,0,0}; 写入 static const int gsize[6]
    graph_g = graph;                                // 把 graph; 写入 graph_g
    gsize_g = gsize;                                // 把 gsize; 写入 gsize_g
    go(0);                                          // go(0);
    int want[] = {0, 1, 3, 4, 2, 5};                // 把 {0,1,3,4,2,5}; 写入 int want[]
    for (int i = 0; i < 6; i++)
        if (order_g[i] != want[i]) {
            printf("FAIL\n");
            return 1;
        } // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS