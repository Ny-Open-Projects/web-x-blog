// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133472893
// LeetCode 787. K站中转内最便宜的航班 — C++ 版（方案11）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件
static int findCheapestPrice(int n, const std::vector<std::vector<int>> &flights, int src, int dst,
                             int k) { // 定义函数/方法 findCheapestPrice
    const int INF = 0x3f3f3f3f;       // 把 0x3f3f3f3f; 写入 const int INF
    std::vector<int> dist(n, INF);    // std::vector 小于 int 超过 dist(元素个数, INF);
    dist[src] = 0;                    // 把 0; 写入 dist[src]
    for (int t = 0; t <= k; ++t) { // 让 另一字符串 从 0 开始计数，另一字符串 不超过 下标 k 就继续
        std::vector<int> nd = dist;           // 把 dist; 写入 std::vector<int> nd
        for (const auto &f : flights) {       // 逐个取出 flights 的元素（f）
            int u = f[0], v = f[1], w = f[2]; // 把 f[0], 值 赋值为 f[1], 权重 赋值为 f[2] 存入 节点 u
            if (dist[u] != INF && dist[u] + w < nd[v])
                nd[v] = dist[u] + w;
        }
        dist = nd; // 把 nd; 写入 dist
    }
    return dist[dst] == INF ? -1 : dist[dst]; // 返回 dist[dst] 等于 INF ? 减 1 : dist[dst]
}
int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::vector<int>> f = {{0, 1, 100}, {1, 2, 100}, {2, 0, 100}, {1, 3, 600}, {2, 3, 200}};
    assert(findCheapestPrice(4, f, 0, 3, 1) == 700); // 断言校验
    assert(findCheapestPrice(4, f, 0, 0, 1) == 0);   // 断言校验
    assert(findCheapestPrice(4, f, 0, 3, 2) == 400); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS