/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130506068 */
/* LeetCode 70. 爬楼梯 — C 版（方案3） */
#include <stdio.h> // 引入头文件
static int climb_stairs(int n) {
    if (n <= 2)
        return n;
    int a = 1, b = 2;
    for (int i = 3; i <= n; i++) {
        int t = a + b;
        a = b;
        b = t;
    }
    return b;
}
int main(void) {
    if (climb_stairs(2) != 2 || climb_stairs(3) != 3 || climb_stairs(10) != 89) {
        printf("FAIL\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS