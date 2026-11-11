/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133986698
 * LeetCode 133. 克隆图 — C 版 */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件

#define MAX_NODES 101 // #define MAX_NODES 101
#define MAX_DEGREE 16 // #define MAX_DEGREE 16

typedef struct GNode {                   // typedef struct GNode {
    int val;                             // int 值;
    struct GNode *neighbors[MAX_DEGREE]; // 定义类型
    int ncount;                          // int ncount;
} GNode;                                 // } GNode;

static GNode *new_node(int val) {              // static GNode 乘 new_node(int 值) {
    GNode *n = (GNode *)malloc(sizeof(GNode)); // 把 (GNode 乘 )malloc(sizeof(GNode)); 写入 GNode *n
    n->val = val;                              // 把 值; 写入 n->val
    n->ncount = 0;                             // 把 0; 写入 n->ncount
    return n;                                  // 返回 元素个数
}

/* visited：数组模拟 Map<Node*, Node*>（指针线性查找，测试规模小） */
typedef struct {            // typedef struct {
    GNode *orig[MAX_NODES]; // GNode 乘 orig[MAX_NODES];
    GNode *copy[MAX_NODES]; // GNode 乘 copy[MAX_NODES];
    int len;                // int 长度;
} VMap;                     // } VMap;

static GNode *vmap_get(const VMap *vm,
                       GNode *orig) { // static GNode 乘 vmap_get(const VMap 乘 vm, GNode 乘 orig) {
    for (int i = 0; i < vm->len; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 vm 减 超过 长度 就继续
        if (vm->orig[i] == orig)
            return vm->copy[i]; // 若 vm 减 超过 orig[下标 i] 等于 orig，直接返回 vm 减 超过 copy[下标 i]
    return NULL;                // 返回 NULL
}

static void vmap_put(VMap *vm, GNode *orig, GNode *copy) { // 定义函数/方法 vmap_put
    vm->orig[vm->len] = orig;                              // 把 orig; 写入 vm->orig[vm->len]
    vm->copy[vm->len] = copy;                              // 把 copy; 写入 vm->copy[vm->len]
    vm->len++;                                             // vm 减 超过 长度 加一 ;
}

/* 方案2（DFS 递归，visited 以节点对象为键） */
static GNode *dfs(GNode *n, VMap *visited) { // static GNode 乘 dfs(GNode 乘 元素个数, VMap 乘 已访问集合) {
    GNode *hit = vmap_get(visited, n); // 把 vmap_get(已访问集合, 元素个数); 写入 GNode *hit
    if (hit != NULL)
        return hit;                  // 若 hit 不等于 NULL，直接返回 hit
    GNode *clone = new_node(n->val); // 把 new_node(元素个数 减 超过 值); 写入 GNode *clone
    vmap_put(visited, n, clone);     // vmap_put(已访问集合, 元素个数, clone);
    for (int i = 0; i < n->ncount;
         i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 减 超过 ncount 就继续
        clone->neighbors[clone->ncount++] = dfs(n->neighbors[i], visited);
    }
    return clone; // 返回 clone
}

static GNode *clone_graph(GNode *node) { // static GNode 乘 clone_graph(GNode 乘 节点) {
    if (node == NULL)
        return NULL;            // 若 节点 等于 NULL，直接返回 NULL
    VMap visited = {0};         // 把 {0}; 写入 VMap visited
    return dfs(node, &visited); // 返回 dfs(节点, 按位与 已访问集合)
}

typedef struct {          // typedef struct {
    int len;              // int 长度;
    int vals[MAX_DEGREE]; // int vals[MAX_DEGREE];
} Row;                    // } Row;

static GNode *build_graph(const Row *adj,
                          int n) { // static GNode 乘 build_graph(const Row 乘 邻接表, int 元素个数) {
    GNode *nodes[MAX_NODES] = {0}; // 把 {0}; 写入 GNode *nodes[MAX_NODES]
    for (int i = 1; i <= n; i++)
        nodes[i] = new_node(i); // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
    for (int idx = 1; idx <= n; idx++) { // 让 idx 从 1 开始计数，idx 不超过 元素个数 就继续
        for (int k = 0; k < adj[idx - 1].len;
             k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 邻接表[idx 减 1].长度 就继续
            nodes[idx]
                ->neighbors[nodes[idx]->ncount++] = // 把  写入 nodes[idx]->neighbors[nodes[idx]->ncount++]
                nodes[adj[idx - 1].vals[k]];        // nodes[邻接表[idx 减 1].vals[下标 k]];
        }
    }
    return nodes[1]; // 返回 nodes[1]
}

/* 收集签名：每个节点的邻居值列表（排序后），按节点 val 索引 */
typedef struct {                   // typedef struct {
    int count; /* -1 表示未访问 */ // int 计数; 除以 乘 减 1 表示未访问 乘 除以
    int vals[MAX_DEGREE];          // int vals[MAX_DEGREE];
} Sig;                             // } Sig;

static void signature(GNode *node, Sig vis[]) { // 定义函数/方法 signature
    vis[node->val].count = node->ncount;        // 把 节点 减 超过 ncount; 写入 计数
    for (int i = 0; i < node->ncount; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 节点 减 超过 ncount 就继续
        vis[node->val].vals[i] =
            node->neighbors[i]
                ->val; // 把 节点 减 超过 neighbors[下标 i] 减 超过 值; 写入 vis[node->val].vals[i]
    /* 插入排序 */
    for (int i = 1; i < vis[node->val].count;
         i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 vis[节点 减 超过 值].计数 就继续
        int key = vis[node->val].vals[i]; // 把 vis[节点 减 超过 值].vals[下标 i] 存入 key
        int j = i - 1;                    // 把 下标 i 减 1 存入 下标 j
        while (j >= 0 &&
               vis[node->val].vals[j] >
                   key) { // 循环，直到不满足「下标 j 不低于 0 且 vis[节点 减 超过 值].vals[下标 j] 超过 key」
            vis[node->val].vals[j + 1] =
                vis[node->val]
                    .vals[j]; // 把 vis[节点 减 超过 值].vals[下标 j]; 写入 vis[node->val].vals[j + 1]
            j--;              // 下标 j 减一
        }
        vis[node->val].vals[j + 1] = key; // 把 key; 写入 vis[node->val].vals[j + 1]
    }
    for (int i = 0; i < node->ncount; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 节点 减 超过 ncount 就继续
        if (vis[node->neighbors[i]->val].count ==
            -1) // 若 vis[节点 减 超过 neighbors[下标 i] 减 超过 值].计数 等于 减 1
            signature(node->neighbors[i], vis); // signature(节点 减 超过 neighbors[下标 i], vis);
}

static void free_graph(GNode *node) { // 定义函数/方法 free_graph
    if (node == NULL)
        return; // 若 节点 等于 NULL) return;
    /* 先 BFS 收集全部节点（入队时标记），再统一释放，避免解引用已释放节点 */
    char seen[MAX_NODES] = {0};   // 把 {0}; 写入 char seen[MAX_NODES]
    GNode *order[MAX_NODES];      // GNode 乘 order[MAX_NODES];
    int cnt = 0, head = 0;        // 把 0, 头节点 赋值为 0 存入 计数
    seen[node->val] = 1;          // 把 1; 写入 seen[node->val]
    order[cnt++] = node;          // 把 节点; 写入 order[cnt++]
    while (head < cnt) {          // 循环，直到不满足「头节点 小于 计数」
        GNode *n = order[head++]; // 把 order[头节点 加一 ]; 写入 GNode *n
        for (int i = 0; i < n->ncount;
             i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 减 超过 ncount 就继续
            GNode *nb = n->neighbors[i]; // 把 元素个数 减 超过 neighbors[下标 i]; 写入 GNode *nb
            if (!seen[nb->val]) {        // 若 取反 已见集合[nb 减 超过 值]
                seen[nb->val] = 1;       // 把 1; 写入 seen[nb->val]
                order[cnt++] = nb;       // 把 nb; 写入 order[cnt++]
            }
        }
    }
    for (int i = 0; i < cnt; i++)
        free(order[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 计数 就继续
}

int main(void) { // 程序入口：跑内嵌自测用例
    Row adj[4] = {{2, {2, 4}}, {2, {1, 3}}, {2, {2, 4}}, {2, {1, 3}}};
    GNode *root = build_graph(adj, 4);        // 把 build_graph(邻接表, 4); 写入 GNode *root
    GNode *cloned = clone_graph(root);        // 把 clone_graph(根节点); 写入 GNode *cloned
    if (cloned == NULL) {                     // 若 cloned 等于 NULL
        printf("cloneGraph returned null\n"); // 打印输出
        return 1;                             // 返回 1
    }
    if (cloned == root) {                          // 若 cloned 等于 根节点
        printf("not a deep copy (same object)\n"); // 打印输出
        return 1;                                  // 返回 1
    }
    Sig vis[MAX_NODES]; // Sig vis[MAX_NODES];
    for (int i = 0; i < MAX_NODES; i++)
        vis[i].count = -1;  // 让 下标 i 从 0 开始计数，下标 i 小于 MAX_NODES 就继续
    signature(cloned, vis); // signature(cloned, vis);
    Row expected[4] = {{2, {2, 4}}, {2, {1, 3}}, {2, {2, 4}}, {2, {1, 3}}};
    for (int k = 1; k <= 4; k++) { // 让 下标 k 从 1 开始计数，下标 k 不超过 4 就继续
        if (vis[k].count != expected[k - 1].len) { // 若 vis[下标 k].计数 不等于 expected[下标 k 减 1].长度
            printf("signature mismatch at %d\n", k); // 打印输出
            return 1;                                // 返回 1
        }
        for (int i = 0; i < expected[k - 1].len;
             i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 expected[下标 k 减 1].长度 就继续
            if (vis[k].vals[i] !=
                expected[k - 1]
                    .vals[i]) { // 若 vis[下标 k].vals[下标 i] 不等于 expected[下标 k 减 1].vals[下标 i]
                printf("signature mismatch at %d\n", k); // 打印输出
                return 1;                                // 返回 1
            }
        }
    }
    free_graph(cloned); // free_graph(cloned);
    free_graph(root);   // free_graph(根节点);
    printf("PASS\n");   // 全部用例通过，输出 PASS
    return 0;           // 返回 0
}
