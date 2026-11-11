// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134045157
// LeetCode 37. 解数独 — C++ 版（方案3）
#include <cassert>                                               // 引入头文件
#include <iostream>                                              // 引入头文件
#include <string>                                                // 引入头文件
#include <vector>                                                // 引入头文件
static void solveSudoku(std::vector<std::vector<char>> &board) { // 定义函数/方法 solveSudoku
    std::function<bool()> dfs =
        [&]() -> bool { // 把 [ 按位与 ]() 减 超过 bool { 写入 std::function<bool()> dfs
        for (int r = 0; r < 9; ++r) {     // 让 右指针 从 0 开始计数，右指针 小于 9 就继续
            for (int c = 0; c < 9; ++c) { // 让 字符 从 0 开始计数，字符 小于 9 就继续
                if (board[r][c] == '.') { // 若 棋盘[右指针][字符] 等于 '.'
                    for (char ch = '1'; ch <= '9';
                         ++ch) {        // 把 '1'; 字符 不超过 '9'; 加一 字符) { 写入 for (char ch
                        bool ok = true; // 把 true 存入 ok
                        for (int i = 0; i < 9 && ok;
                             ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 9 且 ok 就继续
                            if (board[r][i] == ch || board[i][c] == ch)
                                ok = false; // 若 棋盘[右指针][下标 i] 等于 字符 或 棋盘[下标 i][字符] 等于
                                            // 字符) ok 赋值为 false;
                        }
                        int br = r / 3 * 3,
                            bc = c / 3 * 3; // 把 右指针 除以 3 乘 3, bc 赋值为 字符 除以 3 乘 3 存入 br
                        for (int i = br; i < br + 3 && ok;
                             ++i) // 让 下标 i 从 br 开始计数，下标 i 小于 br 加 3 且 ok 就继续
                            for (int j = bc; j < bc + 3 && ok;
                                 ++j) // 让 下标 j 从 bc 开始计数，下标 j 小于 bc 加 3 且 ok 就继续
                                if (board[i][j] == ch)
                                    ok = false; // 若 棋盘[下标 i][下标 j] 等于 字符) ok 赋值为 false;
                        if (ok) {               // 若 ok
                            board[r][c] = ch; // 把 字符; 写入 board[r][c]
                            if (dfs())
                                return true;   // 若 dfs()，直接返回 true
                            board[r][c] = '.'; // 把 '.'; 写入 board[r][c]
                        }
                    }
                    return false; // 返回 false
                }
            }
        }
        return true; // 返回 true
    };
    dfs(); // dfs();
}
int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::vector<char>> board = {
        // 把 { 写入 std::vector<std::vector<char>> board
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'}, {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'}, {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'}, {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'}, {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'},
    };
    solveSudoku(board); // solveSudoku(棋盘);
    const char *solved[] = {
        // 把 { 写入 const char *solved[]
        "534678912", "672195348", "198342567", "859761423", "426853791",
        "713924856", "961537284", "287419635", "345286179",
    };
    for (int r = 0; r < 9; ++r) { // 让 右指针 从 0 开始计数，右指针 小于 9 就继续
        std::string line(board[r].begin(),
                         board[r].end()); // std::string line(棋盘[右指针] 迭代位置 , 棋盘[右指针].终点());
        assert(line == solved[r]); // 断言校验
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
