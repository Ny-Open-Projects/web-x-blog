/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130741193 */
/* LeetCode 714. 买卖股票的最佳时机含手续费 — C 版（方案2） */
#include <stdio.h>                                        // 引入头文件
static int max_profit_fee(const int *p, int n, int fee) { // 定义函数/方法 max_profit_fee
    int hold = -p[0], sold = 0;                           // 把 减 节点[0], sold 赋值为 0 存入 hold
    for (int i = 1; i < n; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
        int nh = hold > sold - p[i]
                     ? hold
                     : sold - p[i]; // 把 hold 超过 sold 减 节点[下标 i] ? hold : sold 减 节点[下标 i] 存入 nh
        int ns = sold > hold + p[i] - fee ? sold : hold + p[i] - fee;
        hold = nh;
        sold = ns; // 把 nh; sold 赋值为 ns; 写入 hold
    }
    return sold; // 返回 sold
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (max_profit_fee((int[]){1, 3, 2, 8, 4, 9}, 6, 2) != 8) {
        printf("FAIL 1\n");
        return 1;
    }
    if (max_profit_fee((int[]){1}, 1, 1) != 0) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS