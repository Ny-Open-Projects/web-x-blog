/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689
 * LeetCode 113951689. 动态规划之 LCS — C 版（最长公共子序列：DP 填表 + 回溯构造）
 */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件

#define MAXN 64 // #define MAXN 64

static int lcs_table(const char *a, const char *b, int dp[][MAXN]) { // 定义函数/方法 lcs_table
    int m = (int)strlen(a),
        n = (int)strlen(b); // 把 (int)strlen(数组), 元素个数 赋值为 (int)strlen(b) 存入 映射表
    for (int i = 0; i <= m; i++) // 让 下标 i 从 0 开始计数，下标 i 不超过 映射表 就继续
        for (int j = 0; j <= n; j++)
            dp[i][j] = 0; // 让 下标 j 从 0 开始计数，下标 j 不超过 元素个数 就继续
    for (int i = 1; i <= m; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
        for (int j = 1; j <= n; j++) { // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
            if (a[i - 1] == b[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            else
                dp[i][j] = dp[i - 1][j] > dp[i][j - 1] ? dp[i - 1][j] : dp[i][j - 1]; // 否则
        }
    }
    return dp[m][n]; // 返回 DP 表[映射表][元素个数]
}

static int lcs_length(const char *a, const char *b) { // 定义函数/方法 lcs_length
    int dp[MAXN][MAXN];                               // int DP 表[MAXN][MAXN];
    return lcs_table(a, b, dp);                       // 返回 lcs_table(数组, b, DP 表)
}

static void lcs_string(const char *a, const char *b, char *out) { // 定义函数/方法 lcs_string
    int dp[MAXN][MAXN];                                           // int DP 表[MAXN][MAXN];
    lcs_table(a, b, dp);                                          // lcs_table(数组, b, DP 表);
    int m = (int)strlen(a),
        n = (int)strlen(b); // 把 (int)strlen(数组), 元素个数 赋值为 (int)strlen(b) 存入 映射表
    char buf[MAXN];         // char buf[MAXN];
    int k = 0;              // 把 0 存入 下标 k
    int i = m, j = n;       // 把 映射表, 下标 j 赋值为 元素个数 存入 下标 i
    while (i > 0 && j > 0) {        // 循环，直到不满足「下标 i 超过 0 且 下标 j 超过 0」
        if (a[i - 1] == b[j - 1]) { // 若 数组[下标 i 减 1] 等于 b[下标 j 减 1]
            buf[k++] = a[i - 1];    // 把 数组[下标 i 减 1]; 写入 buf[k++]
            i--;
            j--; // 下标 i 减一 ; 下标 j 减一 ;
        } else if (dp[i - 1][j] >=
                   dp[i][j - 1]) { // 否则，若 DP 表[下标 i 减 1][下标 j] 不低于 DP 表[下标 i][下标 j 减 1]
            i--;                   // 下标 i 减一
        } else {                   // 否则
            j--;                   // 下标 j 减一
        }
    }
    /* 反转 */
    for (int t = 0; t < k; t++)
        out[t] = buf[k - 1 - t]; // 让 另一字符串 从 0 开始计数，另一字符串 小于 下标 k 就继续
    out[k] = 0;                  // 把 0; 写入 out[k]
}

static int is_common_sub(const char *a, const char *b, const char *s) { // 定义判定函数 is_common_sub
    int ia = 0, ib = 0;                                                 // 把 0, ib 赋值为 0 存入 ia
    for (int k = 0; s[k]; k++) { // 让 下标 k 从 0 开始计数，字符串[下标 k] 就继续
        while (a[ia] && a[ia] != s[k])
            ia++; // 循环，直到不满足「数组[ia] 且 数组[ia] 不等于 字符串[下标 k]) ia 加一 ;」
        while (b[ib] && b[ib] != s[k])
            ib++; // 循环，直到不满足「b[ib] 且 b[ib] 不等于 字符串[下标 k]) ib 加一 ;」
        if (!a[ia] || !b[ib])
            return 0; // 若 取反 数组[ia] 或 取反 b[ib]，直接返回 0
        ia++;
        ib++; // ia 加一 ; ib 加一 ;
    }
    return 1; // 返回 1
}

int main(void) { // 程序入口：跑内嵌自测用例
    struct {
        const char *a, *b;
        int want;
    } cases[] = {
        // 把 { 写入 struct { const char *a, *b; int want; } cases[]
        {"ABCBDAB", "BDCABA", 4}, {"AGGTAB", "GXTXAYB", 4}, {"abc", "abc", 3},
        {"", "abc", 0},           {"abc", "xyz", 0},
    };
    for (int idx = 0; idx < 5; idx++) { // 让 idx 从 0 开始计数，idx 小于 5 就继续
        int got =
            lcs_length(cases[idx].a, cases[idx].b); // 把 lcs_length(cases[idx].数组, cases[idx].b) 存入 got
        if (got != cases[idx].want) {               // 若 got 不等于 cases[idx].want
            printf("case %d failed: got %d want %d\n", idx, got, cases[idx].want); // 打印输出
            return 1;                                                              // 返回 1
        }
    }
    const char *pairs[2][2] = {{"ABCBDAB", "BDCABA"}, {"AGGTAB", "GXTXAYB"}};
    for (int p = 0; p < 2; p++) {                // 让 节点 从 0 开始计数，节点 小于 2 就继续
        char s[MAXN];                            // char 字符串[MAXN];
        lcs_string(pairs[p][0], pairs[p][1], s); // lcs_string(pairs[节点][0], pairs[节点][1], 字符串);
        if ((int)strlen(s) != lcs_length(pairs[p][0], pairs[p][1]) ||
            !is_common_sub(pairs[p][0], pairs[p][1],
                           s)) { // 取反 is_common_sub(pairs[节点][0], pairs[节点][1], 字符串)) {
            printf("lcs_string failed: %s\n", s); // 打印输出
            return 1;                             // 返回 1
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
