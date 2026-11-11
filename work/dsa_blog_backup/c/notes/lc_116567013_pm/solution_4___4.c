/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
 * LeetCode 116567013. PM — C 版（方案4：buildNext 单测）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

static long long N[64]; // static long long N[64];

static void build_next(const char *p) { // 定义函数/方法 build_next
    long long m = strlen(p);            // 把 strlen(节点) 存入 映射表
    for (long long i = 0; i < m; i++)
        N[i] = -1;           // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
    long long j = 0, t = -1; // 把 0, 另一字符串 赋值为 减 1 存入 下标 j
    while (j < m - 1) {      // 循环，直到不满足「下标 j 小于 映射表 减 1」
        if (t < 0 || p[j] == p[t]) { // 若 另一字符串 小于 0 或 节点[下标 j] 等于 节点[另一字符串]
            j++;
            t++;      // 下标 j 加一 ; 另一字符串 加一 ;
            N[j] = t; // 把 另一字符串; 写入 N[j]
        } else {      // 否则
            t = N[t]; // 把 N[另一字符串]; 写入 另一字符串
        }
    }
}

static int eq_arr(const long long *a, const long long *b, int n) { // 定义函数/方法 eq_arr
    for (int i = 0; i < n; i++)
        if (a[i] != b[i])
            return 0; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    return 1;         // 返回 1
}

int main(void) {                              // 程序入口：跑内嵌自测用例
    long long w1[7] = {-1, 0, 0, 1, 2, 3, 0}; // 把 { 减 1, 0, 0, 1, 2, 3, 0}; 写入 long long w1[7]
    build_next("ababaca");                    // build_next(「ababaca」);
    if (!eq_arr(N, w1, 7)) {
        printf("ababaca failed\n");
        return 1;
    } // 若 取反 eq_arr(N, w1, 7)) { 输出「ababaca failed 」); return 1; }
    long long w2[4] = {-1, 0, 1, 2}; // 把 { 减 1, 0, 1, 2}; 写入 long long w2[4]
    build_next("aaaa");              // build_next(「aaaa」);
    if (!eq_arr(N, w2, 4)) {
        printf("aaaa failed\n");
        return 1;
    } // 若 取反 eq_arr(N, w2, 4)) { 输出「aaaa failed 」); return 1; }
    long long w5[6] = {-1, 0, 0, 0, 1, 2}; // 把 { 减 1, 0, 0, 0, 1, 2}; 写入 long long w5[6]
    build_next("abcabc");                  // build_next(「abcabc」);
    if (!eq_arr(N, w5, 6)) {
        printf("abcabc failed\n");
        return 1;
    } // 若 取反 eq_arr(N, w5, 6)) { 输出「abcabc failed 」); return 1; }
    long long w3[4] = {-1, 0, 0, 0}; // 把 { 减 1, 0, 0, 0}; 写入 long long w3[4]
    build_next("abcd");              // build_next(「abcd」);
    if (!eq_arr(N, w3, 4)) {
        printf("abcd failed\n");
        return 1;
    }                       // 若 取反 eq_arr(N, w3, 4)) { 输出「abcd failed 」); return 1; }
    long long w4[1] = {-1}; // 把 { 减 1}; 写入 long long w4[1]
    build_next("a");        // build_next(「数组」);
    if (!eq_arr(N, w4, 1)) {
        printf("a failed\n");
        return 1;
    }                 // 若 取反 eq_arr(N, w4, 1)) { 输出「数组 failed 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
