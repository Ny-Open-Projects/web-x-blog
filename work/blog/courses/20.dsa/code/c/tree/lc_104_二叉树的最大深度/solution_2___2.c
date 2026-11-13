// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
// LeetCode 104. 二叉树的最大深度 — C 版（方案2：分治递归 1+max(左深,右深) — python 风格自测）
// 注：辅助函数在 C 版以打印形式呈现（返回结构见 Rust/C++/Dart/Lua/R 版）
#include <stdio.h>                   // 引入头文件
#include <stdlib.h>                  // 引入头文件
#include <string.h>                  // 引入头文件
#define INT_MIN_SN (-2147483647 - 1) // #define INT_MIN_SN ( 减 2147483647 减 1)
typedef struct TreeNode {            // typedef struct TreeNode {
    int val;                         // int 值;
    struct TreeNode *left;           // 定义类型
    struct TreeNode *right;          // 定义类型
} TreeNode;                          // } TreeNode;
static TreeNode *build_tree(const int *vals,
                            int n) { // static TreeNode 乘 build_tree(const int 乘 vals, int 元素个数) {
    if (n == 0 || vals[0] == INT_MIN_SN)
        return NULL; // 若 元素个数 等于 0 或 vals[0] 等于 INT_MIN_SN，直接返回 NULL
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
            if (vals[i] != INT_MIN_SN) {               // 若 vals[下标 i] 不等于 INT_MIN_SN
                node->left = malloc(sizeof(TreeNode)); // 把 malloc(sizeof(TreeNode)); 写入 node->left
                node->left->val = vals[i];
                node->left->left = node->left->right = NULL;
                queue[tail++] = node->left; // 把 节点 减 超过 左边界; 写入 queue[tail++]
            }
            i++; // 下标 i 加一
        }
        if (i < n) {                                    // 若 下标 i 小于 元素个数
            if (vals[i] != INT_MIN_SN) {                // 若 vals[下标 i] 不等于 INT_MIN_SN
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
static void free_tree(TreeNode *n) { // 定义函数/方法 free_tree
    if (!n)
        return;          // 若 取反 元素个数) return;
    free_tree(n->left);  // free_tree(元素个数 减 超过 左边界);
    free_tree(n->right); // free_tree(元素个数 减 超过 右边界);
    free(n);             // free(元素个数);
}

// 主解法：分治递归，深度 = 1 + max(左子树深度, 右子树深度)
int max_depth(TreeNode *root) { // 定义函数/方法 max_depth
    if (!root)
        return 0;                   // 若 取反 根节点，直接返回 0
    int l = max_depth(root->left);  // 把 max_depth(根节点 减 超过 左边界) 存入 左指针
    int r = max_depth(root->right); // 把 max_depth(根节点 减 超过 右边界) 存入 右指针
    return 1 + (l > r ? l : r);     // 返回 1 加 (左指针 超过 右指针 ? 左指针 : 右指针)
}

int main(void) { // 程序入口：跑内嵌自测用例
    struct {
        int vals[5];
        int n;
        int want;
    } tests[] = {
        // 把 { 写入 struct { int vals[5]; int n; int want; } tests[]
        {{INT_MIN_SN}, 0, 0},
        {{1, 2, 3, 4, 5}, 5, 3},
    };
    for (int idx = 0; idx < 2; idx++) { // 让 idx 从 0 开始计数，idx 小于 2 就继续
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
