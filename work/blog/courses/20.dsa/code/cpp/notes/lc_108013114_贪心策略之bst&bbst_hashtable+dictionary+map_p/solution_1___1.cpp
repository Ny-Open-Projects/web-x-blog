// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108013114
// LeetCode 108013114. 贪心策略之BST&BBST_hashtable+dictionary+map — C++ 版（贪心策略之
// BST/BBST/哈希表：Kruskal 最小生成树（并查集 + 排序））
#include <algorithm>     // 引入头文件
#include <iostream>      // 引入头文件
#include <unordered_map> // 引入头文件
#include <vector>        // 引入头文件

static std::unordered_map<int, int> parent; // static std::unordered_map 小于 int, int 超过 parent;

static int find(int x) { // 定义函数/方法 find
    if (parent.find(x) == parent.end())
        parent[x] = x;                 // 若 parent 查找 x) 等于 parent.终点()) parent[x] 赋值为 x;
    while (parent[x] != x) {           // 循环，直到不满足「parent[x] 不等于 x」
        parent[x] = parent[parent[x]]; // 把 parent[parent[x]]; 写入 parent[x]
        x = parent[x];                 // 把 parent[x]; 写入 x
    }
    return x; // 返回 x
}

static int kruskal_mst(std::vector<std::vector<int>> edges) { // 定义函数/方法 kruskal_mst
    std::sort(edges.begin(), edges.end(),
              [](const std::vector<int> &a, const std::vector<int> &b) { return a[2] < b[2]; });
    parent.clear();                       // parent.clear();
    int total = 0;                        // 把 0 存入 总和
    for (const auto &e : edges) {         // 逐个取出 边集 的元素（e）
        int u = e[0], v = e[1], w = e[2]; // 把 e[0], 值 赋值为 e[1], 权重 赋值为 e[2] 存入 节点 u
        int ru = find(u), rv = find(v);   // 把 find(节点 u), rv 赋值为 find(值) 存入 ru
        if (ru != rv) {                   // 若 ru 不等于 rv
            parent[ru] = rv;              // 把 rv; 写入 parent[ru]
            total += w;                   // 总和累加 权重
        }
    }
    return total; // 返回 总和
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::pair<std::vector<std::vector<int>>, int>> cases = {
        {{{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}}, 19},
        {{{0, 1, 1}, {1, 2, 2}, {2, 3, 3}, {3, 4, 4}}, 10},
        {{{0, 1, 2}, {1, 2, 3}}, 5},
        {{}, 0},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) { // 让 idx 从 0 开始计数，idx 小于 cases.大小() 就继续
        int got = kruskal_mst(cases[idx].first); // 把 kruskal_mst(cases[idx].first) 存入 got
        if (got != cases[idx].second) {          // 若 got 不等于 cases[idx].second
            std::cout << "case " << idx << " failed: got " << got << " want " << cases[idx].second
                      << std::endl; // 打印输出
            return 1;               // 返回 1
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
