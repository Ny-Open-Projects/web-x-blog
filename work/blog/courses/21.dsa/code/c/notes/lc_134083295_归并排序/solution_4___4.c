/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295 */
/* 数据结构与算法之排序: 归并排序 — C 版（方案4） */
#include <stdio.h>                        // 引入头文件
#include <stdlib.h>                       // 引入头文件
static void ms(int v[], int lo, int hi) { // 定义函数/方法 ms
    if (lo >= hi)
        return;                   // 若 左边界 不低于 右边界) return;
    int mid = lo + (hi - lo) / 2; // 把 (左边界 加 右边界) 除以 2 存入 中点
    ms(v, lo, mid);               // ms(值, 左边界, 中点);
    ms(v, mid + 1, hi);           // ms(值, 中点 加 1, 右边界);
    int tmp[4096];                // int 临时变量[4096];
    int i = lo, j = mid + 1, k = 0; // 把 左边界, 下标 j 赋值为 中点 加 1, 下标 k 赋值为 0 存入 下标 i
    while (i <= mid && j <= hi) { // 循环，直到不满足「下标 i 不超过 中点 且 下标 j 不超过 右边界」
        if (v[i] <= v[j])
            tmp[k++] =
                v[i++]; // 若 值[下标 i] 不超过 值[下标 j]) 临时变量[下标 k 加一 ] 赋值为 值[下标 i 加一 ];
        else
            tmp[k++] = v[j++]; // 否则
    }
    while (i <= mid)
        tmp[k++] =
            v[i++]; // 循环，直到不满足「下标 i 不超过 中点) 临时变量[下标 k 加一 ] 赋值为 值[下标 i 加一 ];」
    while (j <= hi)
        tmp[k++] = v[j++]; // 循环，直到不满足「下标 j 不超过 右边界) 临时变量[下标 k 加一 ] 赋值为 值[下标 j
                           // 加一 ];」
    for (int x = 0; x < k; x++)
        v[lo + x] = tmp[x]; // 让 x 从 0 开始计数，x 小于 下标 k 就继续
}
int main(void) {                // 程序入口：跑内嵌自测用例
    int v1[] = {5, 4, 3, 2, 1}; // 把 {5,4,3,2,1}; 写入 int v1[]
    ms(v1, 0, 4);               // ms(v1, 0, 4);
    for (int i = 0; i < 5; i++)
        if (v1[i] != i + 1) {
            printf("FAIL\n");
            return 1;
        } // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS