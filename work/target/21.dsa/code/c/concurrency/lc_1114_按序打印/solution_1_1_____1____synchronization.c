/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760 */
/* LeetCode 1114. 按序打印 — C 版（方案1） */
#include <stdio.h>     // 引入头文件
#include <string.h>    // 引入头文件
int main(void) {       // 程序入口：跑内嵌自测用例
    char out[64] = ""; // 把 「」; 写入 char out[64]
    /* 按序调用（顺序执行即保证顺序） */
    strcat(out, "first");  // 打印输出
    strcat(out, "second"); // 打印输出
    strcat(out, "third");  // 打印输出
    if (strcmp(out, "firstsecondthird") != 0) {
        printf("FAIL\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS