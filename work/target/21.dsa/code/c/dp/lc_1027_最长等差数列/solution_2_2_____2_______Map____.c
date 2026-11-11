/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130687299 */
/* LeetCode 1027. 最长等差数列 — C 版（方案2） */
#include <stdio.h>                                            // 引入头文件
static int longest_arith_seq_length(const int *nums, int n) { // 定义函数/方法 longest_arith_seq_length
    /* n 小，用 O(n^2 * d) 简化：dp[i][d] 用哈希替代 —— 简化为暴力双循环+线性回溯 */
    if (n <= 2)
        return n;                 // 若 元素个数 不超过 2，直接返回 元素个数
    int best = 2;                 // 把 2 存入 当前最优
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (int j = i + 1; j < n; j++) { // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 元素个数 就继续
            int d = nums[j] - nums[i]; // 把 数组[下标 j] 减 数组[下标 i] 存入 d
            int cur = 2;               // 把 2 存入 当前值
            int last = nums[j];        // 把 数组[下标 j] 存入 last
            for (int k = j + 1; k < n;
                 k++) { // 让 下标 k 从 下标 j 加 1 开始计数，下标 k 小于 元素个数 就继续
                if (nums[k] - last == d) {
                    cur++;
                    last = nums[k];
                } // 若 数组[下标 k] 减 last 等于 d) { 当前值 加一 ; last 赋值为 数组[下标 k]; }
            }
            if (cur > best)
                best = cur; // 若 当前值 超过 当前最优) 当前最优 赋值为 当前值;
        }
    }
    return best; // 返回 当前最优
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (longest_arith_seq_length((int[]){9, 4, 7, 2, 10}, 5) != 3) {
        printf("FAIL 1\n");
        return 1;
    }
    if (longest_arith_seq_length((int[]){3, 6, 9, 12}, 4) != 4) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS