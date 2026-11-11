/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134378688 */
/* LeetCode 448. 找到所有数组中消失的数字 — C 版（方案1） */
#include <stdio.h>                                              // 引入头文件
static int find_disappeared(const int *n, int len, int out[]) { // 定义函数/方法 find_disappeared
    int v[4096];                                                // int 值[4096];
    for (int i = 0; i < len; i++)
        v[i] = n[i];                // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
    for (int i = 0; i < len; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
        int idx = v[i] < 0 ? -v[i] - 1
                           : v[i] - 1; // 把 值[下标 i] 小于 0 ? 减 值[下标 i] 减 1 : 值[下标 i] 减 1 存入 idx
        if (v[idx] > 0)
            v[idx] = -v[idx]; // 若 值[idx] 超过 0) 值[idx] 赋值为 减 值[idx];
    }
    int cnt = 0; // 把 0 存入 计数
    for (int i = 0; i < len; i++)
        if (v[i] > 0)
            out[cnt++] = i + 1; // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
    return cnt;                 // 返回 计数
}
int main(void) {      // 程序入口：跑内嵌自测用例
    int out[4096], n; // int out[4096], 元素个数;
    n = find_disappeared((int[]){4, 3, 2, 7, 8, 2, 3, 1}, 8, out);
    if (n != 2 || out[0] != 5 || out[1] != 6) {
        printf("FAIL 1\n");
        return 1;
    }
    n = find_disappeared((int[]){1, 1}, 2, out); // 把 find_disappeared((int[]){1,1}, 2, out); 写入 元素个数
    if (n != 1 || out[0] != 2) {
        printf("FAIL 2\n");
        return 1;
    } // 若 元素个数 不等于 1 或 out[0] 不等于 2) { 输出「FAIL 2 」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS