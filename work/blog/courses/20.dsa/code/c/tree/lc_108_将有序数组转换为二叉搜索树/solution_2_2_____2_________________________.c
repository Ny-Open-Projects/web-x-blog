/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144993168 */
/* LeetCode 108. 将有序数组转换为二叉搜索树 — C 版（方案2） */
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
static int levels_flat(TreeNode *root, int out[]) { // 定义函数/方法 levels_flat
    if (!root)
        return 0; // 若 取反 根节点，直接返回 0
    TreeNode *q[4096];
    int head = 0, tail = 0, cnt = 0; // 把 0, 尾节点 赋值为 0, 计数 赋值为 0; 写入 TreeNode *q[4096]; int head
    q[tail++] = root;                // 把 根节点; 写入 q[tail++]
    while (head < tail) {        // 循环，直到不满足「头节点 小于 尾节点」
        TreeNode *n = q[head++]; // 把 节点[头节点 加一 ]; 写入 TreeNode *n
        out[cnt++] = n->val;     // 把 元素个数 减 超过 值; 写入 out[cnt++]
        if (n->left)
            q[tail++] =
                n->left; // 若 元素个数 减 超过 左边界) 节点[尾节点 加一 ] 赋值为 元素个数 减 超过 左边界;
        if (n->right)
            q[tail++] =
                n->right; // 若 元素个数 减 超过 右边界) 节点[尾节点 加一 ] 赋值为 元素个数 减 超过 右边界;
    }
    return cnt; // 返回 计数
}
static int eqarr(const int *a, int n, const int *b, int m) { // 定义函数/方法 eqarr
    if (n != m)
        return 0; // 若 元素个数 不等于 映射表，直接返回 0
    for (int i = 0; i < n; i++)
        if (a[i] != b[i])
            return 0; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    return 1;         // 返回 1
}

static TreeNode *helper(const int *nums, int left,
                        int right) { // static TreeNode 乘 helper(const int 乘 数组, int 左边界, int 右边界) {
    if (left > right)
        return NULL;                     // 若 左边界 超过 右边界，直接返回 NULL
    int mid = left + (right - left) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2 存入 中点
    TreeNode *root = malloc(sizeof(TreeNode)); // 把 malloc(sizeof(TreeNode)); 写入 TreeNode *root
    root->val = nums[mid];
    root->left = root->right = NULL;
    root->left = helper(nums, left, mid - 1); // 把 helper(数组, 左边界, 中点 减 1); 写入 root->left
    root->right = helper(nums, mid + 1, right); // 把 helper(数组, 中点 加 1, 右边界); 写入 root->right
    return root;                                // 返回 根节点
}
static TreeNode *sorted_array_to_bst(const int *nums, int n) {
    if (n == 0)
        return NULL;               // 若 元素个数 等于 0，直接返回 NULL
    return helper(nums, 0, n - 1); // 返回 helper(数组, 0, 元素个数 减 1)
}
int main(void) {                    // 程序入口：跑内嵌自测用例
    int in1[] = {-10, -3, 0, 5, 9}; // 把 { 减 10, 减 3,0,5,9}; 写入 int in1[]
    int w1[] = {0,  -10,        5, INT_MIN_SN,
                -3, INT_MIN_SN, 9}; // 把 {0, 减 10,5,INT_MIN_SN, 减 3,INT_MIN_SN,9}; 写入 int w1[]
    TreeNode *got = sorted_array_to_bst(in1, 5); // 把 sorted_array_to_bst(in1, 5); 写入 TreeNode *got
    TreeNode *want = build_tree(w1, 7);          // 把 build_tree(w1, 7); 写入 TreeNode *want
    if (!same_tree(got, want)) {
        printf("FAIL 1\n");
        return 1;
    }                // 若 取反 same_tree(got, want)) { 输出「FAIL 1 」); return 1; }
    int in2[] = {1}; // 把 {1}; 写入 int in2[]
    TreeNode *got2 = sorted_array_to_bst(in2, 1); // 把 sorted_array_to_bst(in2, 1); 写入 TreeNode *got2
    int w2[] = {1};                               // 把 {1}; 写入 int w2[]
    if (!same_tree(got2, build_tree(w2, 1))) {
        printf("FAIL 2\n");
        return 1;
    }
    if (sorted_array_to_bst(NULL, 0) != NULL) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
