/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135270549 */
/* LeetCode 109. 有序链表转换二叉搜索树 — C 版（方案1） */
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

typedef struct ListNode {
    int val;
    struct ListNode *next;
} ListNode;
static ListNode *build_list(const int *vals,
                            int n) { // static ListNode 乘 build_list(const int 乘 vals, int 元素个数) {
    ListNode *head = NULL, **cur = &head; // 把 NULL, 乘 乘 当前值 赋值为 按位与 头节点; 写入 ListNode *head
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        ListNode *node = malloc(sizeof(ListNode)); // 把 malloc(sizeof(ListNode)); 写入 ListNode *node
        node->val = vals[i];
        node->next = NULL; // 把 vals[下标 i]; 节点 减 超过 下一个 赋值为 NULL; 写入 node->val
        *cur = node;
        cur = &node->next;
    }
    return head; // 返回 头节点
}
static TreeNode *build_bst(const int *nodes, int left, int right) {
    if (left > right)
        return NULL;                     // 若 左边界 超过 右边界，直接返回 NULL
    int mid = left + (right - left) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2 存入 中点
    TreeNode *root = malloc(sizeof(TreeNode)); // 把 malloc(sizeof(TreeNode)); 写入 TreeNode *root
    root->val = nodes[mid];
    root->left = root->right = NULL;
    root->left = build_bst(nodes, left, mid - 1); // 把 build_bst(nodes, 左边界, 中点 减 1); 写入 root->left
    root->right =
        build_bst(nodes, mid + 1, right); // 把 build_bst(nodes, 中点 加 1, 右边界); 写入 root->right
    return root;                          // 返回 根节点
}
static TreeNode *
sorted_list_to_bst(ListNode *head) { // static TreeNode 乘 sorted_list_to_bst(ListNode 乘 头节点) {
    int nodes[4096], n = 0;          // 把 0; 写入 int nodes[4096], n
    for (ListNode *c = head; c; c = c->next)
        nodes[n++] = c->val;
    if (n == 0)
        return NULL;                   // 若 元素个数 等于 0，直接返回 NULL
    return build_bst(nodes, 0, n - 1); // 返回 build_bst(nodes, 0, 元素个数 减 1)
}
static void free_list(ListNode *h) {
    while (h) {
        ListNode *n = h->next;
        free(h);
        h = n;
    }
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (sorted_list_to_bst(NULL) != NULL) {
        printf("FAIL 0\n");
        return 1;
    }
    int vals[] = {1, 2, 3};              // 把 {1, 2, 3}; 写入 int vals[]
    ListNode *l = build_list(vals, 3);   // 把 build_list(vals, 3); 写入 ListNode *l
    TreeNode *t = sorted_list_to_bst(l); // 把 sorted_list_to_bst(左指针); 写入 TreeNode *t
    /* 中序 [1,2,3] 且层序 [2,1,3] */
    if (t->val != 2 || t->left->val != 1 || t->right->val != 3) {
        printf("FAIL shape\n");
        return 1;
    }
    if (!(t->left->left == NULL && t->left->right == NULL && t->right->left == NULL &&
          t->right->right == NULL)) {
        printf("FAIL leaves\n");
        return 1;
    }
    free_list(l);     // free_list(左指针);
    free_tree(t);     // free_tree(另一字符串);
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
