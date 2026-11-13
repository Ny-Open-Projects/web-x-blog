/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137409838 */
/* LeetCode 572. 另一棵树的子树 — C 版（方案2） */
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
static int same_tree(const TreeNode *p, const TreeNode *q) { // 定义函数/方法 same_tree
    if (!p && !q)
        return 1; // 若 取反 节点 且 取反 节点，直接返回 1
    if (!p || !q || p->val != q->val)
        return 0; // 若 取反 节点 或 取反 节点 或 节点 减 超过 值 不等于 节点 减 超过 值，直接返回 0
    return same_tree(p->left, q->left) && same_tree(p->right, q->right);
}

static int check(const TreeNode *a, const TreeNode *b) { // 定义判定函数 check
    if (!a && !b)
        return 1; // 若 取反 数组 且 取反 b，直接返回 1
    if (!a || !b || a->val != b->val)
        return 0; // 若 取反 数组 或 取反 b 或 数组 减 超过 值 不等于 b 减 超过 值，直接返回 0
    return check(a->left, b->left) && check(a->right, b->right);
}
static int is_subtree(const TreeNode *root, const TreeNode *sub) { // 定义判定函数 is_subtree
    if (!root)
        return 0; // 若 取反 根节点，直接返回 0
    return check(root, sub) || is_subtree(root->left, sub) || is_subtree(root->right, sub);
}
int main(void) {                                 // 程序入口：跑内嵌自测用例
    int a1[] = {3, 4, 5, 1, 2}, b[] = {4, 1, 2}; // 把 {3,4,5,1,2}, b[] 赋值为 {4,1,2}; 写入 int a1[]
    int a2[] = {3, 4, 5, 1, 2, INT_MIN_SN, INT_MIN_SN, INT_MIN_SN, INT_MIN_SN, 0};
    if (!is_subtree(build_tree(a1, 5), build_tree(b, 3))) {
        printf("FAIL 1\n");
        return 1;
    }
    if (is_subtree(build_tree(a2, 10), build_tree(b, 3))) {
        printf("FAIL 2\n");
        return 1;
    }
    if (is_subtree(NULL, NULL)) {
        printf("FAIL 3\n");
        return 1;
    }                 // 若 is_subtree(NULL, NULL)) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
