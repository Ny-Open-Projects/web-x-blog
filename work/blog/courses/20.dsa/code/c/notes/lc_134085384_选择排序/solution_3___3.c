/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085384 */
/* 数据结构与算法之排序: 选择排序 — C 版（方案3） */
#include <stdio.h>                           // 引入头文件
static void selection_sort(int v[], int n) { // 定义函数/方法 selection_sort
    for (int i = 0; i < n - 1; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 减 1 就继续
        int m = i;                    // 把 下标 i 存入 映射表
        for (int j = i + 1; j < n; j++)
            if (v[j] < v[m])
                m = j; // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 元素个数 就继续
        int t = v[i];
        v[i] = v[m];
        v[m] = t; // 把 值[下标 i]; 值[下标 i] 赋值为 值[映射表]; 值[映射表] 赋值为 另一字符串 存入 另一字符串
    }
}
int main(void) {                // 程序入口：跑内嵌自测用例
    int v1[] = {5, 4, 3, 2, 1}; // 把 {5,4,3,2,1}; 写入 int v1[]
    selection_sort(v1, 5);      // selection_sort(v1, 5);
    for (int i = 0; i < 5; i++)
        if (v1[i] != i + 1) {
            printf("FAIL\n");
            return 1;
        } // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS