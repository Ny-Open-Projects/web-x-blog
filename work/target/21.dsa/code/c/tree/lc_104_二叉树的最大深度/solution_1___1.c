/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
 * LeetCode 104. 二叉树的最大深度 — C 版 */
#include <limits.h> // 引入头文件
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件

#define INT_MIN_SENTINEL INT_MIN // #define INT_MIN_SENTINEL INT_MIN

typedef struct TreeNode {   // typedef struct TreeNode {
    int val;                // int 值;
    struct TreeNode *left;  // 定义类型
    struct TreeNode *right; // 定义类型
} TreeNode;                 // } TreeNode;

/* 层序数组构建二叉树，null 用 INT_MIN 哨兵表示 */
TreeNode *build_tree(int *vals, int n) { // TreeNode 乘 build_tree(int 乘 vals, int 元素个数) {
    if (n == 0 || vals[0] == INT_MIN_SENTINEL)
        return NULL; // 若 元素个数 等于 0 或 vals[0] 等于 INT_MIN_SENTINEL，直接返回 NULL
    TreeNode *root = malloc(sizeof(TreeNode)); // 把 malloc(sizeof(TreeNode)); 写入 TreeNode *root
    root->val = vals[0];
    root->left = root->right = NULL;
    TreeNode **queue =
        malloc(sizeof(TreeNode *) * n); // 把 malloc(sizeof(TreeNode 乘 ) 乘 元素个数); 写入 TreeNode **queue
    int head = 0, tail = 0, i = 1; // 把 0, 尾节点 赋值为 0, 下标 i 赋值为 1 存入 头节点
    queue[tail++] = root;          // 把 根节点; 写入 queue[tail++]
    while (head < tail && i < n) { // 循环，直到不满足「头节点 小于 尾节点 且 下标 i 小于 元素个数」
        TreeNode *node = queue[head++];                // 把 队列[头节点 加一 ]; 写入 TreeNode *node
        if (i < n) {                                   // 若 下标 i 小于 元素个数
            if (vals[i] != INT_MIN_SENTINEL) {         // 若 vals[下标 i] 不等于 INT_MIN_SENTINEL
                node->left = malloc(sizeof(TreeNode)); // 把 malloc(sizeof(TreeNode)); 写入 node->left
                node->left->val = vals[i];
                node->left->left = node->left->right = NULL;
                queue[tail++] = node->left; // 把 节点 减 超过 左边界; 写入 queue[tail++]
            }
            i++; // 下标 i 加一
        }
        if (i < n) {                                    // 若 下标 i 小于 元素个数
            if (vals[i] != INT_MIN_SENTINEL) {          // 若 vals[下标 i] 不等于 INT_MIN_SENTINEL
                node->right = malloc(sizeof(TreeNode)); // 把 malloc(sizeof(TreeNode)); 写入 node->right
                node->right->val = vals[i];
                node->right->left = node->right->right = NULL;
                queue[tail++] = node->right; // 把 节点 减 超过 右边界; 写入 queue[tail++]
            }
            i++; // 下标 i 加一
        }
    }
    free(queue); // free(队列);
    return root; // 返回 根节点
}

void free_tree(TreeNode *n) { // 定义函数/方法 free_tree
    if (!n)
        return;          // 若 取反 元素个数) return;
    free_tree(n->left);  // free_tree(元素个数 减 超过 左边界);
    free_tree(n->right); // free_tree(元素个数 减 超过 右边界);
    free(n);             // free(元素个数);
}

/* 主解法：DFS，叶子节点时刷新最大深度（与 blog 方案1一致） */
void dfs(TreeNode *n, int l, int *dep) { // 定义函数/方法 dfs
    if (!n)
        return;                  // 若 取反 元素个数) return;
    if (!n->left && !n->right) { // 若 取反 元素个数 减 超过 左边界 且 取反 元素个数 减 超过 右边界
        if (l > *dep)
            *dep = l; // 若 左指针 超过 乘 dep) 乘 dep 赋值为 左指针;
    }
    dfs(n->left, l + 1, dep);  // dfs(元素个数 减 超过 左边界, 左指针 加 1, dep);
    dfs(n->right, l + 1, dep); // dfs(元素个数 减 超过 右边界, 左指针 加 1, dep);
}

int max_depth(TreeNode *root) { // 定义函数/方法 max_depth
    int dep = 0;                // 把 0 存入 dep
    dfs(root, 1, &dep);         // dfs(根节点, 1, 按位与 dep);
    return dep;                 // 返回 dep
}

int main(void) { // 程序入口：跑内嵌自测用例
    struct {
        int vals[8];
        int n;
        int want;
    } tests[] = {
        // 把 { 写入 struct { int vals[8]; int n; int want; } tests[]
        {{0}, 0, 0},
        {{1}, 1, 1},
        {{3, 9, 20, INT_MIN_SENTINEL, INT_MIN_SENTINEL, 15, 7}, 7, 3},
        {{1, INT_MIN_SENTINEL, 2, INT_MIN_SENTINEL, 3}, 5, 3},
    };
    for (int idx = 0; idx < 4; idx++) { // 让 idx 从 0 开始计数，idx 小于 4 就继续
        TreeNode *t = build_tree(tests[idx].vals, tests[idx].n);
        int got = max_depth(t);       // 把 max_depth(另一字符串) 存入 got
        if (got != tests[idx].want) { // 若 got 不等于 tests[idx].want
            printf("case %d failed: got %d want %d\n", idx, got, tests[idx].want); // 打印输出
            return 1;                                                              // 返回 1
        }
        free_tree(t); // free_tree(另一字符串);
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
