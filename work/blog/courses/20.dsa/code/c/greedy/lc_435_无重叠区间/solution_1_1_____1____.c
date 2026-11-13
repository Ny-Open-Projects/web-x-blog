/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135941089 */
/* LeetCode 435. 无重叠区间 — C 版（方案1） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
static int cmp_iv(const void *a, const void *b) { return ((const int *)a)[1] - ((const int *)b)[1]; }
static int erase_overlap_intervals(int intervals[][2], int n) { // 定义函数/方法 erase_overlap_intervals
    if (n == 0)
        return 0;    // 若 元素个数 等于 0，直接返回 0
    int arr[256][2]; // int 数组[256][2];
    for (int i = 0; i < n; i++) {
        arr[i][0] = intervals[i][0];
        arr[i][1] = intervals[i][1];
    } // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    qsort(arr, n, sizeof(int) * 2, cmp_iv); // qsort(数组, 元素个数, sizeof(int) 乘 2, cmp_iv);
    int count = 1, end = arr[0][1];         // 把 1, 终点 赋值为 数组[0][1] 存入 计数
    for (int i = 1; i < n; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
        if (arr[i][0] >= end) {
            count++;
            end = arr[i][1];
        } // 若 数组[下标 i][0] 不低于 终点) { 计数 加一 ; 终点 赋值为 数组[下标 i][1]; }
    }
    return n - count; // 返回 元素个数 减 计数
}
int main(void) {                                    // 程序入口：跑内嵌自测用例
    int v1[][2] = {{1, 2}, {2, 3}, {3, 4}, {1, 3}}; // 把 {{1,2},{2,3},{3,4},{1,3}}; 写入 int v1[][2]
    int v3[][2] = {{1, 2}, {1, 2}, {1, 2}};         // 把 {{1,2},{1,2},{1,2}}; 写入 int v3[][2]
    if (erase_overlap_intervals(v1, 4) != 1) {
        printf("FAIL 1\n");
        return 1;
    }
    if (erase_overlap_intervals(NULL, 0) != 0) {
        printf("FAIL 2\n");
        return 1;
    }
    if (erase_overlap_intervals(v3, 3) != 2) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
