/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/131038644 */
/* LeetCode 107. 二叉树的层序遍历 II — C 版（方案2） */
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

static int level_order_bottom(TreeNode *root, int out[][64],
                              int levels[]) { // 定义函数/方法 level_order_bottom
    if (!root) {
        return 0;
    }                                    // 若 取反 根节点) { return 0; }
    TreeNode *q[4096];                   // TreeNode 乘 节点[4096];
    int head = 0, tail = 0;              // 把 0, 尾节点 赋值为 0 存入 头节点
    int tmp[64][64], tl[64], nl = 0;     // 把 0; 写入 int tmp[64][64], tl[64], nl
    q[tail++] = root;                    // 把 根节点; 写入 q[tail++]
    while (head < tail) {                // 循环，直到不满足「头节点 小于 尾节点」
        int size = tail - head, cnt = 0; // 把 尾节点 减 头节点, 计数 赋值为 0 存入 大小
        for (int i = 0; i < size; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 大小 就继续
            TreeNode *n = q[head++];     // 把 节点[头节点 加一 ]; 写入 TreeNode *n
            tmp[nl][cnt++] = n->val;     // 把 元素个数 减 超过 值; 写入 tmp[nl][cnt++]
            if (n->left)
                q[tail++] =
                    n->left; // 若 元素个数 减 超过 左边界) 节点[尾节点 加一 ] 赋值为 元素个数 减 超过 左边界;
            if (n->right)
                q[tail++] = n->right; // 若 元素个数 减 超过 右边界) 节点[尾节点 加一 ] 赋值为 元素个数 减
                                      // 超过 右边界;
        }
        tl[nl++] = cnt; // 把 计数; 写入 tl[nl++]
    }
    for (int i = 0; i < nl; i++) { /* 反转 */ // 让 下标 i 从 0 开始计数，下标 i 小于 nl 就继续
        levels[i] = tl[nl - 1 - i];           // 把 tl[nl 减 1 减 下标 i]; 写入 levels[i]
        for (int j = 0; j < tl[nl - 1 - i]; j++)
            out[i][j] =
                tmp[nl - 1 - i][j]; // 让 下标 j 从 0 开始计数，下标 j 小于 tl[nl 减 1 减 下标 i] 就继续
    }
    return nl; // 返回 nl
}
int main(void) { // 程序入口：跑内嵌自测用例
    int v[] = {3,          9,  20, INT_MIN_SN,
               INT_MIN_SN, 15, 7};  // 把 {3,9,20,INT_MIN_SN,INT_MIN_SN,15,7}; 写入 int v[]
    int out[64][64], levels[64], n; // int out[64][64], levels[64], 元素个数;
    if (level_order_bottom(NULL, out, levels) != 0) {
        printf("FAIL 0\n");
        return 1;
    }
    n = level_order_bottom(build_tree(v, 7), out,
                           levels); // 把 level_order_bottom(build_tree(值, 7), out, levels); 写入 元素个数
    if (n != 3 || out[0][0] != 15 || out[0][1] != 7 || out[1][0] != 9 || out[1][1] != 20 || out[2][0] != 3) {
        printf("FAIL 1\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
