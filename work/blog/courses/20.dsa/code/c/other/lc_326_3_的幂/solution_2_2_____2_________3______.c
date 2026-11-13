/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135359346 */
/* LeetCode 326. 3的幂 — C 版（方案2） */
#include <stdio.h>                     // 引入头文件
static int is_power_of_three(long n) { // 定义判定函数 is_power_of_three
    while (n != 0 && n % 3 == 0)
        n /= 3; // 循环，直到不满足「元素个数 不等于 0 且 元素个数 对…取模 3 等于 0) 元素个数 除以 3;」
    return n == 1; // 返回 元素个数 等于 1
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (!is_power_of_three(27)) {
        printf("FAIL 1\n");
        return 1;
    } // 若 取反 is_power_of_three(27)) { 输出「FAIL 1 」); return 1; }
    if (is_power_of_three(0)) {
        printf("FAIL 2\n");
        return 1;
    } // 若 is_power_of_three(0)) { 输出「FAIL 2 」); return 1; }
    if (!is_power_of_three(9)) {
        printf("FAIL 3\n");
        return 1;
    } // 若 取反 is_power_of_three(9)) { 输出「FAIL 3 」); return 1; }
    if (is_power_of_three(-1)) {
        printf("FAIL 4\n");
        return 1;
    } // 若 is_power_of_three( 减 1)) { 输出「FAIL 4 」); return 1; }
    if (!is_power_of_three(1)) {
        printf("FAIL 5\n");
        return 1;
    }                 // 若 取反 is_power_of_three(1)) { 输出「FAIL 5 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
