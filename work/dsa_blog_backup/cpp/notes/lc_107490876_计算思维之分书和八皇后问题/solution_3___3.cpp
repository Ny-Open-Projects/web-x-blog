// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — C++ 版（方案3：八皇后递归 isSafe，行号 1..n）
#include <cmath>    // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

static std::vector<std::vector<int>> n_queens_safe(int n) {
    std::vector<std::vector<int>> results; // std::vector 小于 std::vector 小于 int 超过 超过 results;
    std::vector<int> board(n, 0);          // std::vector 小于 int 超过 棋盘(元素个数, 0);

    std::function<bool(int, int)> is_safe = [&](int col, int row) {
        for (int c = 0; c < col; ++c) { // 让 字符 从 0 开始计数，字符 小于 col 就继续
            if (board[c] == row || std::abs(board[c] - row) == std::abs(c - col))
                return false;
        }
        return true; // 返回 true
    };

    std::function<void(int)> place =
        [&](int col) {      // 把 [ 按位与 ](int col) { 写入 std::function<void(int)> place
            if (col == n) { // 若 col 等于 元素个数
                results.push_back(board); // results 追加 棋盘);
                return;                   // return;
            }
            for (int row = 1; row <= n; ++row) { // 让 row 从 1 开始计数，row 不超过 元素个数 就继续
                if (is_safe(col, row)) {         // 若 is_safe(col, row
                    board[col] = row;            // 把 row; 写入 board[col]
                    place(col + 1);              // place(col 加 1);
                }
            }
        };

    place(0);       // place(0);
    return results; // 返回 results
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
        {8, 92, true, {1, 5, 8, 6, 3, 7, 2, 4}},
        {1, 1, true, {1}},
        {2, 0, false, {}},
        {4, 2, true, {2, 4, 1, 3}},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) { // 让 idx 从 0 开始计数，idx 小于 cases.大小() 就继续
        auto sols = n_queens_safe(cases[idx].n); // 把 n_queens_safe(cases[idx].元素个数) 存入 sols
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
