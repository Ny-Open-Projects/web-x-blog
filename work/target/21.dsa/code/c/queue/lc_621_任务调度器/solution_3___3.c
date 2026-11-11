/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
 * LeetCode 621. 任务调度器 — C 版 */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
#include <string.h> // 引入头文件

static int cmp_desc(const void *a, const void *b) { // 定义函数/方法 cmp_desc
    int x = *(const int *)a,
        y = *(const int *)b; // 把 乘 (const int 乘 )数组, y 赋值为 乘 (const int 乘 )b 存入 x
    return (x < y) - (x > y); /* 降序 */ // 返回 (x 小于 y) 减 (x 超过 y); 除以 乘 降序 乘 除以
}

/* 方案3（贪心模拟，每轮取剩余次数最多的 n+1 个，最后一轮只计实际执行数） */
static int least_interval(const char *tasks, int n) { // 定义函数/方法 least_interval
    int freq[26] = {0};                               // 把 { 0 }; 写入 int freq[26]
    int len = (int)strlen(tasks);                     // 把 (int)strlen(tasks) 存入 长度
    for (int i = 0; i < len; i++)
        freq[tasks[i] - 'A']++;    // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
    int cnt[27];                   // int 计数[27];
    int cnt_len = 0;               // 把 0 存入 cnt_len
    for (int i = 0; i < 26; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 26 就继续
        if (freq[i] > 0)
            cnt[cnt_len++] = freq[i]; // 若 频次表[下标 i] 超过 0) 计数[cnt_len 加一 ] 赋值为 频次表[下标 i];
    }
    int time = 0;         // 把 0 存入 time
    while (cnt_len > 0) { // 循环，直到不满足「cnt_len 超过 0」
        qsort(cnt, (size_t)cnt_len, sizeof(int),
              cmp_desc); // qsort(计数, (size_t)cnt_len, sizeof(int), cmp_desc);
        int used = 0;    // 把 0 存入 已用标记
        int take = n + 1 < cnt_len
                       ? n + 1
                       : cnt_len; // 把 元素个数 加 1 小于 cnt_len ? 元素个数 加 1 : cnt_len 存入 take
        for (int i = 0; i < take; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 take 就继续
            if (cnt[i] > 0) {            // 若 计数[下标 i] 超过 0
                cnt[i] -= 1;             // cnt[i]累减 1
                used++;                  // 已用标记 加一
            }
        }
        int new_len = 0;                    // 把 0 存入 new_len
        for (int i = 0; i < cnt_len; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 cnt_len 就继续
            if (cnt[i] > 0)
                cnt[new_len++] = cnt[i]; // 若 计数[下标 i] 超过 0) 计数[new_len 加一 ] 赋值为 计数[下标 i];
        }
        cnt_len = new_len;                  // 把 new_len; 写入 cnt_len
        time += cnt_len > 0 ? n + 1 : used; // time累加 cnt_len 超过 0 ? 元素个数 加 1 : 已用标记
    }
    return time; // 返回 time
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
