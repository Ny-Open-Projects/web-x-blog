/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130515763 */
/* LeetCode 121. 买卖股票的最佳时机 — C 版（方案3） */
#include <stdio.h>                           // 引入头文件
static int max_profit(const int *p, int n) { // 定义函数/方法 max_profit
    int min_p = 1 << 30, best = 0;           // 把 1 小于 小于 30, 当前最优 赋值为 0 存入 min_p
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        if (p[i] < min_p)
            min_p = p[i]; // 若 节点[下标 i] 小于 min_p) min_p 赋值为 节点[下标 i];
        if (p[i] - min_p > best)
            best = p[i] -
                   min_p; // 若 节点[下标 i] 减 min_p 超过 当前最优) 当前最优 赋值为 节点[下标 i] 减 min_p;
    }
    return best; // 返回 当前最优
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (max_profit((int[]){7, 1, 5, 3, 6, 4}, 6) != 5) {
        printf("FAIL 1\n");
        return 1;
    }
    if (max_profit((int[]){7, 6, 4, 3, 1}, 5) != 0) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS