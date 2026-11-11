/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
 * LeetCode 621. 任务调度器 — C 版 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

/* 方案4（26 位频率桶公式法） */
static int least_interval(const char *tasks, int n) { // 定义函数/方法 least_interval
    int freq[26] = {0};                               // 把 { 0 }; 写入 int freq[26]
    int len = (int)strlen(tasks);                     // 把 (int)strlen(tasks) 存入 长度
    for (int i = 0; i < len; i++)
        freq[tasks[i] - 'A']++;    // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
    int max_freq = 0;              // 把 0 存入 max_freq
    for (int i = 0; i < 26; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 26 就继续
        if (freq[i] > max_freq)
            max_freq = freq[i]; // 若 频次表[下标 i] 超过 max_freq) max_freq 赋值为 频次表[下标 i];
    }
    int same = 0;                  // 把 0 存入 same
    for (int i = 0; i < 26; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 26 就继续
        if (freq[i] == max_freq)
            same++; // 若 频次表[下标 i] 等于 max_freq) same 加一 ;
    }
    int formula =
        (max_freq - 1) * (n + 1) + same; // 把 (max_freq 减 1) 乘 (元素个数 加 1) 加 same 存入 formula
    return formula > len ? formula : len; // 返回 formula 超过 长度 ? formula : 长度
}

int main(void) { // 程序入口：跑内嵌自测用例
    /* 与 TS 事实源内嵌用例一致 */
    struct {
        const char *tasks;
        int n;
        int want;
    } cases[] = {
        {"AAABBB", 2, 8},
        {"AAAA", 2, 10},
        {"ABCD", 0, 4},
    };
    int n = (int)(sizeof(cases) /
                  sizeof(cases[0])); // 把 (int)(sizeof(cases) 除以 sizeof(cases[0])) 存入 元素个数
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        int got = least_interval(
            cases[i].tasks,
            cases[i].n); // 把 least_interval(cases[下标 i].tasks, cases[下标 i].元素个数) 存入 got
        if (got != cases[i].want) { // 若 got 不等于 cases[下标 i].want
            printf("FAIL case %d got %d want %d\n", i, got, cases[i].want); // 打印输出
            return 1;                                                       // 返回 1
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
