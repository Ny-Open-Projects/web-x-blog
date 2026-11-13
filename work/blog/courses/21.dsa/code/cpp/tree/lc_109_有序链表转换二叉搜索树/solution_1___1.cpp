// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135270549
// LeetCode 109. 有序链表转换二叉搜索树 — C++ 版（方案1）
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

struct ListNode {   // 定义类型
    int val;        // int 值;
    ListNode *next; // ListNode 乘 下一个;
    explicit ListNode(int v)
        : val(v), next(nullptr) {} // explicit ListNode(int 值) : 值(值), 下一个(nullptr) {}
};
static ListNode *buildList(const std::vector<int> &vals) {
    ListNode dummy(0);               // ListNode 哨兵节点(0);
    ListNode *cur = &dummy;          // 把 按位与 哨兵节点; 写入 ListNode *cur
    for (int v : vals) {             // for (int 值 : vals) {
        cur->next = new ListNode(v); // 把 new ListNode(值); 写入 cur->next
        cur = cur->next;             // 把 当前值 减 超过 下一个; 写入 当前值
    }
    return dummy.next; // 返回 哨兵节点.下一个
}
static TreeNode *buildBst(const std::vector<int> &nodes, int left, int right) {
    if (left > right)
        return nullptr;                  // 若 左边界 超过 右边界，直接返回 nullptr
    int mid = left + (right - left) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2 存入 中点
    auto *root = new TreeNode(nodes[mid]);       // 把 new TreeNode(nodes[中点]); 写入 auto *root
    root->left = buildBst(nodes, left, mid - 1); // 把 buildBst(nodes, 左边界, 中点 减 1); 写入 root->left
    root->right = buildBst(nodes, mid + 1, right); // 把 buildBst(nodes, 中点 加 1, 右边界); 写入 root->right
    return root;                                   // 返回 根节点
}
static TreeNode *sortedListToBST(ListNode *head) { // static TreeNode 乘 sortedListToBST(ListNode 乘 头节点) {
    std::vector<int> nodes;                        // std::vector 小于 int 超过 nodes;
    for (ListNode *c = head; c; c = c->next)
        nodes.push_back(c->val);
    if (nodes.empty())
        return nullptr; // 若 nodes 是否为空，直接返回 nullptr
    return buildBst(nodes, 0, static_cast<int>(nodes.size()) - 1);
}
static void inorder(TreeNode *n, std::vector<int> &out) { // 定义函数/方法 inorder
    if (!n)
        return;             // 若 取反 元素个数) return;
    inorder(n->left, out);  // inorder(元素个数 减 超过 左边界, out);
    out.push_back(n->val);  // out 追加 元素个数 减 超过 值);
    inorder(n->right, out); // inorder(元素个数 减 超过 右边界, out);
}
int main() {                                         // 程序入口：跑内嵌自测用例
    assert(sortedListToBST(nullptr) == nullptr);     // 断言校验
    auto *t = sortedListToBST(buildList({1, 2, 3})); // 把 sortedListToBST(buildList({1, 2, 3})); 写入 auto *t
    std::vector<int> out;                            // std::vector 小于 int 超过 out;
    inorder(t, out);                                 // inorder(另一字符串, out);
    assert((out == std::vector<int>{1, 2, 3}));      // 断言校验
    assert(t->val == 2 && t->left->val == 1 && t->right->val == 3); // 断言校验
    std::cout << "PASS" << std::endl;                               // 全部用例通过，输出 PASS
    return 0;                                                       // 返回 0
}
