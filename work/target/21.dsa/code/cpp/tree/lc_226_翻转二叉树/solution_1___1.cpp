// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134541657
// LeetCode 226. 翻转二叉树 — C++ 版（方案1）
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

static TreeNode *invertTree(TreeNode *root) { // static TreeNode 乘 invertTree(TreeNode 乘 根节点) {
    if (!root)
        return nullptr;                     // 若 取反 根节点，直接返回 nullptr
    std::vector<TreeNode *> stack{root};    // std::vector 小于 TreeNode 乘 超过 栈{根节点};
    while (!stack.empty()) {                // 循环，直到不满足「取反 栈.empty(」
        auto *node = stack.back();          // 把 栈.back(); 写入 auto *node
        stack.pop_back();                   // 弹出栈顶元素
        std::swap(node->left, node->right); // 交换 节点 减 超过 左边界 与 节点 减 超过 右边界
        if (node->left)
            stack.push_back(node->left); // 若 节点 减 超过 左边界) 栈 追加 节点 减 超过 左边界);
        if (node->right)
            stack.push_back(node->right); // 若 节点 减 超过 右边界) 栈 追加 节点 减 超过 右边界);
    }
    return root; // 返回 根节点
}
static std::vector<int>
levels(TreeNode *root) {  // static std::vector 小于 int 超过 levels(TreeNode 乘 根节点) {
    std::vector<int> out; // std::vector 小于 int 超过 out;
    if (!root)
        return out;           // 若 取反 根节点，直接返回 out
    std::queue<TreeNode *> q; // std::队列 小于 TreeNode 乘 超过 节点;
    q.push(root);             // 把 根节点 压入栈/数组尾部
    while (!q.empty()) {      // 循环，直到不满足「取反 节点.empty(」
        auto *n = q.front();
        q.pop();               // 弹出栈顶元素
        out.push_back(n->val); // out 追加 元素个数 减 超过 值);
        if (n->left)
            q.push(n->left); // 若 元素个数 减 超过 左边界) 节点 追加 元素个数 减 超过 左边界);
        if (n->right)
            q.push(n->right); // 若 元素个数 减 超过 右边界) 节点 追加 元素个数 减 超过 右边界);
    }
    return out; // 返回 out
}
int main() { // 程序入口：跑内嵌自测用例
    auto *t = invertTree(
        build_tree({4, 2, 7, 1, 3, 6, 9})); // 把 invertTree(build_tree({4, 2, 7, 1, 3, 6, 9})); 写入 auto *t
    assert((levels(t) == std::vector<int>{4, 7, 2, 9, 6, 3, 1})); // 断言校验
    assert(invertTree(nullptr) == nullptr);                       // 断言校验
    free_tree(t);                                                 // free_tree(另一字符串);
    std::cout << "PASS" << std::endl;                             // 全部用例通过，输出 PASS
    return 0;                                                     // 返回 0
}
