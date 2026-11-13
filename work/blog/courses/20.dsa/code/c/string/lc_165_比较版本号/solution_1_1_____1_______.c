/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135004886 */
/* LeetCode 165. 比较版本号 — C 版（方案1） */
#include <stdio.h>                              // 引入头文件
#include <stdlib.h>                             // 引入头文件
#include <string.h>                             // 引入头文件
static long parse_seg(const char *s, int len) { // 定义函数/方法 parse_seg
    char buf[32];                               // char buf[32];
    if (len >= 32)
        len = 31;         // 若 长度 不低于 32) 长度 赋值为 31;
    strncpy(buf, s, len); // strncpy(buf, 字符串, 长度);
    buf[len] = '\0';      // 把 '\0'; 写入 buf[len]
    return atol(buf);     // 返回 atol(buf)
}
static int compare_version(const char *v1, const char *v2) { // 定义函数/方法 compare_version
    const char *p1 = v1, *p2 = v2;            // 把 v1, 乘 p2 赋值为 v2; 写入 const char *p1
    while (*p1 || *p2) {                      // 循环，直到不满足「乘 p1 或 乘 p2」
        long a = 0, b = 0;                    // 把 0, b 赋值为 0; 写入 long a
        if (*p1) {                            // 若 乘 p1
            const char *d1 = strchr(p1, '.'); // 把 strchr(p1, '.'); 写入 const char *d1
            int len =
                d1 ? (int)(d1 - p1) : (int)strlen(p1); // 把 d1 ? (int)(d1 减 p1) : (int)strlen(p1) 存入 长度
            a = parse_seg(p1, len);                    // 把 parse_seg(p1, 长度); 写入 数组
            p1 = d1 ? d1 + 1 : p1 + strlen(p1);        // 把 d1 ? d1 加 1 : p1 加 strlen(p1); 写入 p1
        }
        if (*p2) {                            // 若 乘 p2
            const char *d2 = strchr(p2, '.'); // 把 strchr(p2, '.'); 写入 const char *d2
            int len =
                d2 ? (int)(d2 - p2) : (int)strlen(p2); // 把 d2 ? (int)(d2 减 p2) : (int)strlen(p2) 存入 长度
            b = parse_seg(p2, len);                    // 把 parse_seg(p2, 长度); 写入 b
            p2 = d2 ? d2 + 1 : p2 + strlen(p2);        // 把 d2 ? d2 加 1 : p2 加 strlen(p2); 写入 p2
        }
        if (a < b)
            return -1; // 若 数组 小于 b，直接返回 减 1
        if (a > b)
            return 1; // 若 数组 超过 b，直接返回 1
    }
    return 0; // 返回 0
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (compare_version("1.01", "1.001") != 0) {
        printf("FAIL 1\n");
        return 1;
    }
    if (compare_version("1.0", "1.0.0") != 0) {
        printf("FAIL 2\n");
        return 1;
    }
    if (compare_version("0.1", "1.1") != -1) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
