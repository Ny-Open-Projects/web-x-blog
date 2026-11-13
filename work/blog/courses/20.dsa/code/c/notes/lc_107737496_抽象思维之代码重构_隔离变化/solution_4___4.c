/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案4：螺旋矩阵方向模拟 placeFill）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

static void place_fill(int n, int m[][8]) { // 定义函数/方法 place_fill
    for (int i = 0; i < n; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (int j = 0; j < n; j++)
            m[i][j] = 0;        // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
    int row = 0, col = 0;       // 把 0, col 赋值为 0 存入 row
    char direction = 'D';       // 把 'D'; 写入 char direction
    int num = 1;                // 把 1 存入 num
    int total = n * n;          // 把 元素个数 乘 元素个数 存入 总和
    while (num <= total) {      // 循环，直到不满足「num 不超过 总和」
        m[row][col] = num;      // 把 num; 写入 m[row][col]
        num++;                  // num 加一
        if (direction == 'D') { // 若 direction 等于 'D'
            if (row + 1 < n && m[row + 1][col] == 0)
                row++; // 若 row 加 1 小于 元素个数 且 映射表[row 加 1][col] 等于 0) row 加一 ;
            else {
                direction = 'R';
                col++;
            }                          // 否则
        } else if (direction == 'R') { // 否则，若 direction 等于 'R'
            if (col + 1 < n && m[row][col + 1] == 0)
                col++; // 若 col 加 1 小于 元素个数 且 映射表[row][col 加 1] 等于 0) col 加一 ;
            else {
                direction = 'U';
                row--;
            }                          // 否则
        } else if (direction == 'U') { // 否则，若 direction 等于 'U'
            if (row - 1 >= 0 && m[row - 1][col] == 0)
                row--; // 若 row 减 1 不低于 0 且 映射表[row 减 1][col] 等于 0) row 减一 ;
            else {
                direction = 'L';
                col--;
            }    // 否则
        } else { // 否则
            if (col - 1 >= 0 && m[row][col - 1] == 0)
                col--; // 若 col 减 1 不低于 0 且 映射表[row][col 减 1] 等于 0) col 减一 ;
            else {
                direction = 'D';
                row++;
            } // 否则
        }
    }
}

static int eq_mat(const int a[][8], const int want[][8], int n) { // 定义函数/方法 eq_mat
    for (int i = 0; i < n; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (int j = 0; j < n; j++) // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
            if (a[i][j] != want[i][j])
                return 0; // 若 数组[下标 i][下标 j] 不等于 want[下标 i][下标 j]，直接返回 0
    return 1;             // 返回 1
}

int main(void) {   // 程序入口：跑内嵌自测用例
    int got[8][8]; // int got[8][8];
    int want3[3][8] = {
        {1, 8, 7}, {2, 9, 6}, {3, 4, 5}}; // 把 {{1, 8, 7}, {2, 9, 6}, {3, 4, 5}}; 写入 int want3[3][8]
    int want4[4][8] = {{1, 12, 11, 10}, {2, 13, 16, 9}, {3, 14, 15, 8}, {4, 5, 6, 7}};
    place_fill(3, got); // place_fill(3, got);
    if (!eq_mat(got, want3, 3)) {
        printf("place3 failed\n");
        return 1;
    }
    place_fill(4, got); // place_fill(4, got);
    if (!eq_mat(got, want4, 4)) {
        printf("place4 failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
