// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133651611
// LeetCode 133651611. 图及其深度和广度优先遍历实现 — C++ 版（方案4）
#include <iostream> // 引入头文件
#include <map>      // 引入头文件
#include <queue>    // 引入头文件
#include <set>      // 引入头文件
#include <vector>   // 引入头文件

class Graph {                        // 定义类型
  public:                            // public:
    void addEdge(int from, int to) { // 定义函数/方法 addEdge
        adj_[from].push_back(to);    // adj_[from] 追加 to);
        adj_[to].push_back(from);    // adj_[to] 追加 from);
    }

    std::vector<int> dfs(int start) const { // std::vector 小于 int 超过 dfs(int 起点) const {
        std::set<int> visited;              // std::set 小于 int 超过 已访问集合;
        std::vector<int> result;            // std::vector 小于 int 超过 结果;
        dfsHelper(start, visited, result);  // dfsHelper(起点, 已访问集合, 结果);
        return result;                      // 返回 结果
    }

    std::vector<int> bfs(int start) const { // std::vector 小于 int 超过 bfs(int 起点) const {
        std::set<int> visited;              // std::set 小于 int 超过 已访问集合;
        std::vector<int> result;            // std::vector 小于 int 超过 结果;
        std::queue<int> q;                  // std::队列 小于 int 超过 节点;
        q.push(start);                      // 把 起点 压入栈/数组尾部
        visited.insert(start);              // 已访问集合 插入 起点);
        while (!q.empty()) {                // 循环，直到不满足「取反 节点.empty(」
            int node = q.front();           // 把 节点.front() 存入 节点
            q.pop();                        // 弹出栈顶元素
            result.push_back(node);         // 结果 追加 节点);
            auto it = adj_.find(node);      // 把 adj_ 查找 节点) 存入 it
            if (it == adj_.end())
                continue;                       // 若 it 等于 adj_.终点()) continue;
            for (int neighbor : it->second) {   // for (int neighbor : it 减 超过 second) {
                if (!visited.count(neighbor)) { // 若 取反 已访问集合.计数(neighbor
                    visited.insert(neighbor);   // 已访问集合 插入 neighbor);
                    q.push(neighbor);           // 把 neighbor 压入栈/数组尾部
                }
            }
        }
        return result; // 返回 结果
    }

  private: // private:
    void dfsHelper(int node, std::set<int> &visited, std::vector<int> &result) const {
        if (visited.count(node))
            return;                // 若 已访问集合.计数(节点)) return;
        visited.insert(node);      // 已访问集合 插入 节点);
        result.push_back(node);    // 结果 追加 节点);
        auto it = adj_.find(node); // 把 adj_ 查找 节点) 存入 it
        if (it == adj_.end())
            return;                               // 若 it 等于 adj_.终点()) return;
        for (int neighbor : it->second) {         // for (int neighbor : it 减 超过 second) {
            dfsHelper(neighbor, visited, result); // dfsHelper(neighbor, 已访问集合, 结果);
        }
    }

    std::map<int, std::vector<int>> adj_; // std::映射表 小于 int, std::vector 小于 int 超过 超过 adj_;
};

static bool eq(const std::vector<int> &a, const std::vector<int> &b) { // 定义函数/方法 eq
    return a == b;                                                     // 返回 数组 等于 b
}

int main() { // 程序入口：跑内嵌自测用例
    // case 1: 方形图 0-1-3-2-0
    Graph g1;         // Graph g1;
    g1.addEdge(0, 1); // g1.addEdge(0, 1);
    g1.addEdge(0, 2); // g1.addEdge(0, 2);
    g1.addEdge(1, 3); // g1.addEdge(1, 3);
    g1.addEdge(2, 3); // g1.addEdge(2, 3);
    if (!eq(g1.dfs(0), {0, 1, 3, 2})) {
        std::cout << "FAILED case1 dfs(0)" << std::endl;
        return 1;
    }
    if (!eq(g1.bfs(0), {0, 1, 2, 3})) {
        std::cout << "FAILED case1 bfs(0)" << std::endl;
        return 1;
    }

    // case 2: 从另一节点出发
    if (!eq(g1.dfs(2), {2, 0, 1, 3})) {
        std::cout << "FAILED case2 dfs(2)" << std::endl;
        return 1;
    }
    if (!eq(g1.bfs(2), {2, 0, 3, 1})) {
        std::cout << "FAILED case2 bfs(2)" << std::endl;
        return 1;
    }

    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
