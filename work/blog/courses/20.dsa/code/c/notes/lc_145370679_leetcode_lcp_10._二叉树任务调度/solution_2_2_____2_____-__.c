// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
// LeetCode LCP 10. 二叉树任务调度 — C 版（方案2：深度优先-优化）
#include <math.h>   // 引入头文件
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件

// 二叉树节点：val 为自身执行时间（double 承载均摊的 0.5）
typedef struct TreeNode {
    double val;
    struct TreeNode *left, *right;
} TreeNode;

static TreeNode *new_node(double val) { // 新建节点
    TreeNode *n = (TreeNode *)malloc(sizeof(TreeNode));
    n->val = val;
    n->left = NULL;
    n->right = NULL;
    return n;
}

// 层序数组建树，NAN 表示空节点（任务耗时恒为正，用 NAN 做哨兵安全）
static TreeNode *build_tree(const double *vals, int n) {
    if (n == 0)
        return NULL;
    TreeNode *root = new_node(vals[0]);
    TreeNode **queue = (TreeNode **)malloc(sizeof(TreeNode *) * (size_t)n); // 队列里只放非空节点
    int head = 0, tail = 0, i = 1;
    queue[tail++] = root;
    while (head < tail && i < n) {
        TreeNode *node = queue[head++]; // 出队一个父节点
        if (i < n && !isnan(vals[i])) { // 左孩子
            node->left = new_node(vals[i]);
            queue[tail++] = node->left;
        }
        i++;
        if (i < n && !isnan(vals[i])) { // 右孩子
            node->right = new_node(vals[i]);
            queue[tail++] = node->right;
        }
        i++;
    }
    free(queue);
    return root;
}

static void free_tree(TreeNode *root) { // 递归释放整棵树
    if (root == NULL)
        return;
    free_tree(root->left);
    free_tree(root->right);
    free(root);
}

static double dmax(double x, double y) { return x > y ? x : y; } // 双数取大

// dfs：递归求出子树总耗时 *sum 与子树最小完成时间 *max_exec
static void dfs(const TreeNode *root, double *sum, double *max_exec) {
    if (root == NULL) { // 空子树
        *sum = 0.0;
        *max_exec = 0.0;
        return;
    }
    double left_sum, left_exec, right_sum, right_exec;
    dfs(root->left, &left_sum, &left_exec);    // 左子树的总耗时与最小完成时间
    dfs(root->right, &right_sum, &right_exec); // 右子树的总耗时与最小完成时间
    // 当前任务自身必须独占串行跑完；孩子任务两条机器可穿插：
    // 下界取「较慢的一侧」与「两侧工作量均分到两台机器」的较大者
    double parallel = (left_sum + right_sum) / 2.0; // 两台机器均摊左右子树总工作量（浮点）
    *max_exec = root->val + dmax(dmax(left_exec, right_exec), parallel);
    *sum = left_sum + right_sum + root->val;
}

static double minimal_execution_time(const TreeNode *root) { // 答案 = 整棵树的最小完成时间
    double total, max_exec;
    dfs(root, &total, &max_exec);
    return max_exec;
}

int main(void) { // 程序入口：跑内嵌自测用例（三个官方用例）
    const double c1[] = {47, 74, 31};
    const double c2[] = {15, 21, NAN, 24, NAN, 27, 26};
    const double c3[] = {1, 3, 2, NAN, NAN, 4, 4};
    const double *vals[] = {c1, c2, c3};
    const int lens[] = {3, 7, 7};
    const double wants[] = {121.0, 87.0, 7.5};
    for (int k = 0; k < 3; k++) {
        TreeNode *root = build_tree(vals[k], lens[k]);
        double got = minimal_execution_time(root);
        free_tree(root);
        if (fabs(got - wants[k]) >= 1e-6) {                 // 浮点比较用 1e-6 容差
            printf("FAIL got %f want %f\n", got, wants[k]); // 失败打印 FAIL
            return 1;                                       // 非零退出
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0 表示通过
}
