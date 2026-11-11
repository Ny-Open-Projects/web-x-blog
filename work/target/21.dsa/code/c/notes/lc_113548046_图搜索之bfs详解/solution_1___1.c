/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113548046 */
/* 图搜索之BFS详解 — C 版（方案1） */
#include <stdio.h> // 引入头文件
static void bfs_order(const int graph[][8], const int gsize[], int n, int start,
                      int out[]) {  // 定义函数/方法 bfs_order
    int visited[64] = {0};          // 把 {0}; 写入 int visited[64]
    int queue[64];                  // int 队列[64];
    int head = 0, tail = 0, on = 0; // 把 0, 尾节点 赋值为 0, on 赋值为 0 存入 头节点
    visited[start] = 1;             // 把 1; 写入 visited[start]
    queue[tail++] = start;          // 把 起点; 写入 queue[tail++]
    while (head < tail) {           // 循环，直到不满足「头节点 小于 尾节点」
        int c = queue[head++];      // 把 队列[头节点 加一 ] 存入 字符
        out[on++] = c;              // 把 字符; 写入 out[on++]
        for (int i = 0; i < gsize[c]; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 gsize[字符] 就继续
            int nx = graph[c][i];            // 把 graph[字符][下标 i] 存入 nx
            if (!visited[nx]) {              // 若 取反 已访问集合[nx]
                visited[nx] = 1;             // 把 1; 写入 visited[nx]
                queue[tail++] = nx; // 把 nx; 写入 queue[tail++]
            }
        }
    }
}
int main(void) { // 程序入口：跑内嵌自测用例
    int graph[6][8] = {{1, 2}, {3, 4}, {5},
                       {},     {},     {}}; // 把 {{1,2},{3,4},{5},{},{},{}}; 写入 int graph[6][8]
    int gsize[6] = {2, 2, 1, 0, 0, 0};      // 把 {2,2,1,0,0,0}; 写入 int gsize[6]
    int out[64];                            // int out[64];
    bfs_order(graph, gsize, 6, 0, out);     // bfs_order(graph, gsize, 6, 0, out);
    for (int i = 0; i < 6; i++)
        if (out[i] != i) {
            printf("FAIL\n");
            return 1;
        } // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS