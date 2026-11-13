/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136391511 */
/* LeetCode 404. 左叶子之和 — C 版（方案1） */
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

static int is_leaf(const TreeNode *n) { return n && !n->left && !n->right; }
static int sum_of_left_leaves(TreeNode *root) { // 定义函数/方法 sum_of_left_leaves
    if (!root)
        return 0;                      // 若 取反 根节点，直接返回 0
    int total = 0;                     // 把 0 存入 总和
    TreeNode *stack[256];              // TreeNode 乘 栈[256];
    int top = 0;                       // 把 0 存入 top
    stack[top++] = root;               // 把 根节点; 写入 stack[top++]
    while (top > 0) {                  // 循环，直到不满足「top 超过 0」
        TreeNode *node = stack[--top]; // 把 栈[ 减一 top]; 写入 TreeNode *node
        if (node->left) {              // 若 节点 减 超过 左边界
            if (is_leaf(node->left))
                total +=
                    node->left
                        ->val; // 若 is_leaf(节点 减 超过 左边界)) 总和 累加 节点 减 超过 左边界 减 超过 值;
            else
                stack[top++] = node->left; // 否则
        }
        if (node->right)
            stack[top++] = node->right; // 若 节点 减 超过 右边界) 栈[top 加一 ] 赋值为 节点 减 超过 右边界;
    }
    return total; // 返回 总和
}
int main(void) { // 程序入口：跑内嵌自测用例
    int v1[] = {3,          9,  20, INT_MIN_SN,
                INT_MIN_SN, 15, 7}; // 把 {3,9,20,INT_MIN_SN,INT_MIN_SN,15,7}; 写入 int v1[]
    int v3[] = {1, 2, 3, 4, 5};     // 把 {1,2,3,4,5}; 写入 int v3[]
    if (sum_of_left_leaves(build_tree(v1, 7)) != 24) {
        printf("FAIL 1\n");
        return 1;
    }
    if (sum_of_left_leaves(NULL) != 0) {
        printf("FAIL 2\n");
        return 1;
    }
    if (sum_of_left_leaves(build_tree(v3, 5)) != 4) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
