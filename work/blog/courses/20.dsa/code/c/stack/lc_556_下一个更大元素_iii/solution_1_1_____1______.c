/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397820 */
/* LeetCode 556. 下一个更大元素 III — C 版（方案1） */
#include <stdio.h>                       // 引入头文件
static int next_greater_element(int n) { // 定义函数/方法 next_greater_element
    int d[16];                           // int d[16];
    int m = 0;                           // 把 0 存入 映射表
    long x = n;                          // 把 元素个数; 写入 long x
    while (x > 0) {
        d[m++] = (int)(x % 10);
        x /= 10;
    }
    /* 反转为正序 */
    for (int i = 0, j = m - 1; i < j; i++, j--) {
        int t = d[i];
        d[i] = d[j];
        d[j] = t;
    } // 让 下标 i 从 0, 下标 j 赋值为 映射表 减 1 开始计数，下标 i 小于 下标 j 就继续
    int i = m - 2; // 把 映射表 减 2 存入 下标 i
    while (i >= 0 && d[i] >= d[i + 1])
        i--; // 循环，直到不满足「下标 i 不低于 0 且 d[下标 i] 不低于 d[下标 i 加 1]) 下标 i 减一 ;」
    if (i < 0)
        return -1; // 若 下标 i 小于 0，直接返回 减 1
    int j = m - 1; // 把 映射表 减 1 存入 下标 j
    while (d[j] <= d[i])
        j--; // 循环，直到不满足「d[下标 j] 不超过 d[下标 i]) 下标 j 减一 ;」
    int t = d[i];
    d[i] = d[j];
    d[j] = t; // 把 d[下标 i]; d[下标 i] 赋值为 d[下标 j]; d[下标 j] 赋值为 另一字符串 存入 另一字符串
    for (int l = i + 1, r = m - 1; l < r; l++, r--) {
        int t2 = d[l];
        d[l] = d[r];
        d[r] = t2;
    } // 让 左指针 从 下标 i 加 1, 右指针 赋值为 映射表 减 1 开始计数，左指针 小于 右指针 就继续
    long res = 0; // 把 0; 写入 long res
    for (int k = 0; k < m; k++)
        res = res * 10 + d[k]; // 让 下标 k 从 0 开始计数，下标 k 小于 映射表 就继续
    return res > 2147483647L ? -1 : (int)res; // 返回 结果 超过 2147483647L ? 减 1 : (int)结果
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (next_greater_element(12) != 21) {
        printf("FAIL 1\n");
        return 1;
    }
    if (next_greater_element(21) != -1) {
        printf("FAIL 2\n");
        return 1;
    }
    if (next_greater_element(1) != -1) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS