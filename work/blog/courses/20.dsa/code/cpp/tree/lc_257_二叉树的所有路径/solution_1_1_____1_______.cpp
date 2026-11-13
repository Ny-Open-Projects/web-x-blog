// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135666411
// LeetCode 257. 二叉树的所有路径 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <cstdint>  // 引入头文件
#include <iostream> // 引入头文件
#include <optional> // 引入头文件
#include <queue>    // 引入头文件
#include <vector>   // 引入头文件

struct TreeNode {    // 定义类型
    int val;         // int 值;
    TreeNode *left;  // TreeNode 乘 左边界;
    TreeNode *right; // TreeNode 乘 右边界;
    explicit TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

static TreeNode *build_tree(const std::vector<std::optional<int>> &vals) {
    if (vals.empty() || !vals[0].has_value())
        return nullptr; // 若 vals 是否为空 或 取反 vals[0].has_value()，直接返回 nullptr
    auto *root = new TreeNode(*vals[0]); // 把 new TreeNode( 乘 vals[0]); 写入 auto *root
    std::queue<TreeNode *> q;            // std::队列 小于 TreeNode 乘 超过 节点;
    q.push(root);                        // 把 根节点 压入栈/数组尾部
    size_t i = 1;                        // 把 1; 写入 size_t i
    while (!q.empty() &&
           i < vals.size()) { // 循环，直到不满足「取反 节点 是否为空 且 下标 i 小于 vals.大小(」
        TreeNode *node = q.front();                  // 把 节点.front(); 写入 TreeNode *node
        q.pop();                                     // 弹出栈顶元素
        if (i < vals.size()) {                       // 若 下标 i 小于 vals.大小(
            if (vals[i].has_value()) {               // 若 vals[下标 i].has_value(
                node->left = new TreeNode(*vals[i]); // 把 new TreeNode( 乘 vals[下标 i]); 写入 node->left
                q.push(node->left);                  // 把 节点 减 超过 左边界 压入栈/数组尾部
            }
            ++i; // 加一 下标 i;
        }
        if (i < vals.size()) {                        // 若 下标 i 小于 vals.大小(
            if (vals[i].has_value()) {                // 若 vals[下标 i].has_value(
                node->right = new TreeNode(*vals[i]); // 把 new TreeNode( 乘 vals[下标 i]); 写入 node->right
                q.push(node->right); // 把 节点 减 超过 右边界 压入栈/数组尾部
            }
            ++i; // 加一 下标 i;
        }
    }
    return root; // 返回 根节点
}

static void free_tree(TreeNode *n) { // 定义函数/方法 free_tree
    if (!n)
        return;          // 若 取反 元素个数) return;
    free_tree(n->left);  // free_tree(元素个数 减 超过 左边界);
    free_tree(n->right); // free_tree(元素个数 减 超过 右边界);
    delete n;            // delete 元素个数;
}

static std::vector<std::string> binaryTreePaths(TreeNode *root) {
    std::vector<std::string> paths; // std::vector 小于 std::string 超过 paths;
    std::function<void(TreeNode *, std::string)> dfs = [&](TreeNode *n, std::string path) {
        if (!n)
            return;                     // 若 取反 元素个数) return;
        path += std::to_string(n->val); // 当前路径累加 std::to_string(元素个数 减 超过 值)
        if (!n->left && !n->right) { // 若 取反 元素个数 减 超过 左边界 且 取反 元素个数 减 超过 右边界
            paths.push_back(path); // paths 追加 当前路径);
            return;                // return;
        }
        path += "->";        // 当前路径累加 「 减 超过 」
        dfs(n->left, path);  // dfs(元素个数 减 超过 左边界, 当前路径);
        dfs(n->right, path); // dfs(元素个数 减 超过 右边界, 当前路径);
    };
    dfs(root, ""); // dfs(根节点, 「」);
    return paths;  // 返回 paths
}
int main() { // 程序入口：跑内嵌自测用例
    assert((binaryTreePaths(build_tree({1, 2, 3})) == std::vector<std::string>{"1->2", "1->3"})); // 断言校验
    assert((binaryTreePaths(build_tree({1})) == std::vector<std::string>{"1"})); // 断言校验
    assert(binaryTreePaths(nullptr).empty());                                    // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
