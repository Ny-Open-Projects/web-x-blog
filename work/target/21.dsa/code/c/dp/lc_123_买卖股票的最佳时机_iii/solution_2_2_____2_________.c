/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130588647 */
/* LeetCode 123. 买卖股票的最佳时机III — C 版（方案2） */
#include <stdio.h>                               // 引入头文件
static int max_profit_iii(const int *p, int n) { // 定义函数/方法 max_profit_iii
    int buy1 = -1000000000, sell1 = 0, buy2 = -1000000000, sell2 = 0;
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        if (-p[i] > buy1)
            buy1 = -p[i]; // 若 减 节点[下标 i] 超过 buy1) buy1 赋值为 减 节点[下标 i];
        if (buy1 + p[i] > sell1)
            sell1 = buy1 + p[i]; // 若 buy1 加 节点[下标 i] 超过 sell1) sell1 赋值为 buy1 加 节点[下标 i];
        if (sell1 - p[i] > buy2)
            buy2 = sell1 - p[i]; // 若 sell1 减 节点[下标 i] 超过 buy2) buy2 赋值为 sell1 减 节点[下标 i];
        if (buy2 + p[i] > sell2)
            sell2 = buy2 + p[i]; // 若 buy2 加 节点[下标 i] 超过 sell2) sell2 赋值为 buy2 加 节点[下标 i];
    }
    return sell2; // 返回 sell2
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (max_profit_iii((int[]){1, 2, 3}, 3) != 2) {
        printf("FAIL 1\n");
        return 1;
    }
    if (max_profit_iii((int[]){1, 2, 3, 4, 5}, 5) != 4) {
        printf("FAIL 2\n");
        return 1;
    }
    if (max_profit_iii((int[]){7, 6, 4, 3, 1}, 5) != 0) {
        printf("FAIL 3\n");
        return 1;
    }
    if (max_profit_iii((int[]){3, 3, 5, 0, 0, 3, 1, 4}, 8) != 6) {
        printf("FAIL 4\n");
        return 1;
    }
    if (max_profit_iii((int[]){1}, 1) != 0) {
        printf("FAIL 5\n");
        return 1;
    }
    if (max_profit_iii((int[]){1, 2}, 2) != 1) {
        printf("FAIL 6\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS