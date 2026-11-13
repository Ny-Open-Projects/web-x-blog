/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440 */
/* LeetCode 215. 数组中的第K个最大元素 — C 版（方案11） */
#include <stdio.h>                   // 引入头文件
static void heap_up(int *h, int i) { // 定义函数/方法 heap_up
    while (i > 1 && h[i] > h[i / 2]) {
        int t = h[i];
        h[i] = h[i / 2];
        h[i / 2] = t;
        i /= 2;
    }
}
static void heap_down(int *h, int n, int i) { // 定义函数/方法 heap_down
    while (1) {                               // 循环，直到不满足「1」
        int l = 2 * i, r = 2 * i + 1,
            m = i; // 把 2 乘 下标 i, 右指针 赋值为 2 乘 下标 i 加 1, 映射表 赋值为 下标 i 存入 左指针
        if (l <= n && h[l] > h[m])
            m = l; // 若 左指针 不超过 元素个数 且 h[左指针] 超过 h[映射表]) 映射表 赋值为 左指针;
        if (r <= n && h[r] > h[m])
            m = r; // 若 右指针 不超过 元素个数 且 h[右指针] 超过 h[映射表]) 映射表 赋值为 右指针;
        if (m == i)
            break; // 若 映射表 等于 下标 i) break;
        int t = h[i];
        h[i] = h[m];
        h[m] = t; // 把 h[下标 i]; h[下标 i] 赋值为 h[映射表]; h[映射表] 赋值为 另一字符串 存入 另一字符串
        i = m;    // 把 映射表; 写入 下标 i
    }
}
static int find_kth_largest(const int *nums, int n, int k) { // 定义函数/方法 find_kth_largest
    int h[4096];                                             // int h[4096];
    int hn = 0;                                              // 把 0 存入 hn
    for (int i = 0; i < n; i++) {
        h[++hn] = nums[i];
        heap_up(h, hn);
    } // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (int t = 0; t < k - 1; t++) { // 让 另一字符串 从 0 开始计数，另一字符串 小于 下标 k 减 1 就继续
        h[1] = h[hn]; // 把 h[hn]; 写入 h[1]
        hn--;         // hn 减一
        if (hn > 0)
            heap_down(h, hn, 1); // 若 hn 超过 0) heap_down(h, hn, 1);
    }
    return h[1]; // 返回 h[1]
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
