/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975 */
/* LeetCode 557. 反转字符串中的单词III — C 版（方案14） */
#include <stdio.h>                                     // 引入头文件
#include <string.h>                                    // 引入头文件
static void reverse_words(const char *s, char out[]) { // 定义函数/方法 reverse_words
    int pos = 0;                                       // 把 0 存入 pos
    const char *p = s;                                 // 把 字符串; 写入 const char *p
    while (*p) {                                       // 循环，直到不满足「乘 节点」
        while (*p == ' ')
            p++; // 循环，直到不满足「乘 节点 等于 ' ') 节点 加一 ;」
        if (!*p)
            break;             // 若 取反 乘 节点) break;
        const char *start = p; // 把 节点; 写入 const char *start
        while (*p && *p != ' ')
            p++; // 循环，直到不满足「乘 节点 且 乘 节点 不等于 ' ') 节点 加一 ;」
        int len = (int)(p - start); // 把 (int)(节点 减 起点) 存入 长度
        for (int i = len - 1; i >= 0; i--)
            out[pos++] = start[i]; // 让 下标 i 从 长度 减 1 开始计数，下标 i 不低于 0 就继续
        while (*p == ' ')
            p++; // 循环，直到不满足「乘 节点 等于 ' ') 节点 加一 ;」
        if (*p)
            out[pos++] = ' '; // 若 乘 节点) out[pos 加一 ] 赋值为 ' ';
    }
    out[pos] = '\0'; // 把 '\0'; 写入 out[pos]
}
int main(void) {    // 程序入口：跑内嵌自测用例
    char out[8192]; // char out[8192];
    reverse_words("Let's take LeetCode contest", out);
    if (strcmp(out, "s'teL ekat edoCteeL tsetnoc") != 0) {
        printf("FAIL 1 %s\n", out);
        return 1;
    }
    reverse_words("God Ding", out); // reverse_words(「God Ding」, out);
    if (strcmp(out, "doG gniD") != 0) {
        printf("FAIL 2 %s\n", out);
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
