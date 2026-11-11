/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133968437 */
/* LeetCode 268. 丢失的数字 — C 版（方案1） */
#include <stdio.h>                                 // 引入头文件
static int missing_number(const int *n, int len) { // 定义函数/方法 missing_number
    long sum = 0;                                  // 把 0; 写入 long sum
    for (int i = 0; i < len; i++)
        sum += n[i];                     // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
    long m = len;                        // 把 长度; 写入 long m
    return (int)(m * (m + 1) / 2 - sum); // 返回 (int)(映射表 乘 (映射表 加 1) 除以 2 减 累计和)
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (missing_number((int[]){3, 0, 1}, 3) != 2) {
        printf("FAIL 1\n");
        return 1;
    }
    if (missing_number((int[]){0, 1}, 2) != 2) {
        printf("FAIL 2\n");
        return 1;
    }
    if (missing_number((int[]){9, 6, 4, 2, 3, 5, 7, 0, 1}, 9) != 8) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS