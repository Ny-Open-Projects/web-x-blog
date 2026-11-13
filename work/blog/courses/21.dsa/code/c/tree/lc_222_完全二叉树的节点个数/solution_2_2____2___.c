/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136210437 */
/* LeetCode 222. 完全二叉树的节点个数 — C 版（方案2） */
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

static int count_nodes(TreeNode *root) { // 定义函数/方法 count_nodes
    if (!root)
        return 0; // 若 取反 根节点，直接返回 0
    int lh = 0;
    TreeNode *r = root; // 把 0; TreeNode 乘 右指针 赋值为 根节点 存入 lh
    while (r) {
        lh++;
        r = r->left;
    } // 循环，直到不满足「右指针) { lh 加一 ; 右指针 赋值为 右指针 减 超过 左边界; }」
    int rh = 0;
    r = root; // 把 0; 右指针 赋值为 根节点 存入 rh
    while (r) {
        rh++;
        r = r->right;
    } // 循环，直到不满足「右指针) { rh 加一 ; 右指针 赋值为 右指针 减 超过 右边界; }」
    if (lh == rh)
        return (1 << lh) - 1; // 若 lh 等于 rh，直接返回 (1 小于 小于 lh) 减 1
    return 1 + count_nodes(root->left) +
           count_nodes(root->right); // 返回 1 加 count_nodes(根节点 减 超过 左边界) 加 count_nodes(根节点 减
                                     // 超过 右边界)
}
int main(void) {                         // 程序入口：跑内嵌自测用例
    int v1[] = {1, 2, 3, 4, 5, 6};       // 把 {1,2,3,4,5,6}; 写入 int v1[]
    int v4[] = {1, 2, 3, 4, 5, 6, 7, 8}; // 把 {1,2,3,4,5,6,7,8}; 写入 int v4[]
    if (count_nodes(build_tree(v1, 6)) != 6) {
        printf("FAIL 1\n");
        return 1;
    }
    if (count_nodes(NULL) != 0) {
        printf("FAIL 2\n");
        return 1;
    }               // 若 count_nodes(NULL) 不等于 0) { 输出「FAIL 2 」); return 1; }
    int v3[] = {1}; // 把 {1}; 写入 int v3[]
    if (count_nodes(build_tree(v3, 1)) != 1) {
        printf("FAIL 3\n");
        return 1;
    }
    if (count_nodes(build_tree(v4, 8)) != 8) {
        printf("FAIL 4\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
