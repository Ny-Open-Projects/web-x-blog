// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
// LeetCode 107524703. 人鬼渡河问题 — C++ 版（方案3：DFS+奇偶步求解）
#include <functional> // 引入头文件
#include <iostream>   // 引入头文件
#include <set>        // 引入头文件
#include <string>     // 引入头文件
#include <vector>     // 引入头文件

static const int D[5][2] = {{2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}};

static bool safe(int r, int g) { // 定义函数/方法 safe
    return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

static std::vector<std::vector<int>>
solve() { // static std::vector 小于 std::vector 小于 int 超过 超过 solve() {
    std::vector<std::vector<int>> path; // std::vector 小于 std::vector 小于 int 超过 超过 当前路径;
    std::set<std::string> visited;      // std::set 小于 std::string 超过 已访问集合;

    std::function<bool(int, int, int)> dfs = [&](int r, int g, int step) -> bool {
        if (r == 0 && g == 0)
            return true; // 若 右指针 等于 0 且 g 等于 0，直接返回 true
        std::string key = std::to_string(r) + "," + std::to_string(g) + "," + std::to_string(step % 2);
        if (visited.count(key))
            return false;                   // 若 已访问集合.计数(key)，直接返回 false
        visited.insert(key);                // 已访问集合 插入 key);
        bool odd = (step % 2 == 1);         // 把 (步数 对…取模 2 等于 1) 存入 odd
        for (int i = 0; i < 5; ++i) {       // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
            int dr = D[i][0], dg = D[i][1]; // 把 D[下标 i][0], dg 赋值为 D[下标 i][1] 存入 dr
            int nr, ng;                     // int nr, ng;
            if (odd) {                      // 若 odd
                if (r < dr || g < dg)
                    continue; // 若 右指针 小于 dr 或 g 小于 dg) continue;
                nr = r - dr;
                ng = g - dg; // 把 右指针 减 dr; ng 赋值为 g 减 dg; 写入 nr
            } else {         // 否则
                if ((3 - r) < dr || (3 - g) < dg)
                    continue; // 若 (3 减 右指针) 小于 dr 或 (3 减 g) 小于 dg) continue;
                nr = r + dr;
                ng = g + dg; // 把 右指针 加 dr; ng 赋值为 g 加 dg; 写入 nr
            }
            if (!safe(nr, ng))
                continue;                 // 若 取反 safe(nr, ng)) continue;
            if (dfs(nr, ng, step + 1)) {  // 若 dfs(nr, ng, 步数 加 1
                path.push_back({dr, dg}); // 当前路径 追加 {dr, dg});
                return true;              // 返回 true
            }
        }
        return false; // 返回 false
    };

    dfs(3, 3, 1);                           // dfs(3, 3, 1);
    std::reverse(path.begin(), path.end()); // std::reverse(当前路径 迭代位置 , 当前路径.终点());
    return path;                            // 返回 当前路径
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::vector<int>> want = {
        // 把 { 写入 std::vector<std::vector<int>> want
        {1, 1}, {1, 0}, {0, 2}, {0, 1}, {2, 0}, {1, 1}, {2, 0}, {0, 1}, {0, 2}, {1, 0}, {1, 1},
    };
    std::vector<std::vector<int>> got = solve(); // 把 solve(); 写入 std::vector<std::vector<int>> got
    if (got != want) {
        std::cout << "solve mismatch" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
