/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361 */
/* 数据结构与算法之排序: 桶排序 — C 版（方案2） */
#include <stdio.h>                                   // 引入头文件
static int get_index(const int *arr, int n, int k) { // 定义函数/方法 get_index
    for (int i = 0; i < n; i++)
        if (arr[i] == k)
            return k; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    return -1;        // 返回 减 1
}
int main(void) {         // 程序入口：跑内嵌自测用例
    int a[] = {1, 2, 3}; // 把 {1,2,3}; 写入 int a[]
    if (get_index(a, 3, 1) != 1) {
        printf("FAIL 1\n");
        return 1;
    } // 若 get_index(数组, 3, 1) 不等于 1) { 输出「FAIL 1 」); return 1; }
    if (get_index(a, 3, 3) != 3) {
        printf("FAIL 2\n");
        return 1;
    } // 若 get_index(数组, 3, 3) 不等于 3) { 输出「FAIL 2 」); return 1; }
    if (get_index(a, 3, 5) != -1) {
        printf("FAIL 3\n");
        return 1;
    } // 若 get_index(数组, 3, 5) 不等于 减 1) { 输出「FAIL 3 」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS