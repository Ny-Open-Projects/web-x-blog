/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136684493 */
/* LeetCode 230. 二叉搜索树中第K小的元素 — C 版（方案1） */
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

static int kth_smallest(TreeNode *root, int k) { // 定义函数/方法 kth_smallest
    TreeNode *stack[256];                        // TreeNode 乘 栈[256];
    int top = 0;                                 // 把 0 存入 top
    TreeNode *cur = root;                        // 把 根节点; 写入 TreeNode *cur
    while (cur || top > 0) {                     // 循环，直到不满足「当前值 或 top 超过 0」
        while (cur) {
            stack[top++] = cur;
            cur = cur->left;
        } // 循环，直到不满足「当前值) { 栈[top 加一 ] 赋值为 当前值; 当前值 赋值为 当前值 减 超过 左边界; }」
        cur = stack[--top]; // 把 栈[ 减一 top]; 写入 当前值
        k--;                // 下标 k 减一
        if (k == 0)
            return cur->val; // 若 下标 k 等于 0，直接返回 当前值 减 超过 值
        cur = cur->right;    // 把 当前值 减 超过 右边界; 写入 当前值
    }
    return -1; // 返回 减 1
}
int main(void) {                         // 程序入口：跑内嵌自测用例
    int v1[] = {3, 1, 4, INT_MIN_SN, 2}; // 把 {3,1,4,INT_MIN_SN,2}; 写入 int v1[]
    int v2[] = {5, 3,          6,          2,
                4, INT_MIN_SN, INT_MIN_SN, 1}; // 把 {5,3,6,2,4,INT_MIN_SN,INT_MIN_SN,1}; 写入 int v2[]
    TreeNode *t = build_tree(v1, 5);           // 把 build_tree(v1, 5); 写入 TreeNode *t
    if (kth_smallest(t, 1) != 1) {
        printf("FAIL 1\n");
        return 1;
    } // 若 kth_smallest(另一字符串, 1) 不等于 1) { 输出「FAIL 1 」); return 1; }
    if (kth_smallest(t, 2) != 2) {
        printf("FAIL 2\n");
        return 1;
    } // 若 kth_smallest(另一字符串, 2) 不等于 2) { 输出「FAIL 2 」); return 1; }
    TreeNode *t2 = build_tree(v2, 8); // 把 build_tree(v2, 8); 写入 TreeNode *t2
    if (kth_smallest(t2, 3) != 3) {
        printf("FAIL 3\n");
        return 1;
    }                 // 若 kth_smallest(t2, 3) 不等于 3) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
