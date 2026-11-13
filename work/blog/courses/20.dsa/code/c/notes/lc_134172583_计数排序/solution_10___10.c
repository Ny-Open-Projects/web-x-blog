/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583 */
/* 数据结构与算法之排序: 计数排序 — C 版（方案10） */
#include <stdio.h>                       // 引入头文件
static void count_sort(int v[], int n) { // 定义函数/方法 count_sort
    if (n == 0)
        return;               // 若 元素个数 等于 0) return;
    int mx = v[0], mn = v[0]; // 把 值[0], mn 赋值为 值[0] 存入 mx
    for (int i = 1; i < n; i++) {
        if (v[i] > mx)
            mx = v[i];
        if (v[i] < mn)
            mn = v[i];
    }                        // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
    int range = mx - mn + 1; // 把 mx 减 mn 加 1 存入 range
    int count[65536] = {0};  // 把 {0}; 写入 int count[65536]
    for (int i = 0; i < n; i++)
        count[v[i] - mn]++; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (int i = 1; i < range; i++)
        count[i] += count[i - 1]; // 让 下标 i 从 1 开始计数，下标 i 小于 range 就继续
    int output[4096];             // int 输出[4096];
    for (int i = n - 1; i >= 0; i--) { // 让 下标 i 从 元素个数 减 1 开始计数，下标 i 不低于 0 就继续
        output[count[v[i] - mn] - 1] = v[i]; // 把 值[下标 i]; 写入 output[count[v[i] - mn] - 1]
        count[v[i] - mn]--;                  // 计数[值[下标 i] 减 mn] 减一 ;
    }
    for (int i = 0; i < n; i++)
        v[i] = output[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
}
int main(void) {                // 程序入口：跑内嵌自测用例
    int v1[] = {5, 3, 8, 3, 1}; // 把 {5,3,8,3,1}; 写入 int v1[]
    count_sort(v1, 5);          // count_sort(v1, 5);
    int w1[] = {1, 3, 3, 5, 8}; // 把 {1,3,3,5,8}; 写入 int w1[]
    for (int i = 0; i < 5; i++)
        if (v1[i] != w1[i]) {
            printf("FAIL 1\n");
            return 1;
        } // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS