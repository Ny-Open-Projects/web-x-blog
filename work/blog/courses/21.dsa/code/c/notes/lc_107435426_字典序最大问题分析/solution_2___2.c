/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107435426 */
/* 字典序最大问题分析 — C 版（方案2） */
#include <stdio.h>                                                 // 引入头文件
static void lexicographically_largest(int v[], int n, int out[]) { // 定义函数/方法 lexicographically_largest
    /* 降序排序取前 n */
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
            if (v[i] < v[j]) {
                int t = v[i];
                v[i] = v[j];
                v[j] = t;
            }
        }
    for (int i = 0; i < n; i++)
        out[i] = v[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
}
int main(void) {                           // 程序入口：跑内嵌自测用例
    int v1[] = {1, 2, 3};                  // 把 {1,2,3}; 写入 int v1[]
    int out[64];                           // int out[64];
    lexicographically_largest(v1, 3, out); // lexicographically_largest(v1, 3, out);
    if (!(out[0] == 3 && out[2] == 1)) {
        printf("FAIL 1\n");
        return 1;
    }
    int v2[] = {4, 2, 9, 7};               // 把 {4,2,9,7}; 写入 int v2[]
    lexicographically_largest(v2, 4, out); // lexicographically_largest(v2, 4, out);
    if (!(out[0] == 9 && out[3] == 2)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS