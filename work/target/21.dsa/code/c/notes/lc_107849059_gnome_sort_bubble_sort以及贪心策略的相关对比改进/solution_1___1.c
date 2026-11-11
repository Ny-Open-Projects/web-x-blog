// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107849059
// Gnome Sort（侏儒排序）+ Bubble Sort（冒泡排序）+ 贪心找零 对比
#include <stdio.h> // 引入头文件

static void gnome_sort(int *a, int n) { // 定义函数/方法 gnome_sort
    int i = 0;                          // 把 0 存入 下标 i
    while (i < n) {                     // 循环，直到不满足「下标 i 小于 元素个数」
        if (i == 0 || a[i] >= a[i - 1])
            i++; // 若 下标 i 等于 0 或 数组[下标 i] 不低于 数组[下标 i 减 1]) 下标 i 加一 ;
        else {
            int t = a[i - 1];
            a[i - 1] = a[i];
            a[i] = t;
            i--;
        } // 否则
    }
}

static void bubble_sort(int *a, int n) { // 定义函数/方法 bubble_sort
    int swapped = 1;                     // 把 1 存入 swapped
    while (swapped) {                    // 循环，直到不满足「swapped」
        swapped = 0;                     // 把 0; 写入 swapped
        for (int i = 0; i < n - 1; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 减 1 就继续
            if (a[i] > a[i + 1]) {
                int t = a[i];
                a[i] = a[i + 1];
                a[i + 1] = t;
                swapped = 1;
            }
        }
    }
}

static int coin_change(const int *coins, int n, int amount) { // 定义函数/方法 coin_change
    int cs[64];                                               // int cs[64];
    for (int i = 0; i < n; i++)
        cs[i] = coins[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (int i = 0; i < n - 1; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 减 1 就继续
        for (int j = 0; j < n - 1 - i;
             j++) // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 减 1 减 下标 i 就继续
            if (cs[j] < cs[j + 1]) {
                int t = cs[j];
                cs[j] = cs[j + 1];
                cs[j + 1] = t;
            }
    int remaining = amount, count = 0; // 把 目标金额, 计数 赋值为 0 存入 remaining
    for (int i = 0; i < n; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        while (remaining >= cs[i]) {
            remaining -= cs[i];
            count++;
        }
    return remaining == 0 ? count : -1; // 返回 remaining 等于 0 ? 计数 : 减 1
}

static int eq_arr(const int *x, const int *y, int n) { // 定义函数/方法 eq_arr
    for (int i = 0; i < n; i++)
        if (x[i] != y[i])
            return 0; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    return 1;         // 返回 1
}

int main(void) {             // 程序入口：跑内嵌自测用例
    int a[3] = {3, 2, 1};    // 把 {3, 2, 1}; 写入 int a[3]
    int want[3] = {1, 2, 3}; // 把 {1, 2, 3}; 写入 int want[3]
    gnome_sort(a, 3);        // gnome_sort(数组, 3);
    if (!eq_arr(a, want, 3)) {
        printf("g failed\n");
        return 1;
    }                     // 若 取反 eq_arr(数组, want, 3)) { 输出「g failed 」); return 1; }
    int b[3] = {3, 2, 1}; // 把 {3, 2, 1}; 写入 int b[3]
    bubble_sort(b, 3);    // bubble_sort(b, 3);
    if (!eq_arr(b, want, 3)) {
        printf("b failed\n");
        return 1;
    }                              // 若 取反 eq_arr(b, want, 3)) { 输出「b failed 」); return 1; }
    int coins[4] = {1, 5, 10, 25}; // 把 {1, 5, 10, 25}; 写入 int coins[4]
    if (coin_change(coins, 4, 63) != 6) {
        printf("c failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
