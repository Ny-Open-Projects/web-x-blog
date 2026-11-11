/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237 */
/* 数据结构与算法之排序: 冒泡排序 — C 版（方案9） */
#include <stdio.h>                              // 引入头文件
static void gnome_sort_bubble(int v[], int n) { // 定义函数/方法 gnome_sort_bubble
    for (int i = 0; i < n; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        for (int j = 0; j < n - 1 - i;
             j++) // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 减 1 减 下标 i 就继续
            if (v[j] > v[j + 1]) {
                int t = v[j];
                v[j] = v[j + 1];
                v[j + 1] = t;
            }
}
static int check(const int *v, int n, const int *w) { // 定义判定函数 check
    for (int i = 0; i < n; i++)
        if (v[i] != w[i])
            return 0; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    return 1;         // 返回 1
}
int main(void) {                // 程序入口：跑内嵌自测用例
    int v1[] = {5, 4, 3, 2, 1}; // 把 {5,4,3,2,1}; 写入 int v1[]
    gnome_sort_bubble(v1, 5);   // gnome_sort_bubble(v1, 5);
    int w1[] = {1, 2, 3, 4, 5}; // 把 {1,2,3,4,5}; 写入 int w1[]
    if (!check(v1, 5, w1)) {
        printf("FAIL 1\n");
        return 1;
    }                         // 若 取反 check(v1, 5, w1)) { 输出「FAIL 1 」); return 1; }
    int v2[] = {3, 1, 2};     // 把 {3,1,2}; 写入 int v2[]
    gnome_sort_bubble(v2, 3); // gnome_sort_bubble(v2, 3);
    int w2[] = {1, 2, 3};     // 把 {1,2,3}; 写入 int w2[]
    if (!check(v2, 3, w2)) {
        printf("FAIL 2\n");
        return 1;
    } // 若 取反 check(v2, 3, w2)) { 输出「FAIL 2 」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS