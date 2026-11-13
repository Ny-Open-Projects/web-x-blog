/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134053461 */
/* 数据结构与算法之排序: 侏儒排序 — C 版（方案1） */
#include <stdio.h>                       // 引入头文件
static void gnome_sort(int v[], int n) { // 定义函数/方法 gnome_sort
    int i = 0;                           // 把 0 存入 下标 i
    while (i < n) {                      // 循环，直到不满足「下标 i 小于 元素个数」
        if (i == 0 || v[i - 1] <= v[i])
            i++; // 若 下标 i 等于 0 或 值[下标 i 减 1] 不超过 值[下标 i]) 下标 i 加一 ;
        else {
            int t = v[i - 1];
            v[i - 1] = v[i];
            v[i] = t;
            i--;
        } // 否则
    }
}
int main(void) {                // 程序入口：跑内嵌自测用例
    int v1[] = {5, 4, 3, 2, 1}; // 把 {5,4,3,2,1}; 写入 int v1[]
    gnome_sort(v1, 5);          // gnome_sort(v1, 5);
    for (int i = 0; i < 5; i++)
        if (v1[i] != i + 1) {
            printf("FAIL\n");
            return 1;
        } // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS