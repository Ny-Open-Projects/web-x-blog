/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134707891 */
/* LeetCode 66. 加一 — C 版（方案1） */
#include <stdio.h>                                      // 引入头文件
static int plus_one(const int *d, int len, int out[]) { // 定义函数/方法 plus_one
    int v[4096];                                        // int 值[4096];
    for (int i = 0; i < len; i++)
        v[i] = d[i];                     // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
    for (int i = len - 1; i >= 0; i--) { // 让 下标 i 从 长度 减 1 开始计数，下标 i 不低于 0 就继续
        if (v[i] < 9) {
            v[i]++;
            for (int j = 0; j < len; j++)
                out[j] = v[j];
            return len;
        }
        v[i] = 0; // 把 0; 写入 v[i]
    }
    out[0] = 1; // 把 1; 写入 out[0]
    for (int j = 0; j < len; j++)
        out[j + 1] = v[j]; // 让 下标 j 从 0 开始计数，下标 j 小于 长度 就继续
    return len + 1;        // 返回 长度 加 1
}
int main(void) {                            // 程序入口：跑内嵌自测用例
    int out[4096], n;                       // int out[4096], 元素个数;
    n = plus_one((int[]){1, 2, 3}, 3, out); // 把 plus_one((int[]){1,2,3}, 3, out); 写入 元素个数
    if (n != 3 || out[2] != 4) {
        printf("FAIL 1\n");
        return 1;
    } // 若 元素个数 不等于 3 或 out[2] 不等于 4) { 输出「FAIL 1 」); return 1; }
    n = plus_one((int[]){4, 3, 2, 1}, 4, out); // 把 plus_one((int[]){4,3,2,1}, 4, out); 写入 元素个数
    if (n != 4 || out[3] != 2) {
        printf("FAIL 2\n");
        return 1;
    } // 若 元素个数 不等于 4 或 out[3] 不等于 2) { 输出「FAIL 2 」); return 1; }
    n = plus_one((int[]){9}, 1, out); // 把 plus_one((int[]){9}, 1, out); 写入 元素个数
    if (n != 2 || out[0] != 1 || out[1] != 0) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS