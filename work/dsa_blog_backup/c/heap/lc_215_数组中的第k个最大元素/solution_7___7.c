/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440 */
/* LeetCode 215. 数组中的第K个最大元素 — C 版（方案7） */
#include <stdio.h>                                     // 引入头文件
static void quickselect(int *a, int l, int r, int k) { // 定义函数/方法 quickselect
    if (l >= r)
        return;                     // 若 左指针 不低于 右指针) return;
    int i = l, j = r;               // 把 左指针, 下标 j 赋值为 右指针 存入 下标 i
    int pivot = a[l + (r - l) / 2]; // 把 数组[(左指针 加 右指针) 除以 2] 存入 pivot
    while (i <= j) {                // 循环，直到不满足「下标 i 不超过 下标 j」
        while (a[i] > pivot)
            i++; // 循环，直到不满足「数组[下标 i] 超过 pivot) 下标 i 加一 ;」
        while (a[j] < pivot)
            j--; // 循环，直到不满足「数组[下标 j] 小于 pivot) 下标 j 减一 ;」
        if (i <= j) {
            int t = a[i];
            a[i] = a[j];
            a[j] = t;
            i++;
            j--;
        }
    }
    if (k <= j + 1) {
        if (k - 1 <= j && l < j)
            quickselect(a, l, j, k);
        return;
    }
    if (k >= i + 1 && i < r)
        quickselect(a, i, r, k);
}
static int find_kth_largest(const int *nums, int n, int k) { // 定义函数/方法 find_kth_largest
    int a[4096];                                             // int 数组[4096];
    for (int i = 0; i < n; i++)
        a[i] = nums[i];          // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    quickselect(a, 0, n - 1, k); // quickselect(数组, 0, 元素个数 减 1, 下标 k);
    return a[k - 1];             // 返回 数组[下标 k 减 1]
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (find_kth_largest((int[]){3, 2, 1, 5, 6, 4}, 6, 2) != 5) {
        printf("FAIL 1\n");
        return 1;
    }
    if (find_kth_largest((int[]){3, 2, 3, 1, 2, 4, 5, 5, 6}, 9, 4) != 4) {
        printf("FAIL 2\n");
        return 1;
    }
    if (find_kth_largest((int[]){1}, 1, 1) != 1) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
