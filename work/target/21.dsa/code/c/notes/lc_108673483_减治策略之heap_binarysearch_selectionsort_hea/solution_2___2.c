/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
 * LeetCode 108673483. 减治策略 — C 版（方案2：快速选择求第 k 小，k 从 0 起）
 */
#include <stdio.h> // 引入头文件

static int select_k(int *a, int lo, int hi, int k) { // 定义函数/方法 select_k
    if (lo == hi)
        return a[lo];               // 若 左边界 等于 右边界，直接返回 数组[左边界]
    int pivot = a[hi];              // 把 数组[右边界] 存入 pivot
    int i = lo;                     // 把 左边界 存入 下标 i
    for (int j = lo; j < hi; j++) { // 让 下标 j 从 左边界 开始计数，下标 j 小于 右边界 就继续
        if (a[j] <= pivot) {        // 若 数组[下标 j] 不超过 pivot
            int t = a[i];
            a[i] = a[j];
            a[j] = t;
            i++; // 下标 i 加一
        }
    }
    int t = a[i];
    a[i] = a[hi];
    a[hi] = t; // 把 数组[下标 i]; 数组[下标 i] 赋值为 数组[右边界]; 数组[右边界] 赋值为 另一字符串 存入
               // 另一字符串
    if (i == k)
        return a[i]; // 若 下标 i 等于 下标 k，直接返回 数组[下标 i]
    if (i > k)
        return select_k(a, lo, i - 1,
                        k); // 若 下标 i 超过 下标 k，直接返回 select_k(数组, 左边界, 下标 i 减 1, 下标 k)
    return select_k(a, i + 1, hi, k); // 返回 select_k(数组, 下标 i 加 1, 右边界, 下标 k)
}

int main(void) {                            // 程序入口：跑内嵌自测用例
    int base[8] = {3, 1, 4, 1, 5, 9, 2, 6}; // 把 {3, 1, 4, 1, 5, 9, 2, 6}; 写入 int base[8]
    int ks[4] = {2, 3, 0, 7};               // 把 {2, 3, 0, 7}; 写入 int ks[4]
    int ws[4] = {2, 3, 1, 9};               // 把 {2, 3, 1, 9}; 写入 int ws[4]
    for (int idx = 0; idx < 4; idx++) {     // 让 idx 从 0 开始计数，idx 小于 4 就继续
        int a[8];                           // int 数组[8];
        for (int i = 0; i < 8; i++)
            a[i] = base[i];                   // 让 下标 i 从 0 开始计数，下标 i 小于 8 就继续
        int got = select_k(a, 0, 7, ks[idx]); // 把 select_k(数组, 0, 7, ks[idx]) 存入 got
        if (got != ws[idx]) {
            printf("case %d failed\n", idx);
            return 1;
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
