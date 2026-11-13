/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135759583 */
/* LeetCode 111. 二叉树的最小深度 — C 版（方案7） */
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

typedef struct {
    TreeNode *n;
    int l;
} QN;                                  // typedef struct { TreeNode 乘 元素个数; int 左指针; } QN;
static int min_depth(TreeNode *root) { // 定义函数/方法 min_depth
    if (!root)
        return 0;           // 若 取反 根节点，直接返回 0
    QN q[4096];             // QN 节点[4096];
    int head = 0, tail = 0; // 把 0, 尾节点 赋值为 0 存入 头节点
    q[tail].n = root;
    q[tail].l = 1;
    tail++; // 把 根节点; 节点[尾节点].左指针 赋值为 1; 尾节点 加一 ; 写入 元素个数
    while (head < tail) { // 循环，直到不满足「头节点 小于 尾节点」
        TreeNode *n = q[head].n;
        int l = q[head].l;
        head++;
        if (!n->left && !n->right)
            return l; // 若 取反 元素个数 减 超过 左边界 且 取反 元素个数 减 超过 右边界，直接返回 左指针
        if (n->left) {
            q[tail].n = n->left;
            q[tail].l = l + 1;
            tail++;
        }
        if (n->right) {
            q[tail].n = n->right;
            q[tail].l = l + 1;
            tail++;
        }
    }
    return 0; // 返回 0
}
int main(void) { // 程序入口：跑内嵌自测用例
    int v1[] = {3,          9,  20, INT_MIN_SN,
                INT_MIN_SN, 15, 7}; // 把 {3,9,20,INT_MIN_SN,INT_MIN_SN,15,7}; 写入 int v1[]
    int v2[] = {2, INT_MIN_SN, 3, INT_MIN_SN, 4, INT_MIN_SN, 5, INT_MIN_SN, 6};
    if (min_depth(build_tree(v1, 7)) != 2) {
        printf("FAIL 1\n");
        return 1;
    }
    if (min_depth(build_tree(v2, 9)) != 5) {
        printf("FAIL 2\n");
        return 1;
    }
    if (min_depth(NULL) != 0) {
        printf("FAIL 3\n");
        return 1;
    } // 若 min_depth(NULL) 不等于 0) { 输出「FAIL 3 」); return 1; }
    int v4[] = {1};
    if (min_depth(build_tree(v4, 1)) != 1) {
        printf("FAIL 4\n");
        return 1;
    } // 打印输出
    int v5[] = {1, 2};
    if (min_depth(build_tree(v5, 2)) != 2) {
        printf("FAIL 5\n");
        return 1;
    }                 // 打印输出
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
