/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145582435 */
/* LeetCode 3105. 最长的严格递增或递减子数组 — C 版（方案1） */
#include <stdio.h>                                             // 引入头文件
static int longest_monotonic_subarray(const int *n, int len) { // 定义函数/方法 longest_monotonic_subarray
    if (len == 0)
        return 0;                   // 若 长度 等于 0，直接返回 0
    int inc = 1, dec = 1, best = 1; // 把 1, dec 赋值为 1, 当前最优 赋值为 1 存入 inc
    for (int i = 1; i < len; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 长度 就继续
        if (n[i] > n[i - 1]) {
            inc++;
            dec = 1;
        } // 若 元素个数[下标 i] 超过 元素个数[下标 i 减 1]) { inc 加一 ; dec 赋值为 1; }
        else if (n[i] < n[i - 1]) {
            dec++;
            inc = 1;
        } // 否则，若 元素个数[下标 i] 小于 元素个数[下标 i 减 1]) { dec 加一 ; inc 赋值为 1; }
        else {
            inc = 1;
            dec = 1;
        } // 否则
        if (inc > best)
            best = inc; // 若 inc 超过 当前最优) 当前最优 赋值为 inc;
        if (dec > best)
            best = dec; // 若 dec 超过 当前最优) 当前最优 赋值为 dec;
    }
    return best; // 返回 当前最优
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (longest_monotonic_subarray((int[]){1, 2, 3, 4, 5}, 5) != 5) {
        printf("FAIL 1\n");
        return 1;
    }
    if (longest_monotonic_subarray((int[]){5, 4, 3, 2, 1}, 5) != 5) {
        printf("FAIL 2\n");
        return 1;
    }
    if (longest_monotonic_subarray((int[]){1, 4, 3, 2, 5}, 5) != 3) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS