/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
 * LeetCode 104107934. 滑动验证码识别 — C 版（方案4：SAD 绝对差和最佳窗口）
 */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件

static void best_match_window(const int *bg, int bn, const int *puzzle, int pn, int *out_x,
                              long *out_score) { // 定义函数/方法 best_match_window
    int best_x = 0;                              // 把 0 存入 best_x
    long best_score = 1L << 60;                  // 把 1L 小于 小于 60; 写入 long best_score
    for (int x = 0; x <= bn - pn; x++) {         // 让 x 从 0 开始计数，x 不超过 bn 减 pn 就继续
        long score = 0;                          // 把 0; 写入 long score
        for (int y = 0; y < pn; y++)
            score += labs(bg[x + y] - puzzle[y]); // 让 y 从 0 开始计数，y 小于 pn 就继续
        if (score < best_score) {
            best_score = score;
            best_x = x;
        }
    }
    *out_x = best_x;
    *out_score = best_score;
}

int main(void) { // 程序入口：跑内嵌自测用例
    int bg[8] = {10,  10,  10,  10,
                 200, 200, 200, 200};    // 把 {10, 10, 10, 10, 200, 200, 200, 200}; 写入 int bg[8]
    int puzzle[4] = {10, 200, 200, 200}; // 把 {10, 200, 200, 200}; 写入 int puzzle[4]
    int bx;                              // int bx;
    long bs;                             // long bs;
    best_match_window(bg, 8, puzzle, 4, &bx,
                      &bs); // best_match_window(bg, 8, puzzle, 4, 按位与 bx, 按位与 bs);
    if (bx != 3 || bs != 0) {
        printf("gap failed\n");
        return 1;
    }                 // 若 bx 不等于 3 或 bs 不等于 0) { 输出「gap failed 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
