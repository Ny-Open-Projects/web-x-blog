// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108717090
// 减治策略之详解Dijkstra算法 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> dijkstraShortest(const std::vector<std::vector<std::pair<int, int>>> &graph,
                                         int start) {
    size_t n = graph.size();              // 把 graph.大小(); 写入 size_t n
    std::vector<int> dist(n, 0x3f3f3f3f); // std::vector 小于 int 超过 dist(元素个数, 0x3f3f3f3f);
    std::vector<bool> visited(n, false); // std::vector 小于 bool 超过 已访问集合(元素个数, false);
    dist[start] = 0;                     // 把 0; 写入 dist[start]
    while (true) {                       // 循环，直到不满足「true」
        int u = -1;                      // 把 减 1 存入 节点 u
        for (size_t i = 0; i < n; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
            if (!visited[i] && (u < 0 || dist[i] < dist[u]))
                u = static_cast<int>(i);
        }
        if (u < 0 || dist[u] == 0x3f3f3f3f)
            break;                      // 若 节点 u 小于 0 或 dist[节点 u] 等于 0x3f3f3f3f) break;
        visited[u] = true;              // 把 true; 写入 visited[u]
        for (auto &[v, w] : graph[u]) { // for (auto 按位与 [值, 权重] : graph[节点 u]) {
            if (dist[u] + w < dist[v])
                dist[v] = dist[u] +
                          w; // 若 dist[节点 u] 加 权重 小于 dist[值]) dist[值] 赋值为 dist[节点 u] 加 权重;
        }
    }
    return dist; // 返回 dist
}
int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::vector<std::pair<int, int>>> g = {
        // 把 { 写入 std::vector<std::vector<std::pair<int, int>>> g
        {{1, 10}, {2, 3}},
        {{2, 1}, {3, 2}},
        {{1, 4}, {3, 8}},
        {{4, 7}},
        {} // {{1,10},{2,3}}, {{2,1},{3,2}}, {{1,4},{3,8}}, {{4,7}}, {}
    };
    auto d = dijkstraShortest(g, 0); // 把 dijkstraShortest(g, 0) 存入 d
    assert(d[0] == 0 && d[1] == 7 && d[2] == 3 && d[3] == 9 && d[4] == 16); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS