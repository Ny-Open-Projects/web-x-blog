/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136726698 */
/* LeetCode 617. 合并二叉树 — C 版（方案2） */
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
static TreeNode *merge_trees(TreeNode *t1, TreeNode *t2) {
    if (!t1)
        return t2; // 若 取反 t1，直接返回 t2
    if (!t2)
        return t1;      // 若 取反 t2，直接返回 t1
    t1->val += t2->val; // 把 t2 减 超过 值; 写入 t1->val +
    t1->left = merge_trees(t1->left,
                           t2->left); // 把 merge_trees(t1 减 超过 左边界, t2 减 超过 左边界); 写入 t1->left
    t1->right = merge_trees(
        t1->right, t2->right); // 把 merge_trees(t1 减 超过 右边界, t2 减 超过 右边界); 写入 t1->right
    return t1;                 // 返回 t1
}
static void check(const int *a, int na, const int *b, int nb, const int *w, int nw) { // 定义判定函数 check
    TreeNode *got = merge_trees(build_tree(a, na), build_tree(b, nb));
    TreeNode *want = build_tree(w, nw); // 把 build_tree(权重, nw); 写入 TreeNode *want
    if (!same_tree(got, want)) {
        printf("FAIL merge\n");
        exit(1);
    } // 若 取反 same_tree(got, want)) { 输出「FAIL merge 」); exit(1); }
}
int main(void) { // 程序入口：跑内嵌自测用例
    int a1[] = {1, 3, 2, 5}, b1[] = {2, 1, 3, INT_MIN_SN, 4, INT_MIN_SN, 7},
        w1[] = {3, 4, 5, 5, 4, INT_MIN_SN, 7};
    int a2[] = {0}, b2[] = {1}, w2[] = {1}; /* 空树用长度0表达 */
    int a4[] = {1, 2, 3}, b4[] = {1, 2, 3},
        w4[] = {2, 4, 6}; // 把 {1,2,3}, b4[] 赋值为 {1,2,3}, w4[] 赋值为 {2,4,6}; 写入 int a4[]
    check(a1, 4, b1, 7, w1, 7); // check(a1, 4, b1, 7, w1, 7);
    if (!same_tree(merge_trees(NULL, build_tree(b2, 1)), build_tree(w2, 1))) {
        printf("FAIL 2\n");
        return 1;
    }
    if (!same_tree(merge_trees(build_tree(b2, 1), NULL), build_tree(w2, 1))) {
        printf("FAIL 3\n");
        return 1;
    }
    check(a4, 3, b4, 3, w4, 3); // check(a4, 3, b4, 3, w4, 3);
    (void)a2;                   // (void)a2;
    printf("PASS\n");           // 全部用例通过，输出 PASS
    return 0;                   // 返回 0
}
