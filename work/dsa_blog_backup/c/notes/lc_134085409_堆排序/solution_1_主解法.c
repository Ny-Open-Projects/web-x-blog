/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085409 */
/* 数据结构与算法之排序: 堆排序 — C 版（方案1） */
#include <stdio.h>                              // 引入头文件
static void sift(int v[], int start, int end) { // 定义函数/方法 sift
    int root = start;                           // 把 起点 存入 根节点
    while (1) {                                 // 循环，直到不满足「1」
        int child = 2 * root + 1;               // 把 2 乘 根节点 加 1 存入 子节点
        if (child > end)
            break;       // 若 子节点 超过 终点) break;
        int swap = root; // 把 根节点 存入 swap
        if (v[swap] < v[child])
            swap = child; // 若 值[swap] 小于 值[子节点]) swap 赋值为 子节点;
        if (child + 1 <= end && v[swap] < v[child + 1])
            swap = child +
                   1; // 若 子节点 加 1 不超过 终点 且 值[swap] 小于 值[子节点 加 1]) swap 赋值为 子节点 加 1;
        if (swap == root)
            break; // 若 swap 等于 根节点) break;
        int t = v[root];
        v[root] = v[swap];
        v[swap] = t; // 把 值[根节点]; 值[根节点] 赋值为 值[swap]; 值[swap] 赋值为 另一字符串 存入 另一字符串
        root = swap; // 把 swap; 写入 根节点
    }
}
static void heap_sort(int v[], int n) { // 定义函数/方法 heap_sort
    for (int i = n / 2 - 1; i >= 0; i--)
        sift(v, i, n - 1); // 让 下标 i 从 元素个数 除以 2 减 1 开始计数，下标 i 不低于 0 就继续
    for (int end = n - 1; end >= 1; end--) { // 让 终点 从 元素个数 减 1 开始计数，终点 不低于 1 就继续
        int t = v[0];
        v[0] = v[end];
        v[end] = t; // 把 值[0]; 值[0] 赋值为 值[终点]; 值[终点] 赋值为 另一字符串 存入 另一字符串
        sift(v, 0, end - 1); // sift(值, 0, 终点 减 1);
    }
}
int main(void) {                   // 程序入口：跑内嵌自测用例
    int v1[] = {5, 2, 4, 6, 1, 3}; // 把 {5,2,4,6,1,3}; 写入 int v1[]
    heap_sort(v1, 6);              // heap_sort(v1, 6);
    for (int i = 0; i < 6; i++)
        if (v1[i] != i + 1) {
            printf("FAIL\n");
            return 1;
        } // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS