/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133925028 */
/* LeetCode 122. 买卖股票的最佳时机II — C 版（方案3） */
#include <stdio.h>                                // 引入头文件
static int max_profit(const int *prices, int n) { // 定义函数/方法 max_profit
    int profit = 0;                               // 把 0 存入 profit
    for (int i = 1; i < n; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
        if (prices[i] > prices[i - 1])
            profit += prices[i] - prices[i - 1];
    }
    return profit; // 返回 profit
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (max_profit((int[]){7, 1, 5, 3, 6, 4}, 6) != 7) {
        printf("FAIL 1\n");
        return 1;
    }
    if (max_profit((int[]){1, 2, 3, 4, 5}, 5) != 4) {
        printf("FAIL 2\n");
        return 1;
    }
    if (max_profit((int[]){7, 6, 4, 3, 1}, 5) != 0) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
