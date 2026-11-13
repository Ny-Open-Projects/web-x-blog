/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134204437 */
/* LeetCode 79. 单词搜索 — C 版（方案1） */
#include <stdio.h>                    // 引入头文件
#include <string.h>                   // 引入头文件
static char board_g[8][8];            // static char board_g[8][8];
static int rows_g, cols_g;            // static int rows_g, cols_g;
static const char *w_g;               // static const char 乘 w_g;
static int dfs(int i, int j, int k) { // 定义函数/方法 dfs
    if (w_g[k] == '\0')
        return 1; // 若 w_g[下标 k] 等于 '\0'，直接返回 1
    if (i < 0 || i >= rows_g || j < 0 || j >= cols_g)
        return 0;
    if (board_g[i][j] != w_g[k])
        return 0;               // 若 board_g[下标 i][下标 j] 不等于 w_g[下标 k]，直接返回 0
    char saved = board_g[i][j]; // 把 board_g[下标 i][下标 j]; 写入 char saved
    board_g[i][j] = '#';        // 把 '#'; 写入 board_g[i][j]
    int found = dfs(i + 1, j, k + 1) || dfs(i - 1, j, k + 1) || dfs(i, j + 1, k + 1) || dfs(i, j - 1, k + 1);
    board_g[i][j] = saved; // 把 saved; 写入 board_g[i][j]
    return found;          // 返回 found
}
static int exist(char board[][8], int rows, int cols, const char *word) { // 定义函数/方法 exist
    rows_g = rows;
    cols_g = cols;
    w_g = word;                    // 把 行数; cols_g 赋值为 列数; w_g 赋值为 单词; 写入 rows_g
    for (int i = 0; i < rows; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 行数 就继续
        for (int j = 0; j < cols; j++)   // 让 下标 j 从 0 开始计数，下标 j 小于 列数 就继续
            board_g[i][j] = board[i][j]; // 把 棋盘[下标 i][下标 j]; 写入 board_g[i][j]
    for (int i = 0; i < rows; i++)       // 让 下标 i 从 0 开始计数，下标 i 小于 行数 就继续
        for (int j = 0; j < cols; j++)   // 让 下标 j 从 0 开始计数，下标 j 小于 列数 就继续
            if (dfs(i, j, 0))
                return 1; // 若 dfs(下标 i, 下标 j, 0)，直接返回 1
    return 0;             // 返回 0
}
int main(void) { // 程序入口：跑内嵌自测用例
    char b[3][8] = {{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}};
    if (!exist(b, 3, 4, "ABCCED")) {
        printf("FAIL 1\n");
        return 1;
    } // 若 取反 exist(b, 3, 4, 「ABCCED」)) { 输出「ABCCED」); return 1; }
    if (!exist(b, 3, 4, "SEE")) {
        printf("FAIL 2\n");
        return 1;
    } // 若 取反 exist(b, 3, 4, 「SEE」)) { 输出「SEE」); return 1; }
    if (exist(b, 3, 4, "ABCB")) {
        printf("FAIL 3\n");
        return 1;
    }                 // 若 exist(b, 3, 4, 「ABCB」)) { 输出「ABCB」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
