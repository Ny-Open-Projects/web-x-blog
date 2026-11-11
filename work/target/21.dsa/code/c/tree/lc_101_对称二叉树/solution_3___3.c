/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135586474 */
/* LeetCode 101. 对称二叉树 — C 版（方案3） */
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

static int is_mirror(const TreeNode *l, const TreeNode *r) { // 定义判定函数 is_mirror
    if (!l && !r)
        return 1; // 若 取反 左指针 且 取反 右指针，直接返回 1
    if (!l || !r || l->val != r->val)
        return 0; // 若 取反 左指针 或 取反 右指针 或 左指针 减 超过 值 不等于 右指针 减 超过 值，直接返回 0
    return is_mirror(l->left, r->right) && is_mirror(r->left, l->right);
}
static int is_symmetric(const TreeNode *root) { // 定义判定函数 is_symmetric
    if (!root)
        return 1;                              // 若 取反 根节点，直接返回 1
    return is_mirror(root->left, root->right); // 返回 is_mirror(根节点 减 超过 左边界, 根节点 减 超过 右边界)
}
int main(void) {                                        // 程序入口：跑内嵌自测用例
    int v1[] = {1, 2, 2, 3, 4, 4, 3};                   // 把 {1,2,2,3,4,4,3}; 写入 int v1[]
    int v2[] = {1, 2, 2, INT_MIN_SN, 3, INT_MIN_SN, 3}; // 把 {1,2,2,INT_MIN_SN,3,INT_MIN_SN,3}; 写入 int v2[]
    if (!is_symmetric(NULL)) {
        printf("FAIL 0\n");
        return 1;
    } // 若 取反 is_symmetric(NULL)) { 输出「FAIL 0 」); return 1; }
    if (!is_symmetric(build_tree(v1, 7))) {
        printf("FAIL 1\n");
        return 1;
    }
    if (is_symmetric(build_tree(v2, 7))) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
