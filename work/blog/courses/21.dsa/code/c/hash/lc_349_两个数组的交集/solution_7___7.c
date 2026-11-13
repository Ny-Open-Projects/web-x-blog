/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135064368 */
/* LeetCode 349. 两个数组的交集 — C 版（方案7） */
#include <stdio.h>                                                               // 引入头文件
static int intersection(const int *a, int na, const int *b, int nb, int out[]) { // 定义函数/方法 intersection
    int cnt = 0;                                                                 // 把 0 存入 计数
    for (int i = 0; i < nb; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 nb 就继续
        int in_a = 0, dup = 0;     // 把 0, dup 赋值为 0 存入 in_a
        for (int k = 0; k < na; k++)
            if (a[k] == b[i]) {
                in_a = 1;
                break;
            } // 让 下标 k 从 0 开始计数，下标 k 小于 na 就继续
        if (!in_a)
            continue; // 若 取反 in_a) continue;
        for (int k = 0; k < cnt; k++)
            if (out[k] == b[i]) {
                dup = 1;
                break;
            } // 让 下标 k 从 0 开始计数，下标 k 小于 计数 就继续
        if (!dup)
            out[cnt++] = b[i]; // 若 取反 dup) out[计数 加一 ] 赋值为 b[下标 i];
    }
    return cnt; // 返回 计数
}
int main(void) {    // 程序入口：跑内嵌自测用例
    int out[64], n; // int out[64], 元素个数;
    n = intersection((int[]){1, 2, 2, 1}, 4, (int[]){2, 2}, 2, out);
    if (n != 1 || out[0] != 2) {
        printf("FAIL 1\n");
        return 1;
    } // 若 元素个数 不等于 1 或 out[0] 不等于 2) { 输出「FAIL 1 」); return 1; }
    n = intersection((int[]){4, 9, 5}, 3, (int[]){9, 4, 9, 8, 4}, 5, out);
    if (n != 2 || out[0] != 9 || out[1] != 4) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
