// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136528287
// LeetCode 236. 二叉树的最近公共祖先 — C++ 版（方案2）
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

static int lca(TreeNode *n, int p, int q, int &found) { // 定义函数/方法 lca
    if (!n)
        return -1; // 若 取反 元素个数，直接返回 减 1
    if (n->val == p || n->val == q) {
        ++found;
        return n->val;
    }
    int before = found;                // 把 found 存入 before
    int l = lca(n->left, p, q, found); // 把 lca(元素个数 减 超过 左边界, 节点, 节点, found) 存入 左指针
    int r = lca(n->right, p, q, found); // 把 lca(元素个数 减 超过 右边界, 节点, 节点, found) 存入 右指针
    if (l != -1 && r != -1)
        return n->val; // 若 左指针 不等于 减 1 且 右指针 不等于 减 1，直接返回 元素个数 减 超过 值
    if (found > before)
        return (l != -1) ? l : r; // 若 found 超过 before，直接返回 (左指针 不等于 减 1) ? 左指针 : 右指针
    return -1;                    // 返回 减 1
}
static int lowestCommonAncestor(TreeNode *root, int p, int q) { // 定义函数/方法 lowestCommonAncestor
    int found = 0;                                              // 把 0 存入 found
    return lca(root, p, q, found); // 返回 lca(根节点, 节点, 节点, found)
}
int main() { // 程序入口：跑内嵌自测用例
    auto *t = build_tree({3, 5, 1, 6, 2, 0, 8, std::nullopt, std::nullopt, 7, 4});
    assert(lowestCommonAncestor(t, 5, 1) == 3); // 断言校验
    assert(lowestCommonAncestor(t, 5, 4) == 5); // 断言校验
    std::cout << "PASS" << std::endl;           // 全部用例通过，输出 PASS
    return 0;                                   // 返回 0
}
