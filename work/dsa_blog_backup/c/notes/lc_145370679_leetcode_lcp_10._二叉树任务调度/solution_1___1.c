// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
// LeetCode LCP 10. 二叉树任务调度 — C 版（方案1：深度优先-贪心）
#include <math.h>   // 引入头文件
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件

// 二叉树节点：val 为自身执行时间（double 承载并行节省的 0.5）
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

// dfs：递归求出子树总耗时 *sum 与两台机器并行可节省的耗时 *saved
static void dfs(const TreeNode *root, double *sum, double *saved) {
    if (root == NULL) { // 空子树：总耗时 0，节省 0
        *sum = 0.0;
        *saved = 0.0;
        return;
    }
    double a, b, c, d;
    dfs(root->left, &a, &b);  // a: 左子树总耗时, b: 左子树已节省
    dfs(root->right, &c, &d); // c: 右子树总耗时, d: 右子树已节省
    double s;
    if ((c - 2.0 * d <= a && a <= c) || (a - 2.0 * b <= c && c <= a)) {
        // 一侧的串行下界落在另一侧的耗时区间内：两台机器互相填空，左右几乎完全并行
        s = (a + c) / 2.0; // 浮点除法：总和为奇数时会出现 0.5
    } else if (a - 2.0 * b > c) {
        // 左子树串行段太长：右子树整体塞进左边空闲的那台机器
        s = b + c;
    } else {
        // 右子树占主导：左子树整体塞进右边空闲的那台机器
        s = a + d;
    }
    *sum = a + c + root->val; // 加上当前节点自身的执行时间
    *saved = s;
}

static double minimal_execution_time(const TreeNode *root) { // 答案 = 子树总和 - 并行节省
    double total, saved;
    dfs(root, &total, &saved);
    return total - saved;
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
