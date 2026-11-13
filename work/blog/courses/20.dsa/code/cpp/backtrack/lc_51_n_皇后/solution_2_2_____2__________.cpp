// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133970744
// LeetCode 51. N皇后 — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <cmath>    // 引入头文件
#include <iostream> // 引入头文件
#include <string>   // 引入头文件
#include <vector>   // 引入头文件
static std::vector<std::vector<std::string>> solveNQueens(int n) {
    std::vector<std::vector<std::string>>
        res;                      // std::vector 小于 std::vector 小于 std::string 超过 超过 结果;
    std::vector<int> cols(n, -1); // std::vector 小于 int 超过 列数(元素个数, 减 1);
    std::function<void(int)> dfs =
        [&](int row) {      // 把 [ 按位与 ](int row) { 写入 std::function<void(int)> dfs
            if (row == n) { // 若 row 等于 元素个数
                std::vector<std::string> board; // std::vector 小于 std::string 超过 棋盘;
                for (int r = 0; r < n; ++r) { // 让 右指针 从 0 开始计数，右指针 小于 元素个数 就继续
                    std::string line(n, '.'); // std::string line(元素个数, '.');
                    line[cols[r]] = 'Q';      // 把 'Q'; 写入 line[cols[r]]
                    board.push_back(line);    // 棋盘 追加 line);
                }
                res.push_back(board); // 结果 追加 棋盘);
                return;               // return;
            }
            for (int col = 0; col < n; ++col) { // 让 col 从 0 开始计数，col 小于 元素个数 就继续
                bool valid = true;              // 把 true 存入 valid
                for (int r = 0; r < row; ++r) { // 让 右指针 从 0 开始计数，右指针 小于 row 就继续
                    if (cols[r] == col || std::abs(r - row) == std::abs(cols[r] - col)) {
                        valid = false;
                        break;
                    }
                }
                if (valid) {         // 若 valid
                    cols[row] = col; // 把 col; 写入 cols[row]
                    dfs(row + 1);    // dfs(row 加 1);
                    cols[row] = -1;  // 把 减 1; 写入 cols[row]
                }
            }
        };
    dfs(0);     // dfs(0);
    return res; // 返回 结果
}
int main() {                    // 程序入口：跑内嵌自测用例
    auto got = solveNQueens(4); // 把 solveNQueens(4) 存入 got
    assert(got.size() == 2);    // 断言校验
    assert((got[0] == std::vector<std::string>{".Q..", "...Q", "Q...", "..Q."})); // 断言校验
    assert(solveNQueens(1).size() == 1);                                          // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
