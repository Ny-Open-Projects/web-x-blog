/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134150438 */
/* 数据结构与算法之排序: 希尔排序 — C 版（方案3） */
#include <stdio.h>                       // 引入头文件
static void shell_sort(int v[], int n) { // 定义函数/方法 shell_sort
    for (int gap = n / 2; gap > 0; gap /= 2) { // 让 gap 从 元素个数 除以 2 开始计数，gap 超过 0 就继续
        for (int i = gap; i < n; i++) { // 让 下标 i 从 gap 开始计数，下标 i 小于 元素个数 就继续
            int key = v[i];             // 把 值[下标 i] 存入 key
            int j = i - gap;            // 把 下标 i 减 gap 存入 下标 j
            while (j >= 0 && v[j] > key) {
                v[j + gap] = v[j];
                j -= gap;
            }
            v[j + gap] = key; // 把 key; 写入 v[j + gap]
        }
    }
}
int main(void) {                   // 程序入口：跑内嵌自测用例
    int v1[] = {5, 2, 4, 6, 1, 3}; // 把 {5,2,4,6,1,3}; 写入 int v1[]
    shell_sort(v1, 6);             // shell_sort(v1, 6);
    for (int i = 0; i < 6; i++)
        if (v1[i] != i + 1) {
            printf("FAIL\n");
            return 1;
        } // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS