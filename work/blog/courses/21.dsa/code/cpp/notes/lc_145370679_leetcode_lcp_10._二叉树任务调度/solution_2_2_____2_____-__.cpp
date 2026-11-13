// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
// LeetCode LCP 10. 二叉树任务调度 — C++ 版（方案2：深度优先-优化）
#include <algorithm> // 引入头文件
#include <cmath>     // 引入头文件
#include <cstdio>    // 引入头文件
#include <cstdlib>   // 引入头文件
#include <queue>     // 引入头文件
#include <utility>   // 引入头文件
#include <vector>    // 引入头文件

// 二叉树节点：val 为自身执行时间（double 承载均摊的 0.5）
struct TreeNode {
    double val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(double v) : val(v), left(NULL), right(NULL) {} // 构造函数
};

// 层序数组建树，NAN 表示空节点（任务耗时恒为正，用 NAN 做哨兵安全）
static TreeNode *build_tree(const std::vector<double> &vals) {
    if (vals.empty())
        return NULL;
    TreeNode *root = new TreeNode(vals[0]);
    std::queue<TreeNode *> queue; // 队列里只放非空节点
    queue.push(root);
    size_t i = 1;
    while (!queue.empty() && i < vals.size()) {
        TreeNode *node = queue.front(); // 出队一个父节点
        queue.pop();
        if (i < vals.size() && !isnan(vals[i])) { // 左孩子
            node->left = new TreeNode(vals[i]);
            queue.push(node->left);
        }
        i++;
        if (i < vals.size() && !isnan(vals[i])) { // 右孩子
            node->right = new TreeNode(vals[i]);
            queue.push(node->right);
        }
        i++;
    }
    return root;
}

static void free_tree(TreeNode *root) { // 递归释放整棵树
    if (root == NULL)
        return;
    free_tree(root->left);
    free_tree(root->right);
    delete root;
}

// dfs 返回 (子树总耗时, 子树最小完成时间 max_exec)
static std::pair<double, double> dfs(const TreeNode *root) {
    if (root == NULL)
        return std::make_pair(0.0, 0.0);                // 空子树
    std::pair<double, double> left = dfs(root->left);   // 左子树的总耗时与最小完成时间
    std::pair<double, double> right = dfs(root->right); // 右子树的总耗时与最小完成时间
    // 当前任务自身必须独占串行跑完；孩子任务两条机器可穿插：
    // 下界取「较慢的一侧」与「两侧工作量均分到两台机器」的较大者
    double parallel = (left.first + right.first) / 2.0; // 两台机器均摊左右子树总工作量（浮点）
    double max_exec = root->val + std::max(std::max(left.second, right.second), parallel);
    return std::make_pair(left.first + right.first + root->val, max_exec);
}

static double minimal_execution_time(const TreeNode *root) { // 答案 = 整棵树的最小完成时间
    return dfs(root).second;
}

int main() { // 程序入口：跑内嵌自测用例（三个官方用例）
    const double c1[] = {47, 74, 31};
    const double c2[] = {15, 21, NAN, 24, NAN, 27, 26};
    const double c3[] = {1, 3, 2, NAN, NAN, 4, 4};
    const double wants[] = {121.0, 87.0, 7.5};
    const double *vals[] = {c1, c2, c3};
    const size_t lens[] = {3, 7, 7};
    for (int k = 0; k < 3; k++) {
        TreeNode *root = build_tree(std::vector<double>(vals[k], vals[k] + lens[k]));
        double got = minimal_execution_time(root);
        free_tree(root);
        if (std::fabs(got - wants[k]) >= 1e-6) {                 // 浮点比较用 1e-6 容差
            std::printf("FAIL got %f want %f\n", got, wants[k]); // 失败打印 FAIL
            return 1;                                            // 非零退出
        }
    }
    std::printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;              // 返回 0 表示通过
}
