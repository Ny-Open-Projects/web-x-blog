/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134045157 */
/* LeetCode 37. 解数独 — C 版（方案3） */
#include <stdio.h>                                       // 引入头文件
#include <string.h>                                      // 引入头文件
static int valid(char b[9][10], int r, int c, char ch) { // 定义函数/方法 valid
    for (int i = 0; i < 9; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 9 就继续
        if (b[r][i] == ch || b[i][c] == ch)
            return 0; // 若 b[右指针][下标 i] 等于 字符 或 b[下标 i][字符] 等于 字符，直接返回 0
    }
    int br = r / 3 * 3, bc = c / 3 * 3; // 把 右指针 除以 3 乘 3, bc 赋值为 字符 除以 3 乘 3 存入 br
    for (int i = br; i < br + 3; i++) // 让 下标 i 从 br 开始计数，下标 i 小于 br 加 3 就继续
        for (int j = bc; j < bc + 3; j++) // 让 下标 j 从 bc 开始计数，下标 j 小于 bc 加 3 就继续
            if (b[i][j] == ch)
                return 0; // 若 b[下标 i][下标 j] 等于 字符，直接返回 0
    return 1;             // 返回 1
}
static int dfs(char b[9][10]) {       // 定义函数/方法 dfs
    for (int r = 0; r < 9; r++) {     // 让 右指针 从 0 开始计数，右指针 小于 9 就继续
        for (int c = 0; c < 9; c++) { // 让 字符 从 0 开始计数，字符 小于 9 就继续
            if (b[r][c] == '.') {     // 若 b[右指针][字符] 等于 '.'
                for (char ch = '1'; ch <= '9';
                     ch++) { // 把 '1'; 字符 不超过 '9'; 字符 加一 ) { 写入 for (char ch
                    if (valid(b, r, c, ch)) { // 若 valid(b, 右指针, 字符, 字符
                        b[r][c] = ch;         // 把 字符; 写入 b[r][c]
                        if (dfs(b))
                            return 1;  // 若 dfs(b)，直接返回 1
                        b[r][c] = '.'; // 把 '.'; 写入 b[r][c]
                    }
                }
                return 0; // 返回 0
            }
        }
    }
    return 1; // 返回 1
}
static void solve_sudoku(char b[9][10]) { dfs(b); } // static void solve_sudoku(char b[9][10]) { dfs(b); }
int main(void) {                                    // 程序入口：跑内嵌自测用例
    char board[9][10] = {
        // 把 { 写入 char board[9][10]
        "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1",
        "7...2...6", ".6....28.", "...419..5", "....8..79",
    };
    solve_sudoku(board); // solve_sudoku(棋盘);
    const char *solved[] = {
        // 把 { 写入 const char *solved[]
        "534678912", "672195348", "198342567", "859761423", "426853791",
        "713924856", "961537284", "287419635", "345286179",
    };
    for (int r = 0; r < 9; r++) { // 让 右指针 从 0 开始计数，右指针 小于 9 就继续
        if (strcmp(board[r], solved[r]) != 0) {
            printf("FAIL row %d\n", r);
            return 1;
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
