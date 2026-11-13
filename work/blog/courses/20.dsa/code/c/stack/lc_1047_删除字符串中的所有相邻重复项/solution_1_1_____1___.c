/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145295630 */
/* LeetCode 1047. 删除字符串中的所有相邻重复项 — C 版（方案1） */
#include <stdio.h>                                         // 引入头文件
#include <string.h>                                        // 引入头文件
static void remove_duplicates(const char *s, char out[]) { // 定义函数/方法 remove_duplicates
    int top = 0;                                           // 把 0 存入 top
    for (const char *p = s; *p; p++) { // 把 字符串; 乘 节点; 节点 加一 ) { 写入 for (const char *p
        if (top > 0 && out[top - 1] == *p)
            top--; // 若 top 超过 0 且 out[top 减 1] 等于 乘 节点) top 减一 ;
        else
            out[top++] = *p; // 否则
    }
    out[top] = '\0'; // 把 '\0'; 写入 out[top]
}
int main(void) {                      // 程序入口：跑内嵌自测用例
    char out[8192];                   // char out[8192];
    remove_duplicates("abbaca", out); // remove_duplicates(「abbaca」, out);
    if (strcmp(out, "ca") != 0) {
        printf("FAIL 1\n");
        return 1;
    }                                 // 若 strcmp(out, 「ca」) 不等于 0) { 输出「ca」); return 1; }
    remove_duplicates("azxxzy", out); // remove_duplicates(「azxxzy」, out);
    if (strcmp(out, "ay") != 0) {
        printf("FAIL 2\n");
        return 1;
    }                           // 若 strcmp(out, 「ay」) 不等于 0) { 输出「ay」); return 1; }
    remove_duplicates("", out); // remove_duplicates(「」, out);
    if (strcmp(out, "") != 0) {
        printf("FAIL 3\n");
        return 1;
    } // 若 strcmp(out, 「」) 不等于 0) { 输出「」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS