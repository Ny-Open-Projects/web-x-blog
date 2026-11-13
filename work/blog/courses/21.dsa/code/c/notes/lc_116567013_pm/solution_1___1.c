/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
 * LeetCode 116567013. PM — C 版（方案1：Brute-Force 主串指针回退）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

static long match_v1(const char *p, const char *t) { // 定义函数/方法 match_v1
    long n = strlen(t), m = strlen(p); // 把 strlen(另一字符串), 映射表 赋值为 strlen(节点); 写入 long n
    long i = 0, j = 0;                 // 把 0, 下标 j 赋值为 0; 写入 long i
    while (j < m && i < n) { // 循环，直到不满足「下标 j 小于 映射表 且 下标 i 小于 元素个数」
        if (t[i] == p[j]) { // 若 另一字符串[下标 i] 等于 节点[下标 j]
            i++;
            j++;                                           // 下标 i 加一 ; 下标 j 加一 ;
        } else {                                           // 否则
            i -= j - 1; /* 主串回退到本次对齐的下一位置 */ // 把 下标 j 减 1; 除以 乘
                                                           // 主串回退到本次对齐的下一位置 乘 除以 写入 i -
            j = 0; // 把 0; 写入 下标 j
        }
    }
    return j == m ? i - j : -1; // 返回 下标 j 等于 映射表 ? 下标 i 减 下标 j : 减 1
}

int main(void) { // 程序入口：跑内嵌自测用例
    const char *T = "now is the time for all good people to come";
    struct {
        const char *p;
        const char *t;
        long want;
    } cases[] = {
        {"people", T, 29},
        {"good", T, 24},
        {"xyz", T, -1},
        {"a", "", -1},
        /* 边界：空文本 */ // {「数组」, 「数组」, 减 1}, 除以 乘 边界：空文本 乘 除以
        {"is", T, 4},
    };
    for (int idx = 0; idx < 5; idx++) { // 让 idx 从 0 开始计数，idx 小于 5 就继续
        long got = match_v1(
            cases[idx].p, cases[idx].t); // 把 match_v1(cases[idx].节点, cases[idx].另一字符串); 写入 long got
        if (got != cases[idx].want) { // 若 got 不等于 cases[idx].want
            printf("case %d failed: match_v1(%s)=%ld want %ld\n", idx, cases[idx].p, got,
                   cases[idx].want); // 打印输出
            return 1;                // 返回 1
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
