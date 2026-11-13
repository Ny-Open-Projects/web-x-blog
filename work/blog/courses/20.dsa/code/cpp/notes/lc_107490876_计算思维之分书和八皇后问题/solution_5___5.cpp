// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — C++ 版（方案5：八皇后布尔数组标记，行号 0..n-1）
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

static std::vector<std::vector<int>> n_queens_bool(int n) {
    std::vector<int> col_row(n, 0);           // std::vector 小于 int 超过 col_row(元素个数, 0);
    std::vector<bool> rows(n, true);          // std::vector 小于 bool 超过 行数(元素个数, true);
    std::vector<bool> diag1(2 * n - 1, true); // std::vector 小于 bool 超过 diag1(2 乘 元素个数 减 1, true);
    std::vector<bool> diag2(2 * n - 1, true); // std::vector 小于 bool 超过 diag2(2 乘 元素个数 减 1, true);
    int offset = n - 1;                       // 把 元素个数 减 1 存入 offset
    std::vector<std::vector<int>> results; // std::vector 小于 std::vector 小于 int 超过 超过 results;

    std::function<void(int)> place =
        [&](int col) {      // 把 [ 按位与 ](int col) { 写入 std::function<void(int)> place
            if (col == n) { // 若 col 等于 元素个数
                results.push_back(col_row); // results 追加 col_row);
                return;                     // return;
            }
            for (int row = 0; row < n; ++row) { // 让 row 从 0 开始计数，row 小于 元素个数 就继续
                int d1 = col - row + offset;    // 把 col 减 row 加 offset 存入 d1
                int d2 = col + row;             // 把 col 加 row 存入 d2
                if (rows[row] && diag1[d1] && diag2[d2]) { // 若 行数[row] 且 diag1[d1] 且 diag2[d2]
                    col_row[col] = row;                    // 把 row; 写入 col_row[col]
                    rows[row] = false;                     // 把 false; 写入 rows[row]
                    diag1[d1] = false;                     // 把 false; 写入 diag1[d1]
                    diag2[d2] = false;                     // 把 false; 写入 diag2[d2]
                    place(col + 1);                        // place(col 加 1);
                    rows[row] = true;                      // 把 true; 写入 rows[row]
                    diag1[d1] = true;                      // 把 true; 写入 diag1[d1]
                    diag2[d2] = true;                      // 把 true; 写入 diag2[d2]
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
        {8, 92, true, {0, 4, 7, 5, 2, 6, 1, 3}},
        {1, 1, true, {0}},
        {2, 0, false, {}},
        {4, 2, true, {1, 3, 0, 2}},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) { // 让 idx 从 0 开始计数，idx 小于 cases.大小() 就继续
        auto sols = n_queens_bool(cases[idx].n); // 把 n_queens_bool(cases[idx].元素个数) 存入 sols
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
