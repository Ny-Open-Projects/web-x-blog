// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113548046
// 图搜索之BFS详解 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <queue>    // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> bfsOrder(const std::vector<std::vector<int>> &graph, int start) {
    size_t n = graph.size();             // 把 graph.大小(); 写入 size_t n
    std::vector<bool> visited(n, false); // std::vector 小于 bool 超过 已访问集合(元素个数, false);
    std::vector<int> order;              // std::vector 小于 int 超过 order;
    std::queue<int> q;                   // std::队列 小于 int 超过 节点;
    visited[start] = true;               // 把 true; 写入 visited[start]
    q.push(start);                       // 把 起点 压入栈/数组尾部
    while (!q.empty()) {                 // 循环，直到不满足「取反 节点.empty(」
        int c = q.front();               // 把 节点.front() 存入 字符
        q.pop();                         // 弹出栈顶元素
        order.push_back(c);              // order 追加 字符);
        for (int nx : graph[c]) {        // for (int nx : graph[字符]) {
            if (!visited[nx]) {          // 若 取反 已访问集合[nx]
                visited[nx] = true;      // 把 true; 写入 visited[nx]
                q.push(nx);              // 把 nx 压入栈/数组尾部
            }
        }
    }
    return order; // 返回 order
}
int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::vector<int>> g = {{1, 2}, {3, 4}, {5}, {}, {}, {}};
    assert((bfsOrder(g, 0) == std::vector<int>{0, 1, 2, 3, 4, 5})); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS