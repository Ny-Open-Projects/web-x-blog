/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
 * LeetCode 116567013. PM — C 版（方案3：KMP，next 表失配大步跳跃）
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

static long long kmp_match(const char *p, const char *t) {
    build_next(p);                          // build_next(节点);
    long long n = strlen(t), m = strlen(p); // 把 strlen(另一字符串), 映射表 赋值为 strlen(节点) 存入 元素个数
    long long i = 0, j = 0; // 把 0, 下标 j 赋值为 0 存入 下标 i
    while (j < m && i < n) { // 循环，直到不满足「下标 j 小于 映射表 且 下标 i 小于 元素个数」
        if (j < 0 || t[i] == p[j]) { // 若 下标 j 小于 0 或 另一字符串[下标 i] 等于 节点[下标 j]
            i++;
            j++;      // 下标 i 加一 ; 下标 j 加一 ;
        } else {      // 否则
            j = N[j]; // 把 N[下标 j]; 写入 下标 j
        }
    }
    return j == m ? i - j : -1; // 返回 下标 j 等于 映射表 ? 下标 i 减 下标 j : 减 1
}

static int eq_arr(const long long *a, const long long *b, int n) { // 定义函数/方法 eq_arr
    for (int i = 0; i < n; i++)
        if (a[i] != b[i])
            return 0; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    return 1;         // 返回 1
}

int main(void) { // 程序入口：跑内嵌自测用例
    const char *T = "now is the time for all good people to come";
    struct {
        const char *p;
        const char *t;
        long long want;
    } cases[] = {
        {"people", T, 29}, {"all", T, 20}, {"no", T, 0}, {"xyz", T, -1}, {"a", "", -1},
    };
    for (int idx = 0; idx < 5; idx++) { // 让 idx 从 0 开始计数，idx 小于 5 就继续
        if (kmp_match(cases[idx].p, cases[idx].t) != cases[idx].want) {
            printf("case %d failed\n", idx); // 打印输出
            return 1;                        // 返回 1
        }
    }
    if (kmp_match("aaaa", "aaaaa") != 0) {
        printf("overlap failed\n");
        return 1;
    } // 若 kmp_match(「aaaa」, 「aaaa」) 不等于 0) { 输出「aaaa」); return 1; }
    if (kmp_match("aaab", "aaabaaa") != 0) {
        printf("reuse failed\n");
        return 1;
    } // 若 kmp_match(「aaab」, 「aaab」) 不等于 0) { 输出「aaab」); return 1; }

    long long w1[7] = {-1, 0, 0, 1, 2, 3, 0}; // 把 { 减 1, 0, 0, 1, 2, 3, 0}; 写入 long long w1[7]
    build_next("ababaca");                    // build_next(「ababaca」);
    if (!eq_arr(N, w1, 7)) {
        printf("next ababaca failed\n");
        return 1;
    }
    long long w2[4] = {-1, 0, 1, 2}; // 把 { 减 1, 0, 1, 2}; 写入 long long w2[4]
    build_next("aaaa");              // build_next(「aaaa」);
    if (!eq_arr(N, w2, 4)) {
        printf("next aaaa failed\n");
        return 1;
    } // 若 取反 eq_arr(N, w2, 4)) { 输出「下一个 aaaa failed 」); return 1; }
    long long w3[4] = {-1, 0, 0, 0}; // 把 { 减 1, 0, 0, 0}; 写入 long long w3[4]
    build_next("abcd");              // build_next(「abcd」);
    if (!eq_arr(N, w3, 4)) {
        printf("next abcd failed\n");
        return 1;
    }                 // 若 取反 eq_arr(N, w3, 4)) { 输出「下一个 abcd failed 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
