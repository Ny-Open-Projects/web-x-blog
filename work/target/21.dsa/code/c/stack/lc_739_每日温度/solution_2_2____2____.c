/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233913 */
/* LeetCode 739. 每日温度 — C 版（方案2） */
#include <stdio.h>                                               // 引入头文件
static void daily_temperatures(const int *t, int n, int out[]) { // 定义函数/方法 daily_temperatures
    for (int i = 0; i < n; i++)
        out[i] = 0;               // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    int st[8192], top = 0;        // 把 0; 写入 int st[8192], top
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        while (
            top > 0 &&
            t[st[top - 1]] <
                t[i]) { // 循环，直到不满足「top 超过 0 且 另一字符串[st[top 减 1]] 小于 另一字符串[下标 i]」
            out[st[top - 1]] = i - st[top - 1]; // 把 下标 i 减 st[top 减 1]; 写入 out[st[top - 1]]
            top--;                              // top 减一
        }
        st[top++] = i; // 把 下标 i; 写入 st[top++]
    }
}
int main(void) {   // 程序入口：跑内嵌自测用例
    int out[8192]; // int out[8192];
    daily_temperatures((int[]){73, 74, 75, 71, 69, 72, 76, 73}, 8, out);
    if (!(out[0] == 1 && out[2] == 4 && out[7] == 0)) {
        printf("FAIL 1\n");
        return 1;
    }
    daily_temperatures((int[]){30, 40, 50, 60}, 4, out); // daily_temperatures((int[]){30,40,50,60}, 4, out);
    if (!(out[0] == 1 && out[3] == 0)) {
        printf("FAIL 2\n");
        return 1;
    }
    daily_temperatures((int[]){30, 60, 90}, 3, out); // daily_temperatures((int[]){30,60,90}, 3, out);
    if (!(out[0] == 1 && out[2] == 0)) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS