/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135004189 */
/* LeetCode 3. 无重复字符的最长子串 — C 版（方案3） */
#include <stdio.h>                                      // 引入头文件
#include <string.h>                                     // 引入头文件
static int length_of_longest_substring(const char *s) { // 定义函数/方法 length_of_longest_substring
    int set[256] = {0};                                 // 把 {0}; 写入 int set[256]
    int left = 0, max_len = 0;                          // 把 0, max_len 赋值为 0 存入 左边界
    int n = (int)strlen(s);                             // 把 (int)strlen(字符串) 存入 元素个数
    for (int right = 0; right < n; right++) { // 让 右边界 从 0 开始计数，右边界 小于 元素个数 就继续
        while (set[(unsigned char)s[right]]) { // 循环，直到不满足「set[(unsigned char)字符串[右边界]]」
            set[(unsigned char)s[left]] = 0; // 把 0; 写入 set[(unsigned char)s[left]]
            left++;                          // 左边界 加一
        }
        set[(unsigned char)s[right]] = 1; // 把 1; 写入 set[(unsigned char)s[right]]
        int len = right - left + 1;       // 把 右边界 减 左边界 加 1 存入 长度
        if (len > max_len)
            max_len = len; // 若 长度 超过 max_len) max_len 赋值为 长度;
    }
    return max_len; // 返回 max_len
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (length_of_longest_substring("abcabcbb") != 3) {
        printf("FAIL 1\n");
        return 1;
    }
    if (length_of_longest_substring("bbbbb") != 1) {
        printf("FAIL 2\n");
        return 1;
    }
    if (length_of_longest_substring("pwwkew") != 3) {
        printf("FAIL 3\n");
        return 1;
    }
    if (length_of_longest_substring("") != 0) {
        printf("FAIL 4\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
