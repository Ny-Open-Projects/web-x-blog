/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792 */
/* 数据结构与算法之排序: 快速排序 — C 版（方案6） */
#include <stdio.h>                        // 引入头文件
static void qs(int v[], int lo, int hi) { // 定义函数/方法 qs
    if (lo >= hi)
        return;                        // 若 左边界 不低于 右边界) return;
    int pivot = v[lo + (hi - lo) / 2]; // 把 值[(左边界 加 右边界) 除以 2] 存入 pivot
    int i = lo, j = hi;                // 把 左边界, 下标 j 赋值为 右边界 存入 下标 i
    while (i <= j) {                   // 循环，直到不满足「下标 i 不超过 下标 j」
        while (v[i] < pivot)
            i++; // 循环，直到不满足「值[下标 i] 小于 pivot) 下标 i 加一 ;」
        while (v[j] > pivot)
            j--; // 循环，直到不满足「值[下标 j] 超过 pivot) 下标 j 减一 ;」
        if (i <= j) {
            int t = v[i];
            v[i] = v[j];
            v[j] = t;
            i++;
            j--;
        }
    }
    qs(v, lo, j); // qs(值, 左边界, 下标 j);
    qs(v, i, hi); // qs(值, 下标 i, 右边界);
}
int main(void) {                // 程序入口：跑内嵌自测用例
    int v1[] = {5, 4, 3, 2, 1}; // 把 {5,4,3,2,1}; 写入 int v1[]
    qs(v1, 0, 4);               // qs(v1, 0, 4);
    for (int i = 0; i < 5; i++)
        if (v1[i] != i + 1) {
            printf("FAIL 1\n");
            return 1;
        }                       // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
    int v2[] = {3, 1, 4, 1, 5}; // 把 {3,1,4,1,5}; 写入 int v2[]
    qs(v2, 0, 4);               // qs(v2, 0, 4);
    if (!(v2[0] == 1 && v2[1] == 1 && v2[4] == 5)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS