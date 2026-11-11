/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136236962 */
/* LeetCode 1685. 有序数组中差绝对值之和 — C 版（方案3） */
#include <stdio.h> // 引入头文件
static void get_sum_absolute_differences(const int *nums, int n,
                                         int out[]) { // 定义函数/方法 get_sum_absolute_differences
    long total = 0;                                   // 把 0; 写入 long total
    for (int i = 0; i < n; i++)
        total += nums[i];         // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    long prefix = 0;              // 把 0; 写入 long prefix
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        long v = nums[i];         // 把 数组[下标 i]; 写入 long v
        long left = v * i - prefix; // 把 值 乘 下标 i 减 prefix; 写入 long left
        long right =
            (total - prefix - v) -
            v * (n - 1 - i); // 把 (总和 减 prefix 减 值) 减 值 乘 (元素个数 减 1 减 下标 i); 写入 long right
        out[i] = (int)(left + right); // 把 (int)(左边界 加 右边界); 写入 out[i]
        prefix += v;                  // prefix累加 值
    }
}
int main(void) {   // 程序入口：跑内嵌自测用例
    int out[4096]; // int out[4096];
    get_sum_absolute_differences((int[]){2, 3, 5}, 3,
                                 out); // get_sum_absolute_differences((int[]){2,3,5}, 3, out);
    if (!(out[0] == 4 && out[1] == 3 && out[2] == 5)) {
        printf("FAIL 1\n");
        return 1;
    }
    get_sum_absolute_differences((int[]){1, 4, 6, 8, 10}, 5,
                                 out); // get_sum_absolute_differences((int[]){1,4,6,8,10}, 5, out);
    if (!(out[0] == 24 && out[2] == 13 && out[4] == 21)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS