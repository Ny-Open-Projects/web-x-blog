// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135005838
// LeetCode 700. 二叉搜索树中的搜索 — C++ 版（方案2）
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

static TreeNode *searchBST(TreeNode *root,
                           int val) { // static TreeNode 乘 searchBST(TreeNode 乘 根节点, int 值) {
    TreeNode *cur = root;             // 把 根节点; 写入 TreeNode *cur
    while (cur) {                     // 循环，直到不满足「当前值」
        if (cur->val == val)
            return cur; // 若 当前值 减 超过 值 等于 值，直接返回 当前值
        else if (cur->val > val)
            cur = cur->left; // 否则，若 当前值 减 超过 值 超过 值) 当前值 赋值为 当前值 减 超过 左边界;
        else
            cur = cur->right; // 否则
    }
    return nullptr; // 返回 nullptr
}
int main() {                               // 程序入口：跑内嵌自测用例
    auto *t = build_tree({4, 2, 7, 1, 3}); // 把 build_tree({4, 2, 7, 1, 3}); 写入 auto *t
    assert(searchBST(t, 2) != nullptr && searchBST(t, 2)->val == 2); // 断言校验
    assert(searchBST(t, 5) == nullptr);                              // 断言校验
    assert(searchBST(t, 4)->val == 4);                               // 断言校验
    assert(searchBST(nullptr, 1) == nullptr);                        // 断言校验
    free_tree(t);                                                    // free_tree(另一字符串);
    std::cout << "PASS" << std::endl;                                // 全部用例通过，输出 PASS
    return 0;                                                        // 返回 0
}
