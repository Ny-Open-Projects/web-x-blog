/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133468105 */
/* LeetCode 136. 只出现一次的数字 — C 版（方案1） */
#include <stdio.h> // 引入头文件
static int single_number(const int *n, int len) {
    int x = 0;
    for (int i = 0; i < len; i++)
        x ^= n[i];
    return x;
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (single_number((int[]){2, 2, 1}, 3) != 1) {
        printf("FAIL 1\n");
        return 1;
    }
    if (single_number((int[]){4, 1, 2, 1, 2}, 5) != 4) {
        printf("FAIL 2\n");
        return 1;
    }
    if (single_number((int[]){1}, 1) != 1) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS