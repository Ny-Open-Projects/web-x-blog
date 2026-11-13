/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133547933 */
/* LeetCode 313. 超级丑数 — C 版（方案2） */
#include <stdio.h>                                                     // 引入头文件
static long nth_super_ugly_number(int n, const long *primes, int np) { // 定义函数/方法 nth_super_ugly_number
    long ugly[1024];                                                   // long ugly[1024];
    int idx[64];                                                       // int idx[64];
    long val[64];                                                      // long 值[64];
    ugly[0] = 1;                                                       // 把 1; 写入 ugly[0]
    for (int k = 0; k < np; k++) {
        idx[k] = 0;
        val[k] = primes[k];
    }                             // 让 下标 k 从 0 开始计数，下标 k 小于 np 就继续
    for (int i = 1; i < n; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
        long next = ~0UL >> 1;    // 把 ~0UL 超过 超过 1; 写入 long next
        for (int k = 0; k < np; k++)
            if (val[k] < next)
                next = val[k];         // 让 下标 k 从 0 开始计数，下标 k 小于 np 就继续
        ugly[i] = next;                // 把 下一个; 写入 ugly[i]
        for (int k = 0; k < np; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 np 就继续
            if (val[k] == next) {
                idx[k]++;
                val[k] = ugly[idx[k]] * primes[k];
            }
        }
    }
    return ugly[n - 1]; // 返回 ugly[元素个数 减 1]
}
int main(void) {               // 程序入口：跑内嵌自测用例
    long p[] = {2, 7, 13, 19}; // 把 {2, 7, 13, 19}; 写入 long p[]
    if (nth_super_ugly_number(12, p, 4) != 32) {
        printf("FAIL 1\n");
        return 1;
    }
    if (nth_super_ugly_number(1, p, 4) != 1) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
