/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134424807 */
/* LeetCode 485. 最大连续1的个数 — C 版（方案1） */
#include <stdio.h>                                            // 引入头文件
static int find_max_consecutive_ones(const int *n, int len) { // 定义函数/方法 find_max_consecutive_ones
    int best = 0, cur = 0;          // 把 0, 当前值 赋值为 0 存入 当前最优
    for (int i = 0; i < len; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
        if (n[i] == 1) {
            cur++;
            if (cur > best)
                best = cur;
        } else
            cur = 0; // 否则
    }
    return best; // 返回 当前最优
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (find_max_consecutive_ones((int[]){1, 1, 0, 1, 1, 1}, 6) != 3) {
        printf("FAIL 1\n");
        return 1;
    }
    if (find_max_consecutive_ones((int[]){1, 0, 1, 1, 0, 1}, 6) != 2) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS