/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134191965 */
/* 数据结构与算法之排序: 基数排序 — C 版（方案3） */
#include <stdio.h>                       // 引入头文件
static void radix_sort(int v[], int n) { // 定义函数/方法 radix_sort
    if (n == 0)
        return;               // 若 元素个数 等于 0) return;
    int mn = v[0], mx = v[0]; // 把 值[0], mx 赋值为 值[0] 存入 mn
    for (int i = 1; i < n; i++) {
        if (v[i] < mn)
            mn = v[i];
        if (v[i] > mx)
            mx = v[i];
    }                              // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
    int offset = mn < 0 ? -mn : 0; // 把 mn 小于 0 ? 减 mn : 0 存入 offset
    long adj[4096];                // long 邻接表[4096];
    long max_adj = 0;              // 把 0; 写入 long max_adj
    for (int i = 0; i < n; i++) {
        adj[i] = v[i] + offset;
        if (adj[i] > max_adj)
            max_adj = adj[i];
    }                          // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    long radix = 1;            // 把 1; 写入 long radix
    long tmp[4096];            // long 临时变量[4096];
    while (max_adj >= radix) { // 循环，直到不满足「max_adj 不低于 radix」
        long bucket[10] = {0}; // 把 {0}; 写入 long bucket[10]
        for (int i = 0; i < n; i++)
            bucket[(adj[i] / radix) % 10]++; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (int i = 1; i < 10; i++)
            bucket[i] += bucket[i - 1]; // 让 下标 i 从 1 开始计数，下标 i 小于 10 就继续
        for (int i = n - 1; i >= 0; i--) { // 让 下标 i 从 元素个数 减 1 开始计数，下标 i 不低于 0 就继续
            int d = (int)((adj[i] / radix) % 10); // 把 (int)((邻接表[下标 i] 除以 radix) 对…取模 10) 存入 d
            tmp[--bucket[d]] = adj[i]; // 把 邻接表[下标 i]; 写入 tmp[--bucket[d]]
        }
        for (int i = 0; i < n; i++)
            adj[i] = tmp[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        radix *= 10;         // 把 10; 写入 radix *
    }
    for (int i = 0; i < n; i++)
        v[i] = (int)(adj[i] - offset); // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
}
int main(void) {                // 程序入口：跑内嵌自测用例
    int v1[] = {5, 4, 3, 2, 1}; // 把 {5,4,3,2,1}; 写入 int v1[]
    radix_sort(v1, 5);          // radix_sort(v1, 5);
    for (int i = 0; i < 5; i++)
        if (v1[i] != i + 1) {
            printf("FAIL\n");
            return 1;
        } // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS