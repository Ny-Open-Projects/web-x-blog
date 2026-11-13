/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135170465 */
/* LeetCode 110. 平衡二叉树 — C 版（方案2） */
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

static int height(TreeNode *n) { // 定义函数/方法 height
    if (!n)
        return 0; // 若 取反 元素个数，直接返回 0
    int l = height(n->left), r = height(n->right);
    return (l > r ? l : r) + 1; // 返回 (左指针 超过 右指针 ? 左指针 : 右指针) 加 1
}
static int is_balanced(TreeNode *root) { // 定义判定函数 is_balanced
    if (!root)
        return 1; // 若 取反 根节点，直接返回 1
    int lh = height(root->left),
        rh = height(
            root->right); // 把 height(根节点 减 超过 左边界), rh 赋值为 height(根节点 减 超过 右边界) 存入 lh
    int d = lh - rh; // 把 lh 减 rh 存入 d
    if (d < 0)
        d = -d; // 若 d 小于 0) d 赋值为 减 d;
    if (d > 1)
        return 0; // 若 d 超过 1，直接返回 0
    return is_balanced(root->left) &&
           is_balanced(
               root->right); // 返回 is_balanced(根节点 减 超过 左边界) 且 is_balanced(根节点 减 超过 右边界)
}
int main(void) { // 程序入口：跑内嵌自测用例
    int v1[] = {3,          9,  20, INT_MIN_SN,
                INT_MIN_SN, 15, 7}; // 把 {3,9,20,INT_MIN_SN,INT_MIN_SN,15,7}; 写入 int v1[]
    int v2[] = {1,          2,          2, 3, 3,
                INT_MIN_SN, INT_MIN_SN, 4, 4}; // 把 {1,2,2,3,3,INT_MIN_SN,INT_MIN_SN,4,4}; 写入 int v2[]
    if (!is_balanced(build_tree(v1, 7))) {
        printf("FAIL 1\n");
        return 1;
    }
    if (is_balanced(build_tree(v2, 9))) {
        printf("FAIL 2\n");
        return 1;
    }
    if (!is_balanced(NULL)) {
        printf("FAIL 3\n");
        return 1;
    }                 // 若 取反 is_balanced(NULL)) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
