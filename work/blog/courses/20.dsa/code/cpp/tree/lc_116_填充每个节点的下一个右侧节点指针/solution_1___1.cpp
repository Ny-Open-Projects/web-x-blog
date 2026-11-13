// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386215
// LeetCode 116. 填充每个节点的下一个右侧节点指针 — C++ 版（方案1）
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

struct NNode { // 定义类型
    int val;   // int 值;
    NNode *left = nullptr, *right = nullptr, *next = nullptr;
    explicit NNode(int v) : val(v) {} // explicit NNode(int 值) : 值(值) {}
};
static NNode *buildNTree(const std::vector<int> &vals) {
    if (vals.empty())
        return nullptr;              // 若 vals 是否为空，直接返回 nullptr
    auto *root = new NNode(vals[0]); // 把 new NNode(vals[0]); 写入 auto *root
    std::queue<NNode *> q;           // std::队列 小于 NNode 乘 超过 节点;
    q.push(root);                    // 把 根节点 压入栈/数组尾部
    size_t i = 1;                    // 把 1; 写入 size_t i
    while (!q.empty() &&
           i < vals.size()) { // 循环，直到不满足「取反 节点 是否为空 且 下标 i 小于 vals.大小(」
        auto *node = q.front(); // 把 节点.front(); 写入 auto *node
        q.pop();                // 弹出栈顶元素
        if (i < vals.size()) {
            node->left = new NNode(vals[i]);
            q.push(node->left);
            ++i;
        }
        if (i < vals.size()) {
            node->right = new NNode(vals[i]);
            q.push(node->right);
            ++i;
        }
    }
    return root; // 返回 根节点
}
static NNode *connect(NNode *root) { // static NNode 乘 connect(NNode 乘 根节点) {
    if (!root)
        return nullptr;                        // 若 取反 根节点，直接返回 nullptr
    std::queue<NNode *> q;                     // std::队列 小于 NNode 乘 超过 节点;
    q.push(root);                              // 把 根节点 压入栈/数组尾部
    while (!q.empty()) {                       // 循环，直到不满足「取反 节点.empty(」
        int size = static_cast<int>(q.size()); // 把 static_cast 小于 int 超过 (节点.大小()) 存入 大小
        NNode *prev = nullptr;                 // 把 nullptr; 写入 NNode *prev
        for (int i = 0; i < size; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 大小 就继续
            auto *node = q.front();      // 把 节点.front(); 写入 auto *node
            q.pop();                     // 弹出栈顶元素
            if (prev)
                prev->next = node; // 若 前一个) 前一个 减 超过 下一个 赋值为 节点;
            prev = node;           // 把 节点; 写入 前一个
            if (node->left)
                q.push(node->left); // 若 节点 减 超过 左边界) 节点 追加 节点 减 超过 左边界);
            if (node->right)
                q.push(node->right); // 若 节点 减 超过 右边界) 节点 追加 节点 减 超过 右边界);
        }
    }
    return root; // 返回 根节点
}
int main() {                             // 程序入口：跑内嵌自测用例
    assert(connect(nullptr) == nullptr); // 断言校验
    auto *root = connect(
        buildNTree({1, 2, 3, 4, 5, 6, 7})); // 把 connect(buildNTree({1, 2, 3, 4, 5, 6, 7})); 写入 auto *root
    std::vector<std::vector<int>> levels;   // std::vector 小于 std::vector 小于 int 超过 超过 levels;
    auto *cur = root;                       // 把 根节点; 写入 auto *cur
    while (cur) {                           // 循环，直到不满足「当前值」
        std::vector<int> vals;              // std::vector 小于 int 超过 vals;
        for (auto *n = cur; n; n = n->next)
            vals.push_back(n->val);
        levels.push_back(vals); // levels 追加 vals);
        cur = cur->left;        // 把 当前值 减 超过 左边界; 写入 当前值
    }
    assert((levels == std::vector<std::vector<int>>{{1}, {2, 3}, {4, 5, 6, 7}})); // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
