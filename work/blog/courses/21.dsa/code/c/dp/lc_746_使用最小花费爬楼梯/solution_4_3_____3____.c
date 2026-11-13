/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130521152 */
/* LeetCode 746. 使用最小花费爬楼梯 — C 版（方案4） */
#include <stdio.h>                                            // 引入头文件
static int min_cost_climbing_stairs(const int *cost, int n) { // 定义函数/方法 min_cost_climbing_stairs
    int a = 0, b = 0;                                         // 把 0, b 赋值为 0 存入 数组
    for (int i = 2; i <= n; i++) { // 让 下标 i 从 2 开始计数，下标 i 不超过 元素个数 就继续
        int x = a + cost[i - 2],
            y = b + cost[i - 1]; // 把 数组 加 cost[下标 i 减 2], y 赋值为 b 加 cost[下标 i 减 1] 存入 x
        int t = x < y ? x : y; // 把 x 小于 y ? x : y 存入 另一字符串
        a = b;
        b = t; // 把 b; b 赋值为 另一字符串; 写入 数组
    }
    return b; // 返回 b
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (min_cost_climbing_stairs((int[]){10, 15, 20}, 3) != 15) {
        printf("FAIL 1\n");
        return 1;
    }
    if (min_cost_climbing_stairs((int[]){1, 100, 1, 1, 1, 100, 1, 1, 100, 1}, 10) != 6) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS