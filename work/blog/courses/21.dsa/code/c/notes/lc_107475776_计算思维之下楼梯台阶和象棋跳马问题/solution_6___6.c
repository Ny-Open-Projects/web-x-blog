/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776 */
/* 计算思维之下楼梯台阶和象棋跳马问题 — C 版（方案6） */
#include <stdio.h>                         // 引入头文件
static long climb_stairs_variants(int n) { // 定义函数/方法 climb_stairs_variants
    if (n <= 1)
        return 1;      // 若 元素个数 不超过 1，直接返回 1
    long a = 1, b = 1; // 把 1, b 赋值为 1; 写入 long a
    for (int i = 2; i <= n; i++) {
        long t = a + b;
        a = b;
        b = t;
    }         // 让 下标 i 从 2 开始计数，下标 i 不超过 元素个数 就继续
    return b; // 返回 b
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (climb_stairs_variants(10) != 89 || climb_stairs_variants(1) != 1 || climb_stairs_variants(2) != 2) {
        printf("FAIL\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS