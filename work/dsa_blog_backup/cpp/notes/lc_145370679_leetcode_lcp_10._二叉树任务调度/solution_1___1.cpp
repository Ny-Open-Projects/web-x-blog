// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
// LeetCode LCP 10. 二叉树任务调度 — C++ 版（方案1：深度优先-贪心）
#include <cmath>   // 引入头文件
#include <cstdio>  // 引入头文件
#include <cstdlib> // 引入头文件
#include <queue>   // 引入头文件
#include <utility> // 引入头文件
#include <vector>  // 引入头文件

// 二叉树节点：val 为自身执行时间（double 承载并行节省的 0.5）
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

// dfs 返回 (子树总耗时, 两台机器并行可节省的耗时)
static std::pair<double, double> dfs(const TreeNode *root) {
    if (root == NULL)
        return std::make_pair(0.0, 0.0); // 空子树：总耗时 0，节省 0
    std::pair<double, double> left = dfs(root->left);
    std::pair<double, double> right = dfs(root->right);
    double a = left.first, b = left.second;   // a: 左子树总耗时, b: 左子树已节省
    double c = right.first, d = right.second; // c: 右子树总耗时, d: 右子树已节省
    double saved;
    if ((c - 2.0 * d <= a && a <= c) || (a - 2.0 * b <= c && c <= a)) {
        // 一侧的串行下界落在另一侧的耗时区间内：两台机器互相填空，左右几乎完全并行
        saved = (a + c) / 2.0; // 浮点除法：总和为奇数时会出现 0.5
    } else if (a - 2.0 * b > c) {
        // 左子树串行段太长：右子树整体塞进左边空闲的那台机器
        saved = b + c;
    } else {
        // 右子树占主导：左子树整体塞进右边空闲的那台机器
        saved = a + d;
    }
    return std::make_pair(a + c + root->val, saved); // 加上当前节点自身的执行时间
}

static double minimal_execution_time(const TreeNode *root) { // 答案 = 子树总和 - 并行节省
    std::pair<double, double> r = dfs(root);
    return r.first - r.second;
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
