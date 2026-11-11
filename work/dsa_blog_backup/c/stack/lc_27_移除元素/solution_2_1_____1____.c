/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114689 */
/* LeetCode 27. 移除元素 — C 版（方案2） */
#include <stdio.h>                                     // 引入头文件
static int remove_element(int n[], int len, int val) { // 定义函数/方法 remove_element
    int k = 0;                                         // 把 0 存入 下标 k
    for (int i = 0; i < len; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
        if (n[i] != val)
            n[k++] = n[i]; // 若 元素个数[下标 i] 不等于 值) 元素个数[下标 k 加一 ] 赋值为 元素个数[下标 i];
    }
    return k; // 返回 下标 k
}
int main(void) {             // 程序入口：跑内嵌自测用例
    int v1[] = {3, 2, 2, 3}; // 把 {3,2,2,3}; 写入 int v1[]
    if (remove_element(v1, 4, 3) != 2) {
        printf("FAIL 1\n");
        return 1;
    }
    if (!(v1[0] == 2 && v1[1] == 2)) {
        printf("FAIL 1b\n");
        return 1;
    } // 若 取反 (v1[0] 等于 2 且 v1[1] 等于 2)) { 输出「FAIL 1b 」); return 1; }
    int v2[] = {0, 1, 2, 2, 3, 0, 4, 2}; // 把 {0,1,2,2,3,0,4,2}; 写入 int v2[]
    if (remove_element(v2, 8, 2) != 5) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS