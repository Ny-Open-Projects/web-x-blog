/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107450699 */
/* 计算思维之谁做的好事 — C 版（方案2） */
#include <stdio.h>                     // 引入头文件
static char find_good_man(void) {      // 定义函数/方法 find_good_man
    char men[] = {'A', 'B', 'C', 'D'}; // 把 {'A', 'B', 'C', 'D'}; 写入 char men[]
    for (int i = 0; i < 4; i++) {      // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
        char m = men[i];               // 把 men[下标 i]; 写入 char m
        int t = 0;                     // 把 0 存入 另一字符串
        if (m != 'A')
            t++; // 若 映射表 不等于 'A') 另一字符串 加一 ;
        if (m == 'C')
            t++; // 若 映射表 等于 'C') 另一字符串 加一 ;
        if (m == 'D')
            t++; // 若 映射表 等于 'D') 另一字符串 加一 ;
        if (m != 'D')
            t++; // 若 映射表 不等于 'D') 另一字符串 加一 ;
        if (t == 3)
            return m; // 若 另一字符串 等于 3，直接返回 映射表
    }
    return '?'; // 返回 '?'
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (find_good_man() != 'C') {
        printf("FAIL\n");
        return 1;
    } // 若 find_good_man() 不等于 'C') { 输出「FAIL 」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS