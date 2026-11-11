/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130846022 */
/* LeetCode 151. 反转字符串中的单词 — C 版（方案3） */
#include <ctype.h>                                     // 引入头文件
#include <stdio.h>                                     // 引入头文件
#include <stdlib.h>                                    // 引入头文件
#include <string.h>                                    // 引入头文件
static void reverse_words(const char *s, char out[]) { // 定义函数/方法 reverse_words
    char *words[8192];                                 // char 乘 单词列表[8192];
    int wn = 0;                                        // 把 0 存入 wn
    const char *p = s;                                 // 把 字符串; 写入 const char *p
    while (*p) {                                       // 循环，直到不满足「乘 节点」
        while (*p && isspace((unsigned char)*p))
            p++; // 循环，直到不满足「乘 节点 且 isspace((unsigned char) 乘 节点)) 节点 加一 ;」
        if (!*p)
            break;             // 若 取反 乘 节点) break;
        const char *start = p; // 把 节点; 写入 const char *start
        while (*p && !isspace((unsigned char)*p))
            p++; // 循环，直到不满足「乘 节点 且 取反 isspace((unsigned char) 乘 节点)) 节点 加一 ;」
        size_t len = p - start;         // 把 节点 减 起点; 写入 size_t len
        words[wn] = malloc(len + 1);    // 把 malloc(长度 加 1); 写入 words[wn]
        strncpy(words[wn], start, len); // strncpy(单词列表[wn], 起点, 长度);
        words[wn][len] = '\0';          // 把 '\0'; 写入 words[wn][len]
        wn++;                           // wn 加一
    }
    int pos = 0;                        // 把 0 存入 pos
    for (int i = wn - 1; i >= 0; i--) { // 让 下标 i 从 wn 减 1 开始计数，下标 i 不低于 0 就继续
        if (pos > 0)
            out[pos++] = ' ';        // 若 pos 超过 0) out[pos 加一 ] 赋值为 ' ';
        strcpy(out + pos, words[i]); // strcpy(out 加 pos, 单词列表[下标 i]);
        pos += strlen(words[i]);     // pos累加 strlen(单词列表[下标 i])
        free(words[i]);              // free(单词列表[下标 i]);
    }
    out[pos] = '\0'; // 把 '\0'; 写入 out[pos]
}
int main(void) {                           // 程序入口：跑内嵌自测用例
    char out[8192];                        // char out[8192];
    reverse_words("the sky is blue", out); // reverse_words(「the sky is blue」, out);
    if (strcmp(out, "blue is sky the") != 0) {
        printf("FAIL 1\n");
        return 1;
    }
    reverse_words("  hello world  ", out); // reverse_words(「 hello world 」, out);
    if (strcmp(out, "world hello") != 0) {
        printf("FAIL 2\n");
        return 1;
    }
    reverse_words("a good   example", out); // reverse_words(「数组 good example」, out);
    if (strcmp(out, "example good a") != 0) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS