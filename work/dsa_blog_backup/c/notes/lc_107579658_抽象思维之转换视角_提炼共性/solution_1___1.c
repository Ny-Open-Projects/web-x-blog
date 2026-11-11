/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107579658
 * LeetCode 107579658. 转换视角，提炼共性 — C 版（抽象思维之转换视角：统一分书问题与八皇后的回溯框架）
 * queen=false: 分书问题（5人，like 偏好矩阵）; queen=true: 八皇后
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

static const int LIKE[5][5] = {
    // 把 { 写入 static const int LIKE[5][5]
    {0, 0, 1, 1, 0}, {1, 1, 0, 0, 1}, {0, 1, 1, 0, 1}, {0, 0, 0, 1, 0}, {0, 1, 0, 0, 1},
};

#define MAX_SIZE 8                // #define MAX_SIZE 8
static int queen_flag;            // static int queen_flag;
static int SIZE;                  // static int SIZE;
static int Q[MAX_SIZE];           // static int Q[MAX_SIZE];
static int rows[MAX_SIZE];        // static int 行数[MAX_SIZE];
static int diag1[2 * MAX_SIZE];   // static int diag1[2 乘 MAX_SIZE];
static int diag2[2 * MAX_SIZE];   // static int diag2[2 乘 MAX_SIZE];
static int results[64][MAX_SIZE]; // static int results[64][MAX_SIZE];
static int result_count;          // static int result_count;

static int is_valid(int row, int col) { // 定义判定函数 is_valid
    if (queen_flag)
        return 1;               // 若 queen_flag，直接返回 1
    return LIKE[row][col] == 1; // 返回 LIKE[row][col] 等于 1
}

static int is_safe(int row, int col) { // 定义判定函数 is_safe
    if (queen_flag)
        return rows[row] && diag1[col - row + SIZE - 1] && diag2[col + row];
    return rows[row]; // 返回 行数[row]
}

static void place(int col) { // 定义函数/方法 place
    if (col == SIZE) {       // 若 col 等于 SIZE
        memcpy(results[result_count], Q,
               sizeof(int) * SIZE); // memcpy(results[result_count], Q, sizeof(int) 乘 SIZE);
        result_count++;             // result_count 加一
        return;                     // return;
    }
    for (int row = 0; row < SIZE; row++) { // 让 row 从 0 开始计数，row 小于 SIZE 就继续
        if (!is_valid(row, col))
            continue; // 若 取反 is_valid(row, col)) continue;
        if (!is_safe(row, col))
            continue;                        // 若 取反 is_safe(row, col)) continue;
        Q[col] = row;                        // 把 row; 写入 Q[col]
        rows[row] = 0;                       // 把 0; 写入 rows[row]
        if (queen_flag) {                    // 若 queen_flag
            diag1[col - row + SIZE - 1] = 0; // 把 0; 写入 diag1[col - row + SIZE - 1]
            diag2[col + row] = 0;            // 把 0; 写入 diag2[col + row]
        }
        place(col + 1);                      // place(col 加 1);
        rows[row] = 1;                       // 把 1; 写入 rows[row]
        if (queen_flag) {                    // 若 queen_flag
            diag1[col - row + SIZE - 1] = 1; // 把 1; 写入 diag1[col - row + SIZE - 1]
            diag2[col + row] = 1;            // 把 1; 写入 diag2[col + row]
        }
    }
}

int main(void) { // 程序入口：跑内嵌自测用例
    int want[2][5] = {{1, 2, 0, 3, 4},
                      {1, 4, 0, 3, 2}}; // 把 {{1, 2, 0, 3, 4}, {1, 4, 0, 3, 2}}; 写入 int want[2][5]

    queen_flag = 0;                  // 把 0; 写入 queen_flag
    SIZE = 5;                        // 把 5; 写入 SIZE
    memset(rows, 1, sizeof(rows));   // memset(行数, 1, sizeof(行数));
    memset(diag1, 1, sizeof(diag1)); // memset(diag1, 1, sizeof(diag1));
    memset(diag2, 1, sizeof(diag2)); // memset(diag2, 1, sizeof(diag2));
    result_count = 0;                // 把 0; 写入 result_count
    place(0);                        // place(0);

    if (result_count != 2) {
        printf("FAIL count %d\n", result_count);
        return 1;
    }
    for (int i = 0; i < 2; i++)     // 让 下标 i 从 0 开始计数，下标 i 小于 2 就继续
        for (int j = 0; j < 5; j++) // 让 下标 j 从 0 开始计数，下标 j 小于 5 就继续
            if (results[i][j] != want[i][j]) { // 若 results[下标 i][下标 j] 不等于 want[下标 i][下标 j]
                printf("FAIL results[%d][%d]\n", i, j); // 打印输出
                return 1;                               // 返回 1
            }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
