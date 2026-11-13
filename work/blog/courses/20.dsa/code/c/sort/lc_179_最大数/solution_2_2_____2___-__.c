/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134577890 */
/* LeetCode 179. 最大数 — C 版（方案2） */
#include <stdio.h>                                                          // 引入头文件
#include <stdlib.h>                                                         // 引入头文件
#include <string.h>                                                         // 引入头文件
static int cmp_str(const void *a, const void *b) {                          // 定义函数/方法 cmp_str
    char ab[64], ba[64];                                                    // char ab[64], ba[64];
    snprintf(ab, sizeof(ab), "%s%s", *(const char **)a, *(const char **)b); // 打印输出
    snprintf(ba, sizeof(ba), "%s%s", *(const char **)b, *(const char **)a); // 打印输出
    return strcmp(ba, ab);                                                  // 返回 strcmp(ba, ab)
}
static void largest_number(const int *nums, int n, char out[]) { // 定义函数/方法 largest_number
    char strs[64][16];                                           // char strs[64][16];
    const char *ptrs[64];                                        // const char 乘 ptrs[64];
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        snprintf(strs[i], sizeof(strs[i]), "%d", nums[i]); // 打印输出
        ptrs[i] = strs[i];                                 // 把 strs[下标 i]; 写入 ptrs[i]
    }
    qsort(ptrs, n, sizeof(char *), cmp_str); // qsort(ptrs, 元素个数, sizeof(char 乘 ), cmp_str);
    if (n > 0 && strcmp(ptrs[0], "0") == 0) {
        strcpy(out, "0");
        return;
    }
    out[0] = '\0'; // 把 '\0'; 写入 out[0]
    for (int i = 0; i < n; i++)
        strcat(out, ptrs[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
}
int main(void) {                            // 程序入口：跑内嵌自测用例
    char out[4096];                         // char out[4096];
    largest_number((int[]){10, 2}, 2, out); // largest_number((int[]){10,2}, 2, out);
    if (strcmp(out, "210") != 0) {
        printf("FAIL 1 %s\n", out);
        return 1;
    } // 若 strcmp(out, 「210」) 不等于 0) { 输出「210」, out); return 1; }
    largest_number((int[]){3, 30, 34, 5, 9}, 5, out); // largest_number((int[]){3,30,34,5,9}, 5, out);
    if (strcmp(out, "9534330") != 0) {
        printf("FAIL 2 %s\n", out);
        return 1;
    }
    largest_number((int[]){0, 0}, 2, out); // largest_number((int[]){0,0}, 2, out);
    if (strcmp(out, "0") != 0) {
        printf("FAIL 3 %s\n", out);
        return 1;
    }                 // 若 strcmp(out, 「0」) 不等于 0) { 输出「0」, out); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
