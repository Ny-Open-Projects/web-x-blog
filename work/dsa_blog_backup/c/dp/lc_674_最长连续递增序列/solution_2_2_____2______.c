/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130771608 */
/* LeetCode 674. 最长连续递增序列 — C 版（方案2） */
#include <stdio.h>                                      // 引入头文件
static int find_length_of_lcis(const int *n, int len) { // 定义函数/方法 find_length_of_lcis
    if (len == 0)
        return 0;                   // 若 长度 等于 0，直接返回 0
    int best = 1, cur = 1;          // 把 1, 当前值 赋值为 1 存入 当前最优
    for (int i = 1; i < len; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 长度 就继续
        if (n[i] > n[i - 1]) {
            cur++;
            if (cur > best)
                best = cur;
        } else
            cur = 1; // 否则
    }
    return best; // 返回 当前最优
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (find_length_of_lcis((int[]){1, 3, 5, 4, 7}, 5) != 3) {
        printf("FAIL 1\n");
        return 1;
    }
    if (find_length_of_lcis((int[]){2, 2, 2, 2, 2}, 5) != 1) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS