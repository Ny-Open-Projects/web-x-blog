/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135756434 */
/* LeetCode 696. 计数二进制子串 — C 版（方案6） */
#include <stdio.h>                                  // 引入头文件
#include <string.h>                                 // 引入头文件
static int count_binary_substrings(const char *s) { // 定义函数/方法 count_binary_substrings
    int groups[8192], gn = 0;                       // 把 0; 写入 int groups[8192], gn
    int n = (int)strlen(s);                         // 把 (int)strlen(字符串) 存入 元素个数
    int i = 0;                                      // 把 0 存入 下标 i
    while (i < n) {     // 循环，直到不满足「下标 i 小于 元素个数」
        char ch = s[i]; // 把 字符串[下标 i]; 写入 char ch
        int cnt = 0;    // 把 0 存入 计数
        while (i < n && s[i] == ch) {
            cnt++;
            i++;
        }
        groups[gn++] = cnt; // 把 计数; 写入 groups[gn++]
    }
    int ans = 0;                   // 把 0 存入 答案
    for (int k = 1; k < gn; k++) { // 让 下标 k 从 1 开始计数，下标 k 小于 gn 就继续
        int m = groups[k - 1] < groups[k] ? groups[k - 1] : groups[k];
        ans += m; // 答案累加 映射表
    }
    return ans; // 返回 答案
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (count_binary_substrings("00110011") != 6) {
        printf("FAIL 1\n");
        return 1;
    }
    if (count_binary_substrings("10101") != 4) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
