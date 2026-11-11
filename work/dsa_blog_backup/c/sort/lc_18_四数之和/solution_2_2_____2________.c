/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133894317 */
/* LeetCode 18. 四数之和 — C 版（方案2） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static int four_sum(const int *nums, int n, int target, int out[][4]) { // 定义函数/方法 four_sum
    int arr[4096];                                                      // int 数组[4096];
    for (int i = 0; i < n; i++)
        arr[i] = nums[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    qsort(arr, n, sizeof(int), cmp_int); // qsort(数组, 元素个数, sizeof(int), cmp_int);
    int cnt = 0;                         // 把 0 存入 计数
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        if (i > 0 && arr[i] == arr[i - 1])
            continue; // 若 下标 i 超过 0 且 数组[下标 i] 等于 数组[下标 i 减 1]) continue;
        for (int j = i + 1; j < n; j++) { // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 元素个数 就继续
            if (j > i + 1 && arr[j] == arr[j - 1])
                continue; // 若 下标 j 超过 下标 i 加 1 且 数组[下标 j] 等于 数组[下标 j 减 1]) continue;
            int left = j + 1, right = n - 1; // 把 下标 j 加 1, 右边界 赋值为 元素个数 减 1 存入 左边界
            while (left < right) { // 循环，直到不满足「左边界 小于 右边界」
                long s = (long)arr[i] + arr[j] + arr[left] +
                         arr[right]; // 把 (long)数组[下标 i] 加 数组[下标 j] 加 数组[左边界] 加 数组[右边界];
                                     // 写入 long s
                if (s == target) { // 若 字符串 等于 目标值
                    out[cnt][0] = arr[i];
                    out[cnt][1] = arr[j];
                    out[cnt][2] = arr[left];
                    out[cnt][3] = arr[right];
                    cnt++; // 计数 加一
                    left++;
                    right--; // 左边界 加一 ; 右边界 减一 ;
                    while (left < right && arr[left] == arr[left - 1])
                        left++; // 循环，直到不满足「左边界 小于 右边界 且 数组[左边界] 等于 数组[左边界 减
                                // 1]) 左边界 加一 ;」
                    while (left < right && arr[right] == arr[right + 1])
                        right--; // 循环，直到不满足「左边界 小于 右边界 且 数组[右边界] 等于 数组[右边界 加
                                 // 1]) 右边界 减一 ;」
                } else if (s < target)
                    left++; // 否则，若 字符串 小于 目标值) 左边界 加一 ;
                else
                    right--; // 否则
            }
        }
    }
    return cnt; // 返回 计数
}
int main(void) {    // 程序入口：跑内嵌自测用例
    int out[64][4]; // int out[64][4];
    int n = four_sum((int[]){1, 0, -1, 0, -2, 2}, 6, 0,
                     out); // 把 four_sum((int[]){1,0, 减 1,0, 减 2,2}, 6, 0, out) 存入 元素个数
    if (n != 3) {
        printf("FAIL cnt=%d\n", n);
        return 1;
    } // 若 元素个数 不等于 3) { 输出「FAIL 计数 赋值为 对…取模 d 」, 元素个数); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
