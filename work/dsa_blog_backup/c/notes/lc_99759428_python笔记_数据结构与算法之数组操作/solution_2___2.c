/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/99759428 */
/* 数据结构与算法之数组操作 — C 版（方案2） */
#include <stdio.h>                                                  // 引入头文件
static int two_sum(const int *n, int len, int target, int out[2]) { // 定义函数/方法 two_sum
    for (int i = 0; i < len; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
        for (int j = i + 1; j < len; j++) // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 长度 就继续
            if (n[i] + n[j] == target) {
                out[0] = i;
                out[1] = j;
                return 1;
            }
    return 0; // 返回 0
}
static int max_sub_array(const int *n, int len) { // 定义函数/方法 max_sub_array
    int best = n[0], cur = n[0]; // 把 元素个数[0], 当前值 赋值为 元素个数[0] 存入 当前最优
    for (int i = 1; i < len; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 长度 就继续
        cur = cur > 0 ? cur + n[i]
                      : n[i]; // 把 当前值 超过 0 ? 当前值 加 元素个数[下标 i] : 元素个数[下标 i]; 写入 当前值
        if (cur > best)
            best = cur; // 若 当前值 超过 当前最优) 当前最优 赋值为 当前值;
    }
    return best; // 返回 当前最优
}
int main(void) { // 程序入口：跑内嵌自测用例
    int out[2];  // int out[2];
    if (two_sum((int[]){2, 7, 11, 15}, 4, 9, out) != 1 || out[0] != 0 || out[1] != 1) {
        printf("FAIL 1\n");
        return 1;
    }
    if (max_sub_array((int[]){-2, 1, -3, 4, -1, 2, 1, -5, 4}, 9) != 6) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS