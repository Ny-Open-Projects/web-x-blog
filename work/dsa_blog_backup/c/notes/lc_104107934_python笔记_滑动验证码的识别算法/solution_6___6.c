/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
 * LeetCode 104107934. 滑动验证码识别 — C 版（方案6：合成滑块数据 buildSynthetic）
 */
#include <stdio.h> // 引入头文件

static void build_synthetic(int bg_len, int gap_start, int puzzle_len, int *bg,
                            int *puzzle) { // 定义函数/方法 build_synthetic
    for (int i = 0; i < bg_len; i++)
        bg[i] = 10; // 让 下标 i 从 0 开始计数，下标 i 小于 bg_len 就继续
    for (int i = gap_start; i < gap_start + puzzle_len && i < bg_len; i++)
        bg[i] = 200;
    for (int i = 0; i < puzzle_len; i++)
        puzzle[i] = bg[gap_start + i]; // 让 下标 i 从 0 开始计数，下标 i 小于 puzzle_len 就继续
}

int main(void) {                          // 程序入口：跑内嵌自测用例
    int bg[8], puzzle[4];                 // int bg[8], puzzle[4];
    build_synthetic(8, 3, 4, bg, puzzle); // build_synthetic(8, 3, 4, bg, puzzle);
    int want_bg[8] = {10,  10,  10,  200,
                      200, 200, 200, 10};  // 把 {10, 10, 10, 200, 200, 200, 200, 10}; 写入 int want_bg[8]
    int want_pz[4] = {200, 200, 200, 200}; // 把 {200, 200, 200, 200}; 写入 int want_pz[4]
    for (int i = 0; i < 8; i++)            // 让 下标 i 从 0 开始计数，下标 i 小于 8 就继续
        if (bg[i] != want_bg[i]) {
            printf("bg failed\n");
            return 1;
        } // 若 bg[下标 i] 不等于 want_bg[下标 i]) { 输出「bg failed 」); return 1; }
    for (int i = 0; i < 4; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
        if (puzzle[i] != want_pz[i]) {
            printf("puzzle failed\n");
            return 1;
        }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
