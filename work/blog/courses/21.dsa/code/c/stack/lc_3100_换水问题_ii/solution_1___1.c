/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116 */
/* LeetCode 3100. 换水问题 II — C 版（方案1） */
#include <stdio.h>                             // 引入头文件
static int max_bottles_drunk(int nb, int ne) { // 定义函数/方法 max_bottles_drunk
    int drunk = nb, empty = nb;                // 把 nb, empty 赋值为 nb 存入 drunk
    while (empty >= ne) {                      // 循环，直到不满足「empty 不低于 ne」
        empty -= ne;                           // empty累减 ne
        ne++;                                  // ne 加一
        drunk++;                               // drunk 加一
        empty++;                               // empty 加一
    }
    return drunk; // 返回 drunk
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (max_bottles_drunk(10, 3) != 13) {
        printf("FAIL 1\n");
        return 1;
    }
    if (max_bottles_drunk(1, 2) != 1) {
        printf("FAIL 2\n");
        return 1;
    } // 若 max_bottles_drunk(1, 2) 不等于 1) { 输出「FAIL 2 」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS