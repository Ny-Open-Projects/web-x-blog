/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133772625 */
/* LeetCode 131. 分割回文串 — C 版（方案2） */
#include <stdio.h>                               // 引入头文件
#include <string.h>                              // 引入头文件
static char res[256][32][32];                    // static char 结果[256][32][32];
static int res_lens[256], res_n;                 // static int res_lens[256], res_n;
static char path[32][32];                        // static char 当前路径[32][32];
static int path_n;                               // static int path_n;
static int is_pal(const char *s, int l, int r) { // 定义判定函数 is_pal
    while (l < r) {                              // 循环，直到不满足「左指针 小于 右指针」
        if (s[l] != s[r])
            return 0; // 若 字符串[左指针] 不等于 字符串[右指针]，直接返回 0
        l++;
        r--; // 左指针 加一 ; 右指针 减一 ;
    }
    return 1; // 返回 1
}
static void dfs(const char *s, int n, int start) { // 定义函数/方法 dfs
    if (start == n) {                              // 若 起点 等于 元素个数
        for (int i = 0; i < path_n; i++)
            strcpy(res[res_n][i], path[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 path_n 就继续
        res_lens[res_n] = path_n;           // 把 path_n; 写入 res_lens[res_n]
        res_n++;                            // res_n 加一
        return;                             // return;
    }
    for (int e = start; e < n; e++) { // 让 e 从 起点 开始计数，e 小于 元素个数 就继续
        if (is_pal(s, start, e)) {    // 若 is_pal(字符串, 起点, e
            int len = e - start + 1;  // 把 e 减 起点 加 1 存入 长度
            strncpy(path[path_n], s + start, len); // strncpy(当前路径[path_n], 字符串 加 起点, 长度);
            path[path_n][len] = '\0';              // 把 '\0'; 写入 path[path_n][len]
            path_n++;                              // path_n 加一
            dfs(s, n, e + 1);                      // dfs(字符串, 元素个数, e 加 1);
            path_n--;                              // path_n 减一
        }
    }
}
static int partition(const char *s) { // 定义函数/方法 partition
    res_n = 0;
    path_n = 0;                // 把 0; path_n 赋值为 0; 写入 res_n
    dfs(s, (int)strlen(s), 0); // dfs(字符串, (int)strlen(字符串), 0);
    return res_n;              // 返回 res_n
}
int main(void) {              // 程序入口：跑内嵌自测用例
    int n = partition("aab"); // 把 partition(「aab」) 存入 元素个数
    if (n != 2) {
        printf("FAIL cnt=%d\n", n);
        return 1;
    } // 若 元素个数 不等于 2) { 输出「FAIL 计数 赋值为 对…取模 d 」, 元素个数); return 1; }
    if (res_lens[0] != 3 || strcmp(res[0][0], "a") != 0 || strcmp(res[0][2], "b") != 0) {
        printf("FAIL a\n");
        return 1;
    }
    if (res_lens[1] != 2 || strcmp(res[1][0], "aa") != 0) {
        printf("FAIL b\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
