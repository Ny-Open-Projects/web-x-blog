// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134204437
// LeetCode 79. 单词搜索 — C++ 版（方案1）
#include <cassert>                                                                 // 引入头文件
#include <iostream>                                                                // 引入头文件
#include <string>                                                                  // 引入头文件
#include <vector>                                                                  // 引入头文件
static bool exist(std::vector<std::vector<char>> board, const std::string &word) { // 定义函数/方法 exist
    int rows = static_cast<int>(board.size()), cols = static_cast<int>(board[0].size());
    std::function<bool(int, int, int)> dfs = [&](int i, int j, int k) -> bool {
        if (k == static_cast<int>(word.size()))
            return true; // 若 下标 k 等于 static_cast 小于 int 超过 (单词.大小())，直接返回 true
        if (i < 0 || i >= rows || j < 0 || j >= cols || board[i][j] != word[k])
            return false;
        char saved = board[i][j]; // 把 棋盘[下标 i][下标 j]; 写入 char saved
        board[i][j] = '#';        // 把 '#'; 写入 board[i][j]
        bool found =
            dfs(i + 1, j, k + 1) || dfs(i - 1, j, k + 1) || dfs(i, j + 1, k + 1) || dfs(i, j - 1, k + 1);
        board[i][j] = saved; // 把 saved; 写入 board[i][j]
        return found;        // 返回 found
    };
    for (int i = 0; i < rows; ++i)     // 让 下标 i 从 0 开始计数，下标 i 小于 行数 就继续
        for (int j = 0; j < cols; ++j) // 让 下标 j 从 0 开始计数，下标 j 小于 列数 就继续
            if (dfs(i, j, 0))
                return true; // 若 dfs(下标 i, 下标 j, 0)，直接返回 true
    return false;            // 返回 false
}
int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::vector<char>> b = {{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}};
    assert(exist(b, "ABCCED"));       // 断言校验
    assert(exist(b, "SEE"));          // 断言校验
    assert(!exist(b, "ABCB"));        // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
