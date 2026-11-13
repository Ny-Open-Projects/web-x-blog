/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135949307 */
/* LeetCode 452. 用最少数量的箭引爆气球 — C 版（方案2） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
static int cmp_iv(const void *a, const void *b) { return ((const int *)a)[1] - ((const int *)b)[1]; }
static int find_min_arrow_shots(int points[][2], int n) { // 定义函数/方法 find_min_arrow_shots
    if (n == 0)
        return 0;    // 若 元素个数 等于 0，直接返回 0
    int arr[256][2]; // int 数组[256][2];
    for (int i = 0; i < n; i++) {
        arr[i][0] = points[i][0];
        arr[i][1] = points[i][1];
    } // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    qsort(arr, n, sizeof(int) * 2, cmp_iv); // qsort(数组, 元素个数, sizeof(int) 乘 2, cmp_iv);
    int arrows = 1, end = arr[0][1];        // 把 1, 终点 赋值为 数组[0][1] 存入 arrows
    for (int k = 1; k < n; k++) { // 让 下标 k 从 1 开始计数，下标 k 小于 元素个数 就继续
        if (arr[k][0] > end) {
            arrows++;
            end = arr[k][1];
        } // 若 数组[下标 k][0] 超过 终点) { arrows 加一 ; 终点 赋值为 数组[下标 k][1]; }
    }
    return arrows; // 返回 arrows
}
int main(void) {                                       // 程序入口：跑内嵌自测用例
    int v1[][2] = {{10, 16}, {2, 8}, {1, 6}, {7, 12}}; // 把 {{10,16},{2,8},{1,6},{7,12}}; 写入 int v1[][2]
    int v3[][2] = {{1, 2}, {3, 4}, {5, 6}, {7, 8}};    // 把 {{1,2},{3,4},{5,6},{7,8}}; 写入 int v3[][2]
    if (find_min_arrow_shots(v1, 4) != 2) {
        printf("FAIL 1\n");
        return 1;
    }
    if (find_min_arrow_shots(NULL, 0) != 0) {
        printf("FAIL 2\n");
        return 1;
    }
    if (find_min_arrow_shots(v3, 4) != 4) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
