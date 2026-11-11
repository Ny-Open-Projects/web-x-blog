/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130644389 */
/* LeetCode 198. 打家劫舍 — C 版（方案10） */
#include <stdio.h> // 引入头文件
static int rob(const int *n, int len) {
    int a = 0, b = 0;
    for (int i = 0; i < len; i++) {
        int t = b > a + n[i] ? b : a + n[i];
        a = b;
        b = t;
    }
    return b;
}
int main(void) {
    if (rob((int[]){1, 2, 3, 1}, 4) != 4) {
        printf("FAIL 1\n");
        return 1;
    }
    if (rob((int[]){2, 7, 9, 3, 1}, 5) != 12) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS