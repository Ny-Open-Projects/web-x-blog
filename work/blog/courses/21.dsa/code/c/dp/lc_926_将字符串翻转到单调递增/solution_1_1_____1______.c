/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130659442 */
/* LeetCode 926. 将字符串翻转到单调递增 — C 版（方案1） */
#include <stdio.h>                              // 引入头文件
#include <string.h>                             // 引入头文件
static int min_flips_mono_incr(const char *s) { // 定义函数/方法 min_flips_mono_incr
    int ones = 0, flips = 0;                    // 把 0, flips 赋值为 0 存入 ones
    for (const char *p = s; *p; p++) { // 把 字符串; 乘 节点; 节点 加一 ) { 写入 for (const char *p
        if (*p == '1')
            ones++;  // 若 乘 节点 等于 '1') ones 加一 ;
        else {       // 否则
            flips++; // flips 加一
            if (ones < flips)
                flips = ones; // 若 ones 小于 flips) flips 赋值为 ones;
        }
    }
    return flips; // 返回 flips
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (min_flips_mono_incr("00110") != 1) {
        printf("FAIL 1\n");
        return 1;
    }
    if (min_flips_mono_incr("010110") != 2) {
        printf("FAIL 2\n");
        return 1;
    }
    if (min_flips_mono_incr("00011000") != 2) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS