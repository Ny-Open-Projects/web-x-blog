/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133812752 */
/* LeetCode 234. 回文链表 — C 版（方案1） */
#include <stdio.h>                                   // 引入头文件
static int is_palindrome_list(const int *v, int n) { // 定义判定函数 is_palindrome_list
    int i = 0, j = n - 1; // 把 0, 下标 j 赋值为 元素个数 减 1 存入 下标 i
    while (i < j) {       // 循环，直到不满足「下标 i 小于 下标 j」
        if (v[i] != v[j])
            return 0; // 若 值[下标 i] 不等于 值[下标 j]，直接返回 0
        i++;
        j--; // 下标 i 加一 ; 下标 j 减一 ;
    }
    return 1; // 返回 1
}
int main(void) {                            // 程序入口：跑内嵌自测用例
    int v1[] = {1, 2, 2, 1}, v2[] = {1, 2}; // 把 {1,2,2,1}, v2[] 赋值为 {1,2}; 写入 int v1[]
    if (!is_palindrome_list(NULL, 0)) {
        printf("FAIL 0\n");
        return 1;
    }
    if (!is_palindrome_list(v1, 4)) {
        printf("FAIL 1\n");
        return 1;
    } // 若 取反 is_palindrome_list(v1, 4)) { 输出「FAIL 1 」); return 1; }
    if (is_palindrome_list(v2, 2)) {
        printf("FAIL 2\n");
        return 1;
    }                 // 若 is_palindrome_list(v2, 2)) { 输出「FAIL 2 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
