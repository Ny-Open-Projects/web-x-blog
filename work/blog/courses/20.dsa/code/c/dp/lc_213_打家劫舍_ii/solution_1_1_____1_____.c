/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130716392 */
/* LeetCode 213. 打家劫舍II — C 版（方案1） */
#include <stdio.h> // 引入头文件
static int rob_line(const int *n, int len) {
    int a = 0, b = 0;
    for (int i = 0; i < len; i++) {
        int t = b > a + n[i] ? b : a + n[i];
        a = b;
        b = t;
    }
    return b;
}
static int rob_ii(const int *n, int len) { // 定义函数/方法 rob_ii
    if (len == 1)
        return n[0];                   // 若 长度 等于 1，直接返回 元素个数[0]
    int r1 = rob_line(n + 1, len - 1); // 把 rob_line(元素个数 加 1, 长度 减 1) 存入 r1
    int r2 = rob_line(n, len - 1);     // 把 rob_line(元素个数, 长度 减 1) 存入 r2
    return r1 > r2 ? r1 : r2;          // 返回 r1 超过 r2 ? r1 : r2
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (rob_ii((int[]){2, 3, 2}, 3) != 3) {
        printf("FAIL 1\n");
        return 1;
    }
    if (rob_ii((int[]){1, 2, 3, 1}, 4) != 4) {
        printf("FAIL 2\n");
        return 1;
    }
    if (rob_ii((int[]){1}, 1) != 1) {
        printf("FAIL 3\n");
        return 1;
    } // 若 rob_ii((int[]){1}, 1) 不等于 1) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS