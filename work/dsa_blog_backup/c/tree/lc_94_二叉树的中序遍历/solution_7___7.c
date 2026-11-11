/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134915904 */
/* LeetCode 94. 二叉树的中序遍历 — C 版（方案7） */
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

static void dfs_in(TreeNode *n, int *out, int *cnt) { // 定义函数/方法 dfs_in
    if (!n)
        return;                 // 若 取反 元素个数) return;
    dfs_in(n->left, out, cnt);  // dfs_in(元素个数 减 超过 左边界, out, 计数);
    out[(*cnt)++] = n->val;     // 把 元素个数 减 超过 值; 写入 out[(*cnt)++]
    dfs_in(n->right, out, cnt); // dfs_in(元素个数 减 超过 右边界, out, 计数);
}
static int inorder_traversal(TreeNode *root, int out[]) { // 定义函数/方法 inorder_traversal
    int cnt = 0;                                          // 把 0 存入 计数
    dfs_in(root, out, &cnt);                              // dfs_in(根节点, out, 按位与 计数);
    return cnt;                                           // 返回 计数
}
static int eqarr(const int *a, int n, const int *b, int m) { // 定义函数/方法 eqarr
    if (n != m)
        return 0; // 若 元素个数 不等于 映射表，直接返回 0
    for (int i = 0; i < n; i++)
        if (a[i] != b[i])
            return 0; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    return 1;         // 返回 1
}
int main(void) {                                  // 程序入口：跑内嵌自测用例
    int out[64], n;                               // int out[64], 元素个数;
    int w2[] = {1, 2, 3}, w3[] = {2, 1, 3};       // 把 {1,2,3}, w3[] 赋值为 {2,1,3}; 写入 int w2[]
    int v2[] = {1, INT_MIN_SN, 2, INT_MIN_SN, 3}; // 把 {1,INT_MIN_SN,2,INT_MIN_SN,3}; 写入 int v2[]
    int v3[] = {1, 2, 3};                         // 把 {1,2,3}; 写入 int v3[]
    if (inorder_traversal(NULL, out) != 0) {
        printf("FAIL 0\n");
        return 1;
    }
    n = inorder_traversal(build_tree(v2, 5),
                          out); // 把 inorder_traversal(build_tree(v2, 5), out); 写入 元素个数
    if (!eqarr(out, n, w2, 3)) {
        printf("FAIL 1\n");
        return 1;
    } // 若 取反 eqarr(out, 元素个数, w2, 3)) { 输出「FAIL 1 」); return 1; }
    n = inorder_traversal(build_tree(v3, 3),
                          out); // 把 inorder_traversal(build_tree(v3, 3), out); 写入 元素个数
    if (!eqarr(out, n, w3, 3)) {
        printf("FAIL 2\n");
        return 1;
    }                 // 若 取反 eqarr(out, 元素个数, w3, 3)) { 输出「FAIL 2 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
