// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133986698
// LeetCode 133. 克隆图 — C++ 版
#include <algorithm>  // 引入头文件
#include <cassert>    // 引入头文件
#include <functional> // 引入头文件
#include <iostream>   // 引入头文件
#include <map>        // 引入头文件
#include <queue>      // 引入头文件
#include <set>        // 引入头文件
#include <vector>     // 引入头文件

struct Node {                                  // 定义类型
    int val;                                   // int 值;
    std::vector<Node *> neighbors;             // std::vector 小于 Node 乘 超过 neighbors;
    explicit Node(int val_ = 0) : val(val_) {} // 把 0) : 值(val_) {} 写入 explicit Node(int val_
};

// 方案5（BFS，visited 以节点对象为键）
Node *cloneGraph(Node *node) { // Node 乘 cloneGraph(Node 乘 节点) {
    if (node == nullptr)
        return nullptr;                  // 若 节点 等于 nullptr，直接返回 nullptr
    std::map<Node *, Node *> visited;    // 以节点对象（指针）为键
    visited[node] = new Node(node->val); // 把 new Node(节点 减 超过 值); 写入 visited[node]
    std::queue<Node *> q;                // std::队列 小于 Node 乘 超过 节点;
    q.push(node);                        // 把 节点 压入栈/数组尾部
    while (!q.empty()) {                 // 循环，直到不满足「取反 节点.empty(」
        Node *n = q.front();             // 把 节点.front(); 写入 Node *n
        q.pop();                         // 弹出栈顶元素
        for (Node *ne : n->neighbors) {  // for (Node 乘 ne : 元素个数 减 超过 neighbors) {
            if (visited.find(ne) == visited.end()) { // 若 已访问集合 查找 ne) 等于 已访问集合.终点(
                q.push(ne);                          // 把 ne 压入栈/数组尾部
                visited[ne] = new Node(ne->val); // 把 new Node(ne 减 超过 值); 写入 visited[ne]
            }
            visited[n]->neighbors.push_back(
                visited[ne]); // 已访问集合[元素个数] 减 超过 neighbors 追加 已访问集合[ne]);
        }
    }
    return visited[node]; // 返回 已访问集合[节点]
}

Node *buildGraph(const std::vector<std::vector<int>> &adj) {
    std::vector<Node *> nodes; // std::vector 小于 Node 乘 超过 nodes;
    nodes.push_back(nullptr);  // 占位，下标从 1 开始
    for (int i = 1; i <= static_cast<int>(adj.size()); i++)
        nodes.push_back(new Node(i)); // nodes 追加 new Node(下标 i));
    for (int idx = 1; idx <= static_cast<int>(adj.size());
         idx++) // 让 idx 从 1 开始计数，idx 不超过 static_cast 小于 int 超过 (邻接表.大小()) 就继续
        for (int nb : adj[idx - 1])                     // for (int nb : 邻接表[idx 减 1])
            nodes[idx]->neighbors.push_back(nodes[nb]); // nodes[idx] 减 超过 neighbors 追加 nodes[nb]);
    return nodes[1];                                    // 返回 nodes[1]
}

// 收集签名：每个节点的邻居值列表（排序后），按节点 val 键控
std::map<int, std::vector<int>> signature(Node *node) {
    std::map<int, std::vector<int>> vis; // std::映射表 小于 int, std::vector 小于 int 超过 超过 vis;
    std::function<void(Node *)> dfs =
        [&](Node *n) { // 把 [ 按位与 ](Node 乘 元素个数) { 写入 std::function<void(Node *)> dfs
            if (vis.count(n->val))
                return;            // 若 vis.计数(元素个数 减 超过 值)) return;
            std::vector<int> vals; // std::vector 小于 int 超过 vals;
            for (Node *x : n->neighbors)
                vals.push_back(
                    x->val); // for (Node 乘 x : 元素个数 减 超过 neighbors) vals 追加 x 减 超过 值);
            std::sort(vals.begin(), vals.end()); // std::sort(vals 迭代位置 , vals.终点());
            vis[n->val] = vals;                  // 把 vals; 写入 vis[n->val]
            for (Node *x : n->neighbors)
                dfs(x); // for (Node 乘 x : 元素个数 减 超过 neighbors) dfs(x);
        };
    dfs(node);  // dfs(节点);
    return vis; // 返回 vis
}

void freeGraph(Node *node) { // 定义函数/方法 freeGraph
    if (node == nullptr)
        return; // 若 节点 等于 nullptr) return;
    // 先收集全部节点，再统一释放
    std::vector<Node *> order;                  // std::vector 小于 Node 乘 超过 order;
    std::set<Node *> seen;                      // std::set 小于 Node 乘 超过 已见集合;
    order.push_back(node);                      // order 追加 节点);
    seen.insert(node);                          // 已见集合 插入 节点);
    for (size_t i = 0; i < order.size(); i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 order.大小() 就继续
        for (Node *nb : order[i]->neighbors) { // for (Node 乘 nb : order[下标 i] 减 超过 neighbors) {
            if (seen.insert(nb).second)
                order.push_back(nb); // 若 已见集合 插入 nb).second) order 追加 nb);
        }
    }
    for (Node *n : order)
        delete n; // for (Node 乘 元素个数 : order) delete 元素个数;
}

int main() { // 程序入口：跑内嵌自测用例
    Node *root = buildGraph({{2, 4}, {1, 3}, {2, 4}, {1, 3}});
    Node *cloned = cloneGraph(root);                         // 把 cloneGraph(根节点); 写入 Node *cloned
    assert(cloned != nullptr && "cloneGraph returned null"); // 断言校验
    assert(cloned != root && "not a deep copy (same object)"); // 断言校验
    auto sig = signature(cloned);                              // 把 signature(cloned) 存入 sig
    std::map<int, std::vector<int>> expected = {
        // 把 { 写入 std::map<int, std::vector<int>> expected
        {1, {2, 4}},
        {2, {1, 3}},
        {3, {2, 4}},
        {4, {1, 3}}};                 // {1, {2, 4}}, {2, {1, 3}}, {3, {2, 4}}, {4, {1, 3}}};
    for (const auto &kv : expected) { // 逐个取出 expected 的元素（kv）
        assert(sig.count(kv.first) && "signature mismatch");        // 断言校验
        assert(sig[kv.first] == kv.second && "signature mismatch"); // 断言校验
    }
    freeGraph(cloned);                // freeGraph(cloned);
    freeGraph(root);                  // freeGraph(根节点);
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
