/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136528287 */
/* LeetCode 236. 二叉树的最近公共祖先 — C 版（方案1） */
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

static int lca(TreeNode *n, int p, int q, int *found) { // 定义函数/方法 lca
    if (!n)
        return -1; // 若 取反 元素个数，直接返回 减 1
    if (n->val == p || n->val == q) {
        (*found)++;
        return n->val;
    }
    int f_before = *found; // 把 乘 found 存入 f_before
    int l = lca(n->left, p, q, found); // 把 lca(元素个数 减 超过 左边界, 节点, 节点, found) 存入 左指针
    int r = lca(n->right, p, q, found); // 把 lca(元素个数 减 超过 右边界, 节点, 节点, found) 存入 右指针
    if (*found >= 2) {                  // 若 乘 found 不低于 2
        if (l != -1 && r != -1)
            return n->val; // 若 左指针 不等于 减 1 且 右指针 不等于 减 1，直接返回 元素个数 减 超过 值
        return (l != -1) ? l : r; // 返回 (左指针 不等于 减 1) ? 左指针 : 右指针
    }
    if (*found > f_before)
        return (l != -1) ? l
                         : r; // 若 乘 found 超过 f_before，直接返回 (左指针 不等于 减 1) ? 左指针 : 右指针
    return -1; // 返回 减 1
}
static int lowest_common_ancestor(TreeNode *root, int p, int q) { // 定义函数/方法 lowest_common_ancestor
    int found = 0;                                                // 把 0 存入 found
    return lca(root, p, q, &found); // 返回 lca(根节点, 节点, 节点, 按位与 found)
}
int main(void) { // 程序入口：跑内嵌自测用例
    int v[] = {3, 5,          1,          6, 2, 0,
               8, INT_MIN_SN, INT_MIN_SN, 7, 4}; // 把 {3,5,1,6,2,0,8,INT_MIN_SN,INT_MIN_SN,7,4}; 写入 int v[]
    TreeNode *t = build_tree(v, 11);             // 把 build_tree(值, 11); 写入 TreeNode *t
    if (lowest_common_ancestor(t, 5, 1) != 3) {
        printf("FAIL 1\n");
        return 1;
    }
    if (lowest_common_ancestor(t, 5, 4) != 5) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
