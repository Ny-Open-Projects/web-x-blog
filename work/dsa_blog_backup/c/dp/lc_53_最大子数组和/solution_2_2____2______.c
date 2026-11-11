/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130497821 */
/* LeetCode 53. 最大子数组和 — C 版（方案2） */
#include <stdio.h>                                // 引入头文件
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
    if (max_sub_array((int[]){-2, 1, -3, 4, -1, 2, 1, -5, 4}, 9) != 6) {
        printf("FAIL 1\n");
        return 1;
    }
    if (max_sub_array((int[]){1}, 1) != 1) {
        printf("FAIL 2\n");
        return 1;
    }
    if (max_sub_array((int[]){5, 4, -1, 7, 8}, 5) != 23) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS