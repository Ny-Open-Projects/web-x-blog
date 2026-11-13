/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133845474 */
/* LeetCode 15. 三数之和 — C 版（方案2） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static int three_sum(const int *nums, int n, int out[][3]) { // 定义函数/方法 three_sum
    int arr[4096];                                           // int 数组[4096];
    for (int i = 0; i < n; i++)
        arr[i] = nums[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    qsort(arr, n, sizeof(int), cmp_int);      // qsort(数组, 元素个数, sizeof(int), cmp_int);
    int cnt = 0;                              // 把 0 存入 计数
    for (int first = 0; first < n; first++) { // 让 first 从 0 开始计数，first 小于 元素个数 就继续
        if (first > 0 && arr[first] == arr[first - 1])
            continue;      // 若 first 超过 0 且 数组[first] 等于 数组[first 减 1]) continue;
        int third = n - 1; // 把 元素个数 减 1 存入 third
        int target = -arr[first]; // 把 减 数组[first] 存入 目标值
        for (int second = first + 1; second < n;
             second++) { // 让 second 从 first 加 1 开始计数，second 小于 元素个数 就继续
            if (second > first + 1 && arr[second] == arr[second - 1])
                continue;
            while (second < third && arr[second] + arr[third] > target)
                third--;
            if (second == third)
                break;                                // 若 second 等于 third) break;
            if (arr[second] + arr[third] == target) { // 若 数组[second] 加 数组[third] 等于 目标值
                out[cnt][0] = arr[first];
                out[cnt][1] = arr[second];
                out[cnt][2] = arr[third];
                cnt++; // 计数 加一
            }
        }
    }
    return cnt; // 返回 计数
}
int main(void) {    // 程序入口：跑内嵌自测用例
    int out[64][3]; // int out[64][3];
    int n = three_sum((int[]){-1, 0, 1, 2, -1, -4}, 6,
                      out); // 把 three_sum((int[]){ 减 1,0,1,2, 减 1, 减 4}, 6, out) 存入 元素个数
    /* 期望两组：[-1,-1,2] 与 [-1,0,1]（已按序生成） */
    if (n != 2) {
        printf("FAIL cnt=%d\n", n);
        return 1;
    } // 若 元素个数 不等于 2) { 输出「FAIL 计数 赋值为 对…取模 d 」, 元素个数); return 1; }
    if (out[0][0] != -1 || out[0][1] != -1 || out[0][2] != 2) {
        printf("FAIL t1\n");
        return 1;
    }
    if (out[1][0] != -1 || out[1][1] != 0 || out[1][2] != 1) {
        printf("FAIL t2\n");
        return 1;
    }
    n = three_sum((int[]){0, 0, 0}, 3, out); // 把 three_sum((int[]){0,0,0}, 3, out); 写入 元素个数
    if (n != 1 || out[0][0] != 0) {
        printf("FAIL z\n");
        return 1;
    } // 若 元素个数 不等于 1 或 out[0][0] 不等于 0) { 输出「FAIL z 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
