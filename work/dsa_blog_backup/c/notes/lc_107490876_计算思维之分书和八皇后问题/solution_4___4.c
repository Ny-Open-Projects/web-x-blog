/* 来源：https://blog.csdn.net/tyro_java/article/details/107490876
 * LeetCode 107490876. 分书和八皇后问题 — C 版（方案4：八皇后显式栈迭代）
 */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
#include <string.h> // 引入头文件

#define STACK_MAX 8192 // #define STACK_MAX 8192

static int valid(int x, const int *a, int len) { // 定义函数/方法 valid
    int y = len + 1;                             // 把 长度 加 1 存入 y
    for (int i = 1; i <= len; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 长度 就继续
        if (x == a[i - 1] || abs(y - i) == abs(x - a[i - 1]))
            return 0;
    }
    return 1; // 返回 1
}

static int run_case(int n, int sols[][8]) { // 定义函数/方法 run_case
    static int stack[STACK_MAX][9];         // static int 栈[STACK_MAX][9];
    static int slen[STACK_MAX];             // static int slen[STACK_MAX];
    int top = 0;                            // 把 0 存入 top
    slen[top] = 0; /* 空盘入栈 */           // 把 0; 除以 乘 空盘入栈 乘 除以 写入 slen[top]
    top++;                                  // top 加一
    int sol_count = 0;                      // 把 0 存入 sol_count
    while (top > 0) {                       // 循环，直到不满足「top 超过 0」
        top--;                              // top 减一
        const int *a = stack[top];          // 把 栈[top]; 写入 const int *a
        int alen = slen[top];               // 把 slen[top] 存入 alen
        if (alen == n) {                    // 若 alen 等于 元素个数
            memcpy(sols[sol_count], a,
                   sizeof(int) * n); // memcpy(sols[sol_count], 数组, sizeof(int) 乘 元素个数);
            sol_count++;             // sol_count 加一
        } else {                     // 否则
            for (int i = 1; i <= n; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
                if (valid(i, a, alen)) {                       // 若 valid(下标 i, 数组, alen
                    memcpy(stack[top], a, sizeof(int) * alen); // memcpy(栈[top], 数组, sizeof(int) 乘 alen);
                    stack[top][alen] = i;                      // 把 下标 i; 写入 stack[top][alen]
                    slen[top] = alen + 1;                      // 把 alen 加 1; 写入 slen[top]
                    top++;                                     // top 加一
                }
            }
        }
    }
    return sol_count; // 返回 sol_count
}

int main(void) {             // 程序入口：跑内嵌自测用例
    static int sols[100][8]; // static int sols[100][8];
    struct {
        int n;
        int count;
        int has_first;
        int first[8];
    } cases[] = {
        {8, 92, 1, {8, 4, 1, 3, 6, 2, 7, 5}},
        {1, 1, 1, {1}},
        {2, 0, 0, {0}},
        {4, 2, 1, {3, 1, 4, 2}},
    };
    for (int idx = 0; idx < 4; idx++) {           // 让 idx 从 0 开始计数，idx 小于 4 就继续
        int count = run_case(cases[idx].n, sols); // 把 run_case(cases[idx].元素个数, sols) 存入 计数
        if (count != cases[idx].count) {
            printf("case %d count %d\n", idx, count);
            return 1;
        }
        if (cases[idx].has_first) { // 若 cases[idx].has_first
            for (int j = 0; j < cases[idx].n;
                 j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 cases[idx].元素个数 就继续
                if (sols[0][j] != cases[idx].first[j]) {
                    printf("case %d first\n", idx);
                    return 1;
                }
            }
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
