// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136210437
// LeetCode 222. 完全二叉树的节点个数 — C++ 版（方案3）
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

static int countNodes(TreeNode *root) { // 定义函数/方法 countNodes
    if (!root)
        return 0; // 若 取反 根节点，直接返回 0
    int lh = 0;   // 把 0 存入 lh
    for (TreeNode *r = root; r; r = r->left)
        ++lh; // 把 根节点; 右指针; 右指针 赋值为 右指针 减 超过 左边界) 加一 lh; 写入 for (TreeNode *r
    int rh = 0; // 把 0 存入 rh
    for (TreeNode *r = root; r; r = r->right)
        ++rh; // 把 根节点; 右指针; 右指针 赋值为 右指针 减 超过 右边界) 加一 rh; 写入 for (TreeNode *r
    if (lh == rh)
        return (1 << lh) - 1; // 若 lh 等于 rh，直接返回 (1 小于 小于 lh) 减 1
    return 1 + countNodes(root->left) +
           countNodes(root->right); // 返回 1 加 countNodes(根节点 减 超过 左边界) 加 countNodes(根节点 减
                                    // 超过 右边界)
}
int main() {                                                       // 程序入口：跑内嵌自测用例
    assert(countNodes(build_tree({1, 2, 3, 4, 5, 6})) == 6);       // 断言校验
    assert(countNodes(nullptr) == 0);                              // 断言校验
    assert(countNodes(build_tree({1})) == 1);                      // 断言校验
    assert(countNodes(build_tree({1, 2, 3, 4, 5, 6, 7, 8})) == 8); // 断言校验
    std::cout << "PASS" << std::endl;                              // 全部用例通过，输出 PASS
    return 0;                                                      // 返回 0
}
