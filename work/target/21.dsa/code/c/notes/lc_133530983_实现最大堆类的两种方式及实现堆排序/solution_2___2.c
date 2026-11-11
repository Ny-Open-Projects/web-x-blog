/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133530983 */
/* 数据结构与算法之堆: 实现最大堆类及堆排序 — C 版（方案2） */
#include <stdio.h>                  // 引入头文件
static void up_max(int *h, int i) { // 定义函数/方法 up_max
    while (i > 0) {                 // 循环，直到不满足「下标 i 超过 0」
        int p = (i - 1) / 2;        // 把 (下标 i 减 1) 除以 2 存入 节点
        if (h[p] >= h[i])
            break; // 若 h[节点] 不低于 h[下标 i]) break;
        int t = h[p];
        h[p] = h[i];
        h[i] = t; // 把 h[节点]; h[节点] 赋值为 h[下标 i]; h[下标 i] 赋值为 另一字符串 存入 另一字符串
        i = p;    // 把 节点; 写入 下标 i
    }
}
static void down_max(int *h, int n, int i) { // 定义函数/方法 down_max
    while (1) {                              // 循环，直到不满足「1」
        int l = 2 * i + 1, r = 2 * i + 2,
            m = i; // 把 2 乘 下标 i 加 1, 右指针 赋值为 2 乘 下标 i 加 2, 映射表 赋值为 下标 i 存入 左指针
        if (l < n && h[l] > h[m])
            m = l; // 若 左指针 小于 元素个数 且 h[左指针] 超过 h[映射表]) 映射表 赋值为 左指针;
        if (r < n && h[r] > h[m])
            m = r; // 若 右指针 小于 元素个数 且 h[右指针] 超过 h[映射表]) 映射表 赋值为 右指针;
        if (m == i)
            break; // 若 映射表 等于 下标 i) break;
        int t = h[i];
        h[i] = h[m];
        h[m] = t; // 把 h[下标 i]; h[下标 i] 赋值为 h[映射表]; h[映射表] 赋值为 另一字符串 存入 另一字符串
        i = m;    // 把 映射表; 写入 下标 i
    }
}
static void max_heap_pop_all(const int *in, int n, int out[]) { // 定义函数/方法 max_heap_pop_all
    int h[4096];                                                // int h[4096];
    int hn = 0;                                                 // 把 0 存入 hn
    for (int i = 0; i < n; i++) {
        h[hn++] = in[i];
        up_max(h, hn - 1);
    }                       // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    int on = 0;             // 把 0 存入 on
    while (hn > 0) {        // 循环，直到不满足「hn 超过 0」
        out[on++] = h[0];   // 把 h[0]; 写入 out[on++]
        int last = h[--hn]; // 把 h[ 减一 hn] 存入 last
        if (hn > 0) {
            h[0] = last;
            down_max(h, hn, 0);
        } // 若 hn 超过 0) { h[0] 赋值为 last; down_max(h, hn, 0); }
    }
}
int main(void) {                                         // 程序入口：跑内嵌自测用例
    int out[64];                                         // int out[64];
    max_heap_pop_all((int[]){3, 1, 6, 5, 2, 4}, 6, out); // max_heap_pop_all((int[]){3,1,6,5,2,4}, 6, out);
    for (int i = 0; i < 6; i++)
        if (out[i] != 6 - i) {
            printf("FAIL\n");
            return 1;
        } // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS