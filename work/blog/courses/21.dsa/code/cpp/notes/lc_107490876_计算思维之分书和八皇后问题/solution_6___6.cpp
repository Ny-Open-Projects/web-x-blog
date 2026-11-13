// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — C++ 版（方案6：八皇后不可变状态函数式）
#include <functional> // 引入头文件
#include <iostream>   // 引入头文件
#include <vector>     // 引入头文件

struct State {                // 定义类型
    std::vector<int> col_row; // std::vector 小于 int 超过 col_row;
    std::vector<bool> rows;   // std::vector 小于 bool 超过 行数;
    std::vector<bool> diag1;  // std::vector 小于 bool 超过 diag1;
    std::vector<bool> diag2;  // std::vector 小于 bool 超过 diag2;
};

static void place(int col, int n, State st, std::vector<std::vector<int>> &results) { // 定义函数/方法 place
    if (col == n) {                    // 若 col 等于 元素个数
        results.push_back(st.col_row); // results 追加 st.col_row);
        return;                        // return;
    }
    for (int row = 0; row < n; ++row) { // 让 row 从 0 开始计数，row 小于 元素个数 就继续
        int d1 = col - row + (n - 1);   // 把 col 减 row 加 (元素个数 减 1) 存入 d1
        int d2 = col + row;             // 把 col 加 row 存入 d2
        if (st.rows[row] && st.diag1[d1] && st.diag2[d2]) { // 若 st.行数[row] 且 st.diag1[d1] 且 st.diag2[d2]
            State ns = st;
                /* 值拷贝 = 不可变语义 */ // 把 st; 除以 乘 值拷贝 赋值为 不可变语义 乘 除以 写入 State ns
            ns.col_row.push_back(row);      // ns.col_row 追加 row);
            ns.rows[row] = false;           // 把 false; 写入 ns.rows[row]
            ns.diag1[d1] = false;           // 把 false; 写入 ns.diag1[d1]
            ns.diag2[d2] = false;           // 把 false; 写入 ns.diag2[d2]
            place(col + 1, n, ns, results); // place(col 加 1, 元素个数, ns, results);
        }
    }
}

static std::vector<std::vector<int>> n_queens_func(int n) {
    State init;                            // State init;
    init.col_row.reserve(n);               // init.col_row.reserve(元素个数);
    init.rows.assign(n, true);             // init.行数.assign(元素个数, true);
    init.diag1.assign(2 * n - 1, true);    // init.diag1.assign(2 乘 元素个数 减 1, true);
    init.diag2.assign(2 * n - 1, true);    // init.diag2.assign(2 乘 元素个数 减 1, true);
    std::vector<std::vector<int>> results; // std::vector 小于 std::vector 小于 int 超过 超过 results;
    place(0, n, init, results);            // place(0, 元素个数, init, results);
    return results;                        // 返回 results
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
        auto sols = n_queens_func(cases[idx].n); // 把 n_queens_func(cases[idx].元素个数) 存入 sols
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
