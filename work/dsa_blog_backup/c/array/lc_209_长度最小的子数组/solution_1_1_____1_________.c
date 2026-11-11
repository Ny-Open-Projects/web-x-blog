/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133807379 */
/* LeetCode 209. 长度最小的子数组 — C 版（方案1） */
#include <stdio.h>                                                // 引入头文件
static int min_sub_array_len(int target, const int *n, int len) { // 定义函数/方法 min_sub_array_len
    int l = 0, best = 1 << 30;      // 把 0, 当前最优 赋值为 1 小于 小于 30 存入 左指针
    long sum = 0;                   // 把 0; 写入 long sum
    for (int r = 0; r < len; r++) { // 让 右指针 从 0 开始计数，右指针 小于 长度 就继续
        sum += n[r];                // 累计和累加 元素个数[右指针]
        while (sum >= target) {     // 循环，直到不满足「累计和 不低于 目标值」
            if (r - l + 1 < best)
                best = r - l +
                       1; // 若 右指针 减 左指针 加 1 小于 当前最优) 当前最优 赋值为 右指针 减 左指针 加 1;
            sum -= n[l++]; // 累计和累减 元素个数[左指针 加一 ]
        }
    }
    return best == (1 << 30) ? 0 : best; // 返回 当前最优 等于 (1 小于 小于 30) ? 0 : 当前最优
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (min_sub_array_len(7, (int[]){2, 3, 1, 2, 4, 3}, 6) != 2) {
        printf("FAIL 1\n");
        return 1;
    }
    if (min_sub_array_len(4, (int[]){1, 4, 4}, 3) != 1) {
        printf("FAIL 2\n");
        return 1;
    }
    if (min_sub_array_len(11, (int[]){1, 1, 1, 1, 1, 1, 1, 1}, 8) != 0) {
        printf("FAIL 3\n");
        return 1;
    }
    if (min_sub_array_len(1, (int[]){1, 2, 3}, 3) != 1) {
        printf("FAIL 4\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS