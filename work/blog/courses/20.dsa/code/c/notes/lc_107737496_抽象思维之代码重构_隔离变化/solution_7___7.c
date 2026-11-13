/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案7：螺旋矩阵分派表 place）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

typedef struct {                      // typedef struct {
    int row, col;                     // int row, col;
    char next_dir; /* 0 表示不变向 */ // char next_dir; 除以 乘 0 表示不变向 乘 除以
} Move;                               // } Move;

static Move place(int row, int col, char direction, int n, const int m[][8]) { // 定义函数/方法 place
    Move mv;                                                                   // Move mv;
    switch (direction) {                                                       // switch (direction) {
    case 'D':                                                                  // case 'D':
        if (row + 1 < n && m[row + 1][col] == 0) {
            mv.row = row + 1;
            mv.col = col;
            mv.next_dir = 0;
        } else {
            mv.row = row;
            mv.col = col + 1;
            mv.next_dir = 'R';
        }      // 否则
        break; // 跳出循环
    case 'R':  // case 'R':
        if (col + 1 < n && m[row][col + 1] == 0) {
            mv.row = row;
            mv.col = col + 1;
            mv.next_dir = 0;
        } else {
            mv.row = row - 1;
            mv.col = col;
            mv.next_dir = 'U';
        }      // 否则
        break; // 跳出循环
    case 'U':  // case 'U':
        if (row - 1 >= 0 && m[row - 1][col] == 0) {
            mv.row = row - 1;
            mv.col = col;
            mv.next_dir = 0;
        } else {
            mv.row = row;
            mv.col = col - 1;
            mv.next_dir = 'L';
        }      // 否则
        break; // 跳出循环
    default:   // default:
        if (col - 1 >= 0 && m[row][col - 1] == 0) {
            mv.row = row;
            mv.col = col - 1;
            mv.next_dir = 0;
        } else {
            mv.row = row + 1;
            mv.col = col;
            mv.next_dir = 'D';
        }      // 否则
        break; // 跳出循环
    }
    return mv; // 返回 mv
}

static void fill_spiral(int n, int m[][8]) { // 定义函数/方法 fill_spiral
    for (int i = 0; i < n; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (int j = 0; j < n; j++)
            m[i][j] = 0;   // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
    int row = 0, col = 0;  // 把 0, col 赋值为 0 存入 row
    char direction = 'D';  // 把 'D'; 写入 char direction
    int num = 1;           // 把 1 存入 num
    while (num <= n * n) { // 循环，直到不满足「num 不超过 元素个数 乘 元素个数」
        m[row][col] = num; // 把 num; 写入 m[row][col]
        num++;             // num 加一
        Move mv =
            place(row, col, direction, n, m); // 把 place(row, col, direction, 元素个数, 映射表); 写入 Move mv
        row = mv.row;                         // 把 mv.row; 写入 row
        col = mv.col;                         // 把 mv.col; 写入 col
        if (mv.next_dir)
            direction = mv.next_dir; // 若 mv.next_dir) direction 赋值为 mv.next_dir;
    }
}

int main(void) { // 程序入口：跑内嵌自测用例
    int m[8][8]; // int 映射表[8][8];
    int want3[3][3] = {
        {1, 8, 7}, {2, 9, 6}, {3, 4, 5}}; // 把 {{1, 8, 7}, {2, 9, 6}, {3, 4, 5}}; 写入 int want3[3][3]
    int want4[4][4] = {{1, 12, 11, 10}, {2, 13, 16, 9}, {3, 14, 15, 8}, {4, 5, 6, 7}};
    fill_spiral(3, m);              // fill_spiral(3, 映射表);
    for (int i = 0; i < 3; i++)     // 让 下标 i 从 0 开始计数，下标 i 小于 3 就继续
        for (int j = 0; j < 3; j++) // 让 下标 j 从 0 开始计数，下标 j 小于 3 就继续
            if (m[i][j] != want3[i][j]) {
                printf("spiral3 failed\n");
                return 1;
            }
    fill_spiral(4, m);              // fill_spiral(4, 映射表);
    for (int i = 0; i < 4; i++)     // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
        for (int j = 0; j < 4; j++) // 让 下标 j 从 0 开始计数，下标 j 小于 4 就继续
            if (m[i][j] != want4[i][j]) {
                printf("spiral4 failed\n");
                return 1;
            }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
