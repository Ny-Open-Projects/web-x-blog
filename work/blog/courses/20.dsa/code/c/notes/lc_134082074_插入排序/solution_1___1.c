/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134082074 */
/* 数据结构与算法之排序: 插入排序 — C 版（方案1） */
#include <stdio.h>                           // 引入头文件
static void insertion_sort(int v[], int n) { // 定义函数/方法 insertion_sort
    for (int i = 1; i < n; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
        int key = v[i];           // 把 值[下标 i] 存入 key
        int j = i - 1;            // 把 下标 i 减 1 存入 下标 j
        while (j >= 0 && v[j] > key) {
            v[j + 1] = v[j];
            j--;
        }
        v[j + 1] = key; // 把 key; 写入 v[j + 1]
    }
}
int main(void) {                // 程序入口：跑内嵌自测用例
    int v1[] = {5, 4, 3, 2, 1}; // 把 {5,4,3,2,1}; 写入 int v1[]
    insertion_sort(v1, 5);      // insertion_sort(v1, 5);
    for (int i = 0; i < 5; i++)
        if (v1[i] != i + 1) {
            printf("FAIL\n");
            return 1;
        } // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS