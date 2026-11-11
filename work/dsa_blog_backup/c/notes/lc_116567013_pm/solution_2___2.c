/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
 * LeetCode 116567013. PM — C 版（方案2：Brute-Force 双循环对齐）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

static long match_v2(const char *p, const char *t) { // 定义函数/方法 match_v2
    long n = strlen(t), m = strlen(p); // 把 strlen(另一字符串), 映射表 赋值为 strlen(节点); 写入 long n
    if (m == 0 || n < m)
        return -1; // 若 映射表 等于 0 或 元素个数 小于 映射表，直接返回 减 1
    for (long i = 0; i <= n - m;
         i++) { // 把 0; 下标 i 不超过 元素个数 减 映射表; 下标 i 加一 ) { 写入 for (long i
        long j = 0; // 把 0; 写入 long j
        while (j < m && t[i + j] == p[j])
            j++;
        if (j == m)
            return i; // 若 下标 j 等于 映射表，直接返回 下标 i
    }
    return -1; // 返回 减 1
}

int main(void) { // 程序入口：跑内嵌自测用例
    const char *T = "now is the time for all good people to come";
    struct {
        const char *p;
        const char *t;
        long want;
    } cases[] = {
        {"people", T, 29}, {"time", T, 11}, {"all", T, 20}, {"xyz", T, -1}, {"a", "", -1}, {"is", T, 4},
    };
    for (int idx = 0; idx < 6; idx++) { // 让 idx 从 0 开始计数，idx 小于 6 就继续
        long got = match_v2(
            cases[idx].p, cases[idx].t); // 把 match_v2(cases[idx].节点, cases[idx].另一字符串); 写入 long got
        if (got != cases[idx].want) {
            printf("case %d failed\n", idx);
            return 1;
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
