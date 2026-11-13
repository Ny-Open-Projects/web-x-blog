// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135122295
// LeetCode 144. 二叉树的前序遍历 — C++ 版（方案3）
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

static std::vector<int> preorderTraversal(TreeNode *root) {
    if (!root)
        return {};                          // 若 取反 根节点，直接返回 {}
    std::vector<int> res{root->val};        // std::vector 小于 int 超过 结果{根节点 减 超过 值};
    auto l = preorderTraversal(root->left); // 把 preorderTraversal(根节点 减 超过 左边界) 存入 左指针
    auto r = preorderTraversal(root->right); // 把 preorderTraversal(根节点 减 超过 右边界) 存入 右指针
    res.insert(res.end(), l.begin(), l.end()); // 结果 插入 结果.终点(), 左指针 迭代位置 , 左指针.终点());
    res.insert(res.end(), r.begin(), r.end()); // 结果 插入 结果.终点(), 右指针 迭代位置 , 右指针.终点());
    return res;                                // 返回 结果
}
int main() { // 程序入口：跑内嵌自测用例
    assert((preorderTraversal(build_tree({1, 2, 3, std::nullopt, 4, 5})) ==
            std::vector<int>{1, 2, 4, 3, 5}));  // 断言校验
    assert(preorderTraversal(nullptr).empty()); // 断言校验
    std::cout << "PASS" << std::endl;           // 全部用例通过，输出 PASS
    return 0;                                   // 返回 0
}
