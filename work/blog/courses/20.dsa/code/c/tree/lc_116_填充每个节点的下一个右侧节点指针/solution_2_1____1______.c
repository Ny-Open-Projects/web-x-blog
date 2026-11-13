/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386215 */
/* LeetCode 116. 填充每个节点的下一个右侧节点指针 — C 版（方案2） */
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

typedef struct NNode {
    int val;
    struct NNode *left, *right, *next;
} NNode;
static NNode *nnew(int v) {
    NNode *n = calloc(1, sizeof(NNode));
    n->val = v;
    return n;
}
static void free_ntree(NNode *n) {
    if (!n)
        return;
    free_ntree(n->left);
    free_ntree(n->right);
    free(n);
}
static NNode *build_ntree(const int *vals,
                          int n) { // static NNode 乘 build_ntree(const int 乘 vals, int 元素个数) {
    if (n == 0)
        return NULL;               // 若 元素个数 等于 0，直接返回 NULL
    NNode *root = nnew(vals[0]);   // 把 nnew(vals[0]); 写入 NNode *root
    NNode *q[256];                 // NNode 乘 节点[256];
    int head = 0, tail = 0, i = 1; // 把 0, 尾节点 赋值为 0, 下标 i 赋值为 1 存入 头节点
    q[tail++] = root;              // 把 根节点; 写入 q[tail++]
    while (head < tail && i < n) { // 循环，直到不满足「头节点 小于 尾节点 且 下标 i 小于 元素个数」
        NNode *node = q[head++]; // 把 节点[头节点 加一 ]; 写入 NNode *node
        if (i < n) {
            node->left = nnew(vals[i]);
            q[tail++] = node->left;
            i++;
        }
        if (i < n) {
            node->right = nnew(vals[i]);
            q[tail++] = node->right;
            i++;
        }
    }
    return root; // 返回 根节点
}
static NNode *connect(NNode *root) { // static NNode 乘 connect(NNode 乘 根节点) {
    if (!root)
        return NULL;                     // 若 取反 根节点，直接返回 NULL
    NNode *q[256];                       // NNode 乘 节点[256];
    int head = 0, tail = 0;              // 把 0, 尾节点 赋值为 0 存入 头节点
    q[tail++] = root;                    // 把 根节点; 写入 q[tail++]
    while (head < tail) {                // 循环，直到不满足「头节点 小于 尾节点」
        int size = tail - head;          // 把 尾节点 减 头节点 存入 大小
        NNode *prev = NULL;              // 把 NULL; 写入 NNode *prev
        for (int i = 0; i < size; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 大小 就继续
            NNode *node = q[head++];     // 把 节点[头节点 加一 ]; 写入 NNode *node
            if (prev)
                prev->next = node; // 若 前一个) 前一个 减 超过 下一个 赋值为 节点;
            prev = node;           // 把 节点; 写入 前一个
            if (node->left)
                q[tail++] =
                    node->left; // 若 节点 减 超过 左边界) 节点[尾节点 加一 ] 赋值为 节点 减 超过 左边界;
            if (node->right)
                q[tail++] =
                    node->right; // 若 节点 减 超过 右边界) 节点[尾节点 加一 ] 赋值为 节点 减 超过 右边界;
        }
    }
    return root; // 返回 根节点
}
int main(void) {                        // 程序入口：跑内嵌自测用例
    int vals[] = {1, 2, 3, 4, 5, 6, 7}; // 把 {1,2,3,4,5,6,7}; 写入 int vals[]
    if (connect(NULL) != NULL) {
        printf("FAIL nil\n");
        return 1;
    } // 若 connect(NULL) 不等于 NULL) { 输出「FAIL nil 」); return 1; }
    NNode *root = connect(build_ntree(vals, 7));  // 把 connect(build_ntree(vals, 7)); 写入 NNode *root
    NNode *cur = root;                            // 把 根节点; 写入 NNode *cur
    int level = 0;                                // 把 0 存入 level
    int want[3][4] = {{1}, {2, 3}, {4, 5, 6, 7}}; // 把 { {1}, {2,3}, {4,5,6,7} }; 写入 int want[3][4]
    int wantn[3] = {1, 2, 4};                     // 把 {1, 2, 4}; 写入 int wantn[3]
    while (cur) {                                 // 循环，直到不满足「当前值」
        int cnt = 0;                              // 把 0 存入 计数
        for (NNode *n = cur; n; n = n->next) { // 把 当前值; 元素个数; 元素个数 赋值为 元素个数 减 超过
                                               // 下一个) { 写入 for (NNode *n
            if (cnt >= wantn[level] || n->val != want[level][cnt]) {
                printf("FAIL L%d\n", level);
                return 1;
            }
            cnt++; // 计数 加一
        }
        if (cnt != wantn[level]) {
            printf("FAIL L%d cnt\n", level);
            return 1;
        }
        cur = cur->left; // 把 当前值 减 超过 左边界; 写入 当前值
        level++;         // level 加一
    }
    if (level != 3) {
        printf("FAIL levels\n");
        return 1;
    }                 // 若 level 不等于 3) { 输出「FAIL levels 」); return 1; }
    free_ntree(root); // free_ntree(根节点);
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
