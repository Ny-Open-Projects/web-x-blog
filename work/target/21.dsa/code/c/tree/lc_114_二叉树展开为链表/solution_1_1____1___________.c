/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135637716 */
/* LeetCode 114. 二叉树展开为链表 — C 版（方案1） */
#include <stdio.h>                   // 引入头文件
#include <stdlib.h>                  // 引入头文件
#define INT_MIN_SN (-2147483647 - 1) // #define INT_MIN_SN ( 减 2147483647 减 1)

typedef struct TreeNode {   // typedef struct TreeNode {
    int val;                // int 值;
    struct TreeNode *left;  // 定义类型
    struct TreeNode *right; // 定义类型
} TreeNode;                 // } TreeNode;

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

static TreeNode *g_prev_114;          // static TreeNode 乘 g_prev_114;
static void dfs_114(TreeNode *node) { // 定义函数/方法 dfs_114
    if (!node)
        return;               // 若 取反 节点) return;
    dfs_114(node->right);     // dfs_114(节点 减 超过 右边界);
    dfs_114(node->left);      // dfs_114(节点 减 超过 左边界);
    node->right = g_prev_114; // 把 g_prev_114; 写入 node->right
    node->left = NULL;        // 把 NULL; 写入 node->left
    g_prev_114 = node;        // 把 节点; 写入 g_prev_114
}
static TreeNode *flatten(TreeNode *root) { // static TreeNode 乘 flatten(TreeNode 乘 根节点) {
    g_prev_114 = NULL;                     // 把 NULL; 写入 g_prev_114
    dfs_114(root);                         // dfs_114(根节点);
    return root;                           // 返回 根节点
}
static int chain(TreeNode *root, int out[]) { // 定义函数/方法 chain
    int cnt = 0;                              // 把 0 存入 计数
    while (root) {                            // 循环，直到不满足「根节点」
        if (root->left) {
            printf("FAIL left\n");
            exit(1);
        } // 若 根节点 减 超过 左边界) { 输出「FAIL 左边界 」); exit(1); }
        out[cnt++] = root->val; // 把 根节点 减 超过 值; 写入 out[cnt++]
        root = root->right;     // 把 根节点 减 超过 右边界; 写入 根节点
    }
    return cnt; // 返回 计数
}
int main(void) {                               // 程序入口：跑内嵌自测用例
    int v1[] = {1, 2, 5, 3, 4, INT_MIN_SN, 6}; // 把 {1,2,5,3,4,INT_MIN_SN,6}; 写入 int v1[]
    int w1[] = {1, 2, 3, 4, 5, 6};             // 把 {1,2,3,4,5,6}; 写入 int w1[]
    int out[64], n;                            // int out[64], 元素个数;
    TreeNode *t = flatten(build_tree(v1, 7));  // 把 flatten(build_tree(v1, 7)); 写入 TreeNode *t
    n = chain(t, out);                         // 把 chain(另一字符串, out); 写入 元素个数
    if (n != 6) {
        printf("FAIL len\n");
        return 1;
    } // 若 元素个数 不等于 6) { 输出「FAIL 长度 」); return 1; }
    for (int i = 0; i < 6; i++)
        if (out[i] != w1[i]) {
            printf("FAIL %d\n", i);
            return 1;
        }           // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
    int v2[] = {7}; // 把 {7}; 写入 int v2[]
    TreeNode *t2 = flatten(build_tree(v2, 1)); // 把 flatten(build_tree(v2, 1)); 写入 TreeNode *t2
    n = chain(t2, out);                        // 把 chain(t2, out); 写入 元素个数
    if (n != 1 || out[0] != 7) {
        printf("FAIL 2\n");
        return 1;
    } // 若 元素个数 不等于 1 或 out[0] 不等于 7) { 输出「FAIL 2 」); return 1; }
    if (flatten(NULL) != NULL) {
        printf("FAIL 3\n");
        return 1;
    }                 // 若 flatten(NULL) 不等于 NULL) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
