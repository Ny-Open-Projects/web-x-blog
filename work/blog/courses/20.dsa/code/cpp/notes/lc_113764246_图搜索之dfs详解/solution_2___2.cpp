// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113764246
// 图搜索之DFS详解 — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static void dfsGo(size_t c, const std::vector<std::vector<int>> &graph, std::vector<bool> &visited,
                  std::vector<int> &order) {
    visited[c] = true;                    // 把 true; 写入 visited[c]
    order.push_back(static_cast<int>(c)); // order 追加 static_cast 小于 int 超过 (字符));
    for (int nx : graph[c]) {             // for (int nx : graph[字符]) {
        if (!visited[nx])
            dfsGo(static_cast<size_t>(nx), graph, visited, order);
    }
}
int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::vector<int>> g = {{1, 2}, {3, 4}, {5}, {}, {}, {}};
    std::vector<bool> visited(g.size(), false); // std::vector 小于 bool 超过 已访问集合(g.大小(), false);
    std::vector<int> order;                     // std::vector 小于 int 超过 order;
    dfsGo(0, g, visited, order);                // dfsGo(0, g, 已访问集合, order);
    assert((order == std::vector<int>{0, 1, 3, 4, 2, 5})); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS