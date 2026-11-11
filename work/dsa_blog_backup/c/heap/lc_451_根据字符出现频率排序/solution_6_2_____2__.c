/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137060905 */
/* LeetCode 451. 根据字符出现频率排序 — C 版（方案6） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
#include <string.h> // 引入头文件
typedef struct {
    char c;
    int cnt;
    int first;
} FC; // typedef struct { char 字符; int 计数; int first; } FC;
static int cmp_fc(const void *a, const void *b) { // 定义函数/方法 cmp_fc
    const FC *x = a, *y = b;                      // 把 数组, 乘 y 赋值为 b; 写入 const FC *x
    if (x->cnt != y->cnt)
        return y->cnt -
               x->cnt; // 若 x 减 超过 计数 不等于 y 减 超过 计数，直接返回 y 减 超过 计数 减 x 减 超过 计数
    return x->first - y->first; // 返回 x 减 超过 first 减 y 减 超过 first
}
static void frequency_sort(const char *s, char out[]) { // 定义函数/方法 frequency_sort
    FC fcs[256];                                        // FC fcs[256];
    int n = 0;                                          // 把 0 存入 元素个数
    int seen[256] = {0};                                // 把 {0}; 写入 int seen[256]
    for (const char *p = s; *p; p++) { // 把 字符串; 乘 节点; 节点 加一 ) { 写入 for (const char *p
        unsigned char c = (unsigned char)*p; // 把 (unsigned char) 乘 节点; 写入 unsigned char c
        if (!seen[c]) {
            seen[c] = 1;
            fcs[n].c = c;
            fcs[n].cnt = 0;
            fcs[n].first = (int)(p - s);
            n++;
        }
        fcs[0].cnt += 0; // noop
        for (int k = 0; k < n; k++)
            if (fcs[k].c == c) {
                fcs[k].cnt++;
                break;
            } // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
    }
    qsort(fcs, n, sizeof(FC), cmp_fc); // qsort(fcs, 元素个数, sizeof(FC), cmp_fc);
    int pos = 0;                       // 把 0 存入 pos
    for (int k = 0; k < n; k++) // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
        for (int j = 0; j < fcs[k].cnt; j++)
            out[pos++] = fcs[k].c; // 让 下标 j 从 0 开始计数，下标 j 小于 fcs[下标 k].计数 就继续
    out[pos] = '\0';               // 把 '\0'; 写入 out[pos]
}
int main(void) {                 // 程序入口：跑内嵌自测用例
    char out[4096];              // char out[4096];
    frequency_sort("tree", out); // frequency_sort(「tree」, out);
    if (strcmp(out, "eetr") != 0) {
        printf("FAIL 1 %s\n", out);
        return 1;
    }                        // 若 strcmp(out, 「eetr」) 不等于 0) { 输出「eetr」, out); return 1; }
    frequency_sort("", out); // frequency_sort(「」, out);
    if (strcmp(out, "") != 0) {
        printf("FAIL 2\n");
        return 1;
    }                              // 若 strcmp(out, 「」) 不等于 0) { 输出「」); return 1; }
    frequency_sort("cccaaa", out); // frequency_sort(「cccaaa」, out);
    if (strcmp(out, "cccaaa") != 0) {
        printf("FAIL 3 %s\n", out);
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
