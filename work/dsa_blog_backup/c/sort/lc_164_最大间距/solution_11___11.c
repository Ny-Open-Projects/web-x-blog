/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135003383 */
/* LeetCode 164. 最大间距 — C 版（方案11） */
#include <stdio.h>                               // 引入头文件
#include <stdlib.h>                              // 引入头文件
static int maximum_gap(const int *nums, int n) { // 定义函数/方法 maximum_gap
    if (n < 2)
        return 0;                             // 若 元素个数 小于 2，直接返回 0
    int min_val = nums[0], max_val = nums[0]; // 把 数组[0], max_val 赋值为 数组[0] 存入 min_val
    for (int i = 1; i < n; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
        if (nums[i] < min_val)
            min_val = nums[i]; // 若 数组[下标 i] 小于 min_val) min_val 赋值为 数组[下标 i];
        if (nums[i] > max_val)
            max_val = nums[i]; // 若 数组[下标 i] 超过 max_val) max_val 赋值为 数组[下标 i];
    }
    if (min_val == max_val)
        return 0;                          // 若 min_val 等于 max_val，直接返回 0
    int d = (max_val - min_val) / (n - 1); // 把 (max_val 减 min_val) 除以 (元素个数 减 1) 存入 d
    if (d < 1)
        d = 1;                                     // 若 d 小于 1) d 赋值为 1;
    int bucket_size = (max_val - min_val) / d + 1; // 把 (max_val 减 min_val) 除以 d 加 1 存入 bucket_size
    int(*buckets)[2] = malloc(sizeof(int) * 2 * bucket_size);
    for (int i = 0; i < bucket_size; i++) {
        buckets[i][0] = -1;
        buckets[i][1] = -1;
    }                             // 让 下标 i 从 0 开始计数，下标 i 小于 bucket_size 就继续
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        int idx = (nums[i] - min_val) / d; // 把 (数组[下标 i] 减 min_val) 除以 d 存入 idx
        if (buckets[idx][0] == -1) {
            buckets[idx][0] = nums[i];
            buckets[idx][1] = nums[i];
        } else { // 否则
            if (nums[i] < buckets[idx][0])
                buckets[idx][0] =
                    nums[i]; // 若 数组[下标 i] 小于 buckets[idx][0]) buckets[idx][0] 赋值为 数组[下标 i];
            if (nums[i] > buckets[idx][1])
                buckets[idx][1] =
                    nums[i]; // 若 数组[下标 i] 超过 buckets[idx][1]) buckets[idx][1] 赋值为 数组[下标 i];
        }
    }
    int ans = 0, prev_max = -1;             // 把 0, prev_max 赋值为 减 1 存入 答案
    for (int i = 0; i < bucket_size; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 bucket_size 就继续
        if (buckets[i][0] == -1)
            continue; // 若 buckets[下标 i][0] 等于 减 1) continue;
        if (prev_max != -1 && buckets[i][0] - prev_max > ans)
            ans = buckets[i][0] - prev_max;
        prev_max = buckets[i][1]; // 把 buckets[下标 i][1]; 写入 prev_max
    }
    free(buckets); // free(buckets);
    return ans;    // 返回 答案
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (maximum_gap((int[]){1, 2, 3}, 3) != 1) {
        printf("FAIL 1\n");
        return 1;
    }
    if (maximum_gap((int[]){3, 6, 9, 1}, 4) != 3) {
        printf("FAIL 2\n");
        return 1;
    }
    if (maximum_gap((int[]){10}, 1) != 0) {
        printf("FAIL 3\n");
        return 1;
    }
    if (maximum_gap(NULL, 0) != 0) {
        printf("FAIL 4\n");
        return 1;
    } // 若 maximum_gap(NULL, 0) 不等于 0) { 输出「FAIL 4 」); return 1; }
    if (maximum_gap((int[]){1, 10000000}, 2) != 9999999) {
        printf("FAIL 5\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
