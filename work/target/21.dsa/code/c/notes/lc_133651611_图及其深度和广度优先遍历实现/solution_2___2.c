/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133651611
 * LeetCode 133651611. 图及其深度和广度优先遍历实现 — C 版（方案2）
 * 邻接表（保持插入序），最大 16 节点每点 8 邻居
 */
#include <stdio.h> // 引入头文件

#define MAXV 16  // #define MAXV 16
#define MAXDEG 8 // #define MAXDEG 8

typedef struct {           // typedef struct {
    int adj[MAXV][MAXDEG]; // int 邻接表[MAXV][MAXDEG];
    int deg[MAXV];         // int deg[MAXV];
} Graph;                   // } Graph;

static void graph_init(Graph *g) { // 定义函数/方法 graph_init
    for (int i = 0; i < MAXV; i++)
        g->deg[i] = 0; // 让 下标 i 从 0 开始计数，下标 i 小于 MAXV 就继续
}

static void add_edge(Graph *g, int from, int to) { // 定义函数/方法 add_edge
    g->adj[from][g->deg[from]++] = to;             // 把 to; 写入 g->adj[from][g->deg[from]++]
    g->adj[to][g->deg[to]++] = from;               // 把 from; 写入 g->adj[to][g->deg[to]++]
}

static int visited[MAXV]; // static int 已访问集合[MAXV];
static int result[MAXV];  // static int 结果[MAXV];
static int result_len;    // static int result_len;

static void dfs_helper(const Graph *g, int node) { // 定义函数/方法 dfs_helper
    if (visited[node])
        return;                  // 若 已访问集合[节点]) return;
    visited[node] = 1;           // 把 1; 写入 visited[node]
    result[result_len++] = node; // 把 节点; 写入 result[result_len++]
    for (int i = 0; i < g->deg[node];
         i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 g 减 超过 deg[节点] 就继续
        dfs_helper(g, g->adj[node][i]); // dfs_helper(g, g 减 超过 邻接表[节点][下标 i]);
    }
}

static int dfs(const Graph *g, int start, int out[]) { // 定义函数/方法 dfs
    for (int i = 0; i < MAXV; i++)
        visited[i] = 0;   // 让 下标 i 从 0 开始计数，下标 i 小于 MAXV 就继续
    result_len = 0;       // 把 0; 写入 result_len
    dfs_helper(g, start); // dfs_helper(g, 起点);
    for (int i = 0; i < result_len; i++)
        out[i] = result[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 result_len 就继续
    return result_len;      // 返回 result_len
}

static int bfs(const Graph *g, int start, int out[]) { // 定义函数/方法 bfs
    for (int i = 0; i < MAXV; i++)
        visited[i] = 0;                  // 让 下标 i 从 0 开始计数，下标 i 小于 MAXV 就继续
    int queue[MAXV], head = 0, tail = 0; // 把 0, 尾节点 赋值为 0; 写入 int queue[MAXV], head
    int len = 0;                         // 把 0 存入 长度
    queue[tail++] = start;               // 把 起点; 写入 queue[tail++]
    visited[start] = 1;                  // 把 1; 写入 visited[start]
    while (head < tail) {                // 循环，直到不满足「头节点 小于 尾节点」
        int node = queue[head++];        // 把 队列[头节点 加一 ] 存入 节点
        out[len++] = node;               // 把 节点; 写入 out[len++]
        for (int i = 0; i < g->deg[node];
             i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 g 减 超过 deg[节点] 就继续
            int nb = g->adj[node][i]; // 把 g 减 超过 邻接表[节点][下标 i] 存入 nb
            if (!visited[nb]) {       // 若 取反 已访问集合[nb]
                visited[nb] = 1;      // 把 1; 写入 visited[nb]
                queue[tail++] = nb;   // 把 nb; 写入 queue[tail++]
            }
        }
    }
    return len; // 返回 长度
}

static int eq(const int *a, const int *b, int n) { // 定义函数/方法 eq
    for (int i = 0; i < n; i++)
        if (a[i] != b[i])
            return 0; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    return 1;         // 返回 1
}

int main(void) { // 程序入口：跑内嵌自测用例
    /* case 1: 方形图 0-1-3-2-0 */
    Graph g1;            // Graph g1;
    graph_init(&g1);     // graph_init( 按位与 g1);
    add_edge(&g1, 0, 1); // add_edge( 按位与 g1, 0, 1);
    add_edge(&g1, 0, 2); // add_edge( 按位与 g1, 0, 2);
    add_edge(&g1, 1, 3); // add_edge( 按位与 g1, 1, 3);
    add_edge(&g1, 2, 3); // add_edge( 按位与 g1, 2, 3);

    int got[8];  // int got[8];
    int want[4]; // int want[4];

    want[0] = 0;
    want[1] = 1;
    want[2] = 3;
    want[3] = 2; // 把 0; want[1] 赋值为 1; want[2] 赋值为 3; want[3] 赋值为 2; 写入 want[0]
    if (dfs(&g1, 0, got) != 4 || !eq(got, want, 4)) {
        printf("case1 dfs(0) failed\n");
        return 1;
    }
    want[0] = 0;
    want[1] = 1;
    want[2] = 2;
    want[3] = 3; // 把 0; want[1] 赋值为 1; want[2] 赋值为 2; want[3] 赋值为 3; 写入 want[0]
    if (bfs(&g1, 0, got) != 4 || !eq(got, want, 4)) {
        printf("case1 bfs(0) failed\n");
        return 1;
    }

    /* case 2: 从另一节点出发 */
    want[0] = 2;
    want[1] = 0;
    want[2] = 1;
    want[3] = 3; // 把 2; want[1] 赋值为 0; want[2] 赋值为 1; want[3] 赋值为 3; 写入 want[0]
    if (dfs(&g1, 2, got) != 4 || !eq(got, want, 4)) {
        printf("case2 dfs(2) failed\n");
        return 1;
    }
    want[0] = 2;
    want[1] = 0;
    want[2] = 3;
    want[3] = 1; // 把 2; want[1] 赋值为 0; want[2] 赋值为 3; want[3] 赋值为 1; 写入 want[0]
    if (bfs(&g1, 2, got) != 4 || !eq(got, want, 4)) {
        printf("case2 bfs(2) failed\n");
        return 1;
    }

    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
