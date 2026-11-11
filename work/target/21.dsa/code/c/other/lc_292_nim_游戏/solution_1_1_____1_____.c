/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135424151 */
/* LeetCode 292. Nim游戏 — C 版（方案1） */
#include <stdio.h> // 引入头文件
static int can_win_nim(long n) {
    return n % 4 != 0;
} // 把 0; } 写入 static int can_win_nim(long n) { return n % 4 !
int main(void) { // 程序入口：跑内嵌自测用例
    if (can_win_nim(4)) {
        printf("FAIL 1\n");
        return 1;
    } // 若 can_win_nim(4)) { 输出「FAIL 1 」); return 1; }
    if (!can_win_nim(1) || !can_win_nim(2)) {
        printf("FAIL 2\n");
        return 1;
    }
    if (can_win_nim(8)) {
        printf("FAIL 3\n");
        return 1;
    }                 // 若 can_win_nim(8)) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
