/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134893847 */
/* LeetCode 905. 按奇偶排序数组 — C 版（方案2） */
#include <stdio.h>                                   // 引入头文件
static void sort_array_by_parity(int n[], int len) { // 定义函数/方法 sort_array_by_parity
    int pos = 0;                                     // 把 0 存入 pos
    for (int i = 0; i < len; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
        if (n[i] % 2 == 0) {
            int t = n[pos];
            n[pos] = n[i];
            n[i] = t;
            pos++;
        }
    }
}
int main(void) {                 // 程序入口：跑内嵌自测用例
    int v1[] = {3, 1, 2, 4};     // 把 {3,1,2,4}; 写入 int v1[]
    sort_array_by_parity(v1, 4); // sort_array_by_parity(v1, 4);
    if (!(v1[0] % 2 == 0 && v1[1] % 2 == 0 && v1[2] % 2 == 1 && v1[3] % 2 == 1)) {
        printf("FAIL 1\n");
        return 1;
    }
    int v2[] = {1, 2, 3};        // 把 {1,2,3}; 写入 int v2[]
    sort_array_by_parity(v2, 3); // sort_array_by_parity(v2, 3);
    if (!(v2[0] == 2 && v2[1] == 1 && v2[2] == 3)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS