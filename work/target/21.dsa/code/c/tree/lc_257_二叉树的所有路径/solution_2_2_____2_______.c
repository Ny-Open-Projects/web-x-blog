/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135666411 */
/* LeetCode 257. 二叉树的所有路径 — C 版（方案2） */
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

#include <string.h>                                                           // 引入头文件
static void dfs_paths(TreeNode *n, char *path, char (*paths)[64], int *cnt) { // 定义函数/方法 dfs_paths
    if (!n)
        return;                                       // 若 取反 元素个数) return;
    char buf[64];                                     // char buf[64];
    snprintf(buf, sizeof(buf), "%s%d", path, n->val); // 打印输出
    if (!n->left && !n->right) { // 若 取反 元素个数 减 超过 左边界 且 取反 元素个数 减 超过 右边界
        snprintf(paths[(*cnt)++], 64, "%s", buf); // 打印输出
        return;                                   // return;
    }
    strcat(buf, "->");                    // 打印输出
    dfs_paths(n->left, buf, paths, cnt);  // dfs_paths(元素个数 减 超过 左边界, buf, paths, 计数);
    dfs_paths(n->right, buf, paths, cnt); // dfs_paths(元素个数 减 超过 右边界, buf, paths, 计数);
}
static int binary_tree_paths(TreeNode *root, char (*paths)[64]) { // 定义函数/方法 binary_tree_paths
    int cnt = 0;                                                  // 把 0 存入 计数
    dfs_paths(root, "", paths, &cnt); // dfs_paths(根节点, 「」, paths, 按位与 计数);
    return cnt;                       // 返回 计数
}
int main(void) {        // 程序入口：跑内嵌自测用例
    char paths[64][64]; // char paths[64][64];
    int n = binary_tree_paths(build_tree((int[]){1, 2, 3}, 3), paths);
    if (n != 2 || strcmp(paths[0], "1->2") != 0 || strcmp(paths[1], "1->3") != 0) {
        printf("FAIL 1\n");
        return 1;
    }
    n = binary_tree_paths(build_tree((int[]){1}, 1), paths);
    if (n != 1 || strcmp(paths[0], "1") != 0) {
        printf("FAIL 2\n");
        return 1;
    }
    if (binary_tree_paths(NULL, paths) != 0) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
