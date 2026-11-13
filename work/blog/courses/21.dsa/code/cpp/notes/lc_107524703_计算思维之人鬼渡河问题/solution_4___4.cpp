// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
// LeetCode 107524703. 人鬼渡河问题 — C++ 版（方案4：方向入状态的 DFS 变体，断言无可行路径）
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

    std::function<bool(int, int, int, int)> jump = [&](int dir, int r, int g, int step) -> bool {
        if (r == 0 && g == 0 && step % 2 == 0)
            return true; // 若 右指针 等于 0 且 g 等于 0 且 步数 对…取模 2 等于 0，直接返回 true
        std::string key = std::to_string(r) + "," + std::to_string(g) + "," + std::to_string(step % 2);
        if (visited.count(key))
            return false;                   // 若 已访问集合.计数(key)，直接返回 false
        visited.insert(key);                // 已访问集合 插入 key);
        for (int i = 0; i < 5; ++i) {       // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
            int dr = D[i][0], dg = D[i][1]; // 把 D[下标 i][0], dg 赋值为 D[下标 i][1] 存入 dr
            int nr = r + dir * dr;          // 把 右指针 加 dir 乘 dr 存入 nr
            int ng = g + dir * dg;          // 把 g 加 dir 乘 dg 存入 ng
            if (!safe(nr, ng))
                continue;                       // 若 取反 safe(nr, ng)) continue;
            if (jump(-dir, nr, ng, step + 1)) { // 若 jump( 减 dir, nr, ng, 步数 加 1
                path.push_back({dr, dg});       // 当前路径 追加 {dr, dg});
                return true;                    // 返回 true
            }
        }
        return false; // 返回 false
    };

    jump(-1, 3, 3, 0);                      // jump( 减 1, 3, 3, 0);
    std::reverse(path.begin(), path.end()); // std::reverse(当前路径 迭代位置 , 当前路径.终点());
    return path;                            // 返回 当前路径
}

int main() { // 程序入口：跑内嵌自测用例
    /* 与 TS 原文件一致：该变体断言返回空路径（parity 约束下无解） */
    std::vector<std::vector<int>> got = solve(); // 把 solve(); 写入 std::vector<std::vector<int>> got
    if (!got.empty()) {
        std::cout << "FAIL: got " << got.size() << " moves" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
