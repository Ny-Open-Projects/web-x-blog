/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133598918 */
/* LeetCode 2. 两数相加 — C 版（方案4） */
#include <stdio.h> // 引入头文件
static int add_two_numbers(const int *a, int na, const int *b, int nb,
                           int out[]) { // 定义函数/方法 add_two_numbers
    int i = 0, j = 0, carry = 0,
        n = 0; // 把 0, 下标 j 赋值为 0, carry 赋值为 0, 元素个数 赋值为 0 存入 下标 i
    while (i < na || j < nb || carry) { // 循环，直到不满足「下标 i 小于 na 或 下标 j 小于 nb 或 carry」
        int total = carry; // 把 carry 存入 总和
        if (i < na) {
            total += a[i++];
        } // 若 下标 i 小于 na) { 总和 累加 数组[下标 i 加一 ]; }
        if (j < nb) {
            total += b[j++];
        }                      // 若 下标 j 小于 nb) { 总和 累加 b[下标 j 加一 ]; }
        out[n++] = total % 10; // 把 总和 对…取模 10; 写入 out[n++]
        carry = total / 10;    // 把 总和 除以 10; 写入 carry
    }
    if (n == 0)
        out[n++] = 0; // 若 元素个数 等于 0) out[元素个数 加一 ] 赋值为 0;
    return n;         // 返回 元素个数
}
int main(void) {    // 程序入口：跑内嵌自测用例
    int out[64], n; // int out[64], 元素个数;
    int w1[] = {7, 0, 8}, w2[] = {0}, w3[] = {8, 9, 9, 9, 0, 0, 0, 1};
    n = add_two_numbers((int[]){2, 4, 3}, 3, (int[]){5, 6, 4}, 3, out);
    if (n != 3) {
        printf("FAIL n1\n");
        return 1;
    } // 若 元素个数 不等于 3) { 输出「FAIL n1 」); return 1; }
    for (int i = 0; i < 3; i++)
        if (out[i] != w1[i]) {
            printf("FAIL 1\n");
            return 1;
        } // 让 下标 i 从 0 开始计数，下标 i 小于 3 就继续
    n = add_two_numbers((int[]){0}, 1, (int[]){0}, 1, out);
    if (n != 1 || out[0] != 0) {
        printf("FAIL 2\n");
        return 1;
    } // 若 元素个数 不等于 1 或 out[0] 不等于 0) { 输出「FAIL 2 」); return 1; }
    n = add_two_numbers((int[]){9, 9, 9, 9, 9, 9, 9}, 7, (int[]){9, 9, 9, 9}, 4, out);
    if (n != 8) {
        printf("FAIL n3\n");
        return 1;
    } // 若 元素个数 不等于 8) { 输出「FAIL n3 」); return 1; }
    for (int i = 0; i < 8; i++)
        if (out[i] != w3[i]) {
            printf("FAIL 3\n");
            return 1;
        }             // 让 下标 i 从 0 开始计数，下标 i 小于 8 就继续
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
