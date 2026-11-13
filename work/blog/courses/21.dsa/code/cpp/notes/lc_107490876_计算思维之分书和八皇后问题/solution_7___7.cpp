// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — C++ 版（方案7：八皇后位置对列表）
#include <cmath>    // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

static std::vector<std::vector<int>> n_queens_simple(int n) {
    std::vector<std::pair<int, int>>
        positions; // std::vector 小于 std::pair 小于 int, int 超过 超过 positions;
    std::vector<std::vector<int>> solutions; // std::vector 小于 std::vector 小于 int 超过 超过 solutions;

    std::function<bool(int, int)> safe = [&](int r, int c) {
        for (const auto &p : positions) { // 逐个取出 positions 的元素（节点）
            if (p.first == r || std::abs(p.first - r) == std::abs(p.second - c))
                return false;
        }
        return true; // 返回 true
    };

    std::function<void(int)> solve =
        [&](int col) {                 // 把 [ 按位与 ](int col) { 写入 std::function<void(int)> solve
            if (col == n) {            // 若 col 等于 元素个数
                std::vector<int> rows; // std::vector 小于 int 超过 行数;
                for (const auto &p : positions)
                    rows.push_back(p.first); // 逐个取出 positions 的元素（节点）
                solutions.push_back(rows);   // solutions 追加 行数);
                return;                      // return;
            }
            for (int r = 0; r < n; ++r) { // 让 右指针 从 0 开始计数，右指针 小于 元素个数 就继续
                if (safe(r, col)) {                // 若 safe(右指针, col
                    positions.push_back({r, col}); // positions 追加 {右指针, col});
                    solve(col + 1);                // solve(col 加 1);
                    positions.pop_back();          // 弹出栈顶元素
                }
            }
        };

    solve(0);         // solve(0);
    return solutions; // 返回 solutions
}

int main() { // 程序入口：跑内嵌自测用例
    struct Case {
        int n;
        int count;
        bool has_first;
        std::vector<int> first;
    }; // 定义类型
    std::vector<Case> cases = {
        // 把 { 写入 std::vector<Case> cases
        {8, 92, true, {0, 4, 7, 5, 2, 6, 1, 3}},
        {1, 1, true, {0}},
        {2, 0, false, {}},
        {4, 2, true, {1, 3, 0, 2}},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) { // 让 idx 从 0 开始计数，idx 小于 cases.大小() 就继续
        auto sols = n_queens_simple(cases[idx].n); // 把 n_queens_simple(cases[idx].元素个数) 存入 sols
        if (static_cast<int>(sols.size()) != cases[idx].count) {
            std::cout << "case " << idx << " count" << std::endl;
            return 1;
        }
        if (cases[idx].has_first && sols[0] != cases[idx].first) {
            std::cout << "case " << idx << " first" << std::endl;
            return 1;
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
