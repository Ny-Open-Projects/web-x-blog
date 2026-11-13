/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145078849 */
/* LeetCode 341. 扁平化嵌套列表迭代器 — C 版（方案2） */
#include <stdio.h> // 引入头文件
/* 用 tagged union 模拟嵌套列表 */
typedef struct NI {
    int is_int;
    int int_val;
    struct NI **items;
    int n_items;
} NI;
static void flatten(NI *ni, int out[], int *cnt) { // 定义函数/方法 flatten
    if (ni->is_int) {
        out[(*cnt)++] = ni->int_val;
        return;
    }
    for (int i = 0; i < ni->n_items; i++)
        flatten(ni->items[i], out, cnt); // 让 下标 i 从 0 开始计数，下标 i 小于 ni 减 超过 n_items 就继续
}
int main(void) {                                     // 程序入口：跑内嵌自测用例
    NI i1 = {1, 1, NULL, 0};                         // 把 {1, 1, NULL, 0}; 写入 NI i1
    NI i2 = {1, 2, NULL, 0};                         // 把 {1, 2, NULL, 0}; 写入 NI i2
    NI i3 = {1, 3, NULL, 0};                         // 把 {1, 3, NULL, 0}; 写入 NI i3
    NI i4 = {1, 4, NULL, 0};                         // 把 {1, 4, NULL, 0}; 写入 NI i4
    NI inner2[2] = {i3, i4};                         // 把 {i3, i4}; 写入 NI inner2[2]
    NI l2 = {0, 0, (NI *[]){inner2, inner2 + 2}, 0}; /* 数组指针模拟 */
    /* 简化：直接构造嵌套 */
    NI *inner_items[] = {&i3, &i4};    // 把 { 按位与 i3, 按位与 i4}; 写入 NI *inner_items[]
    NI list2 = {0, 0, inner_items, 2}; // 把 {0, 0, inner_items, 2}; 写入 NI list2
    NI *top_items[] = {&i1, &i2, &list2}; // 把 { 按位与 i1, 按位与 i2, 按位与 list2}; 写入 NI *top_items[]
    NI top = {0, 0, top_items, 3}; // 把 {0, 0, top_items, 3}; 写入 NI top
    int out[64], cnt = 0;          // 把 0; 写入 int out[64], cnt
    flatten(&top, out, &cnt);      // flatten( 按位与 top, out, 按位与 计数);
    if (cnt != 4 || !(out[0] == 1 && out[1] == 2 && out[2] == 3 && out[3] == 4)) {
        printf("FAIL cnt=%d\n", cnt);
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS