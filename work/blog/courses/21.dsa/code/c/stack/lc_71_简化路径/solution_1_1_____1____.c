/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134368624 */
/* LeetCode 71. 简化路径 — C 版（方案1） */
#include <stdio.h>                                        // 引入头文件
#include <string.h>                                       // 引入头文件
static void simplify_path(const char *path, char out[]) { // 定义函数/方法 simplify_path
    char *parts[1024];                                    // char 乘 parts[1024];
    int pn = 0;                                           // 把 0 存入 pn
    char buf[8192];                                       // char buf[8192];
    strncpy(buf, path, sizeof(buf) - 1);                  // strncpy(buf, 当前路径, sizeof(buf) 减 1);
    buf[sizeof(buf) - 1] = '\0';                          // 把 '\0'; 写入 buf[sizeof(buf) - 1]
    char *tok = strtok(buf, "/");                         // 把 strtok(buf, 「 除以 」); 写入 char *tok
    while (tok) {                                         // 循环，直到不满足「tok」
        if (strcmp(tok, "..") == 0) {
            if (pn > 0)
                pn--;
        } // 若 strcmp(tok, 「..」) 等于 0) { if (pn 超过 0) pn 减一 ; }
        else if (strcmp(tok, ".") != 0)
            parts[pn++] = tok; // 否则，若 strcmp(tok, 「.」) 不等于 0) parts[pn 加一 ] 赋值为 tok;
        tok = strtok(NULL, "/"); // 把 strtok(NULL, 「 除以 」); 写入 tok
    }
    int pos = 0; // 把 0 存入 pos
    if (pn == 0) {
        out[pos++] = '/';
    } // 若 pn 等于 0) { out[pos 加一 ] 赋值为 ' 除以 '; }
    else
        for (int i = 0; i < pn; i++) {   // 否则
            out[pos++] = '/';            // 把 ' 除以 '; 写入 out[pos++]
            strcpy(out + pos, parts[i]); // strcpy(out 加 pos, parts[下标 i]);
            pos += strlen(parts[i]);     // pos累加 strlen(parts[下标 i])
        }
    out[pos] = '\0'; // 把 '\0'; 写入 out[pos]
}
int main(void) {                  // 程序入口：跑内嵌自测用例
    char out[8192];               // char out[8192];
    simplify_path("/home/", out); // simplify_path(「 除以 home 除以 」, out);
    if (strcmp(out, "/home") != 0) {
        printf("FAIL 1\n");
        return 1;
    }
    simplify_path("/../", out); // simplify_path(「 除以 .. 除以 」, out);
    if (strcmp(out, "/") != 0) {
        printf("FAIL 2\n");
        return 1;
    } // 若 strcmp(out, 「 除以 」) 不等于 0) { 输出「 除以 」); return 1; }
    simplify_path("/home//foo/", out); // simplify_path(" 除以 home
    if (strcmp(out, "/home/foo") != 0) {
        printf("FAIL 3\n");
        return 1;
    }
    simplify_path("/a/./b/../../c/", out);
    if (strcmp(out, "/c") != 0) {
        printf("FAIL 4\n");
        return 1;
    } // 若 strcmp(out, 「 除以 字符」) 不等于 0) { 输出「 除以 字符」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS