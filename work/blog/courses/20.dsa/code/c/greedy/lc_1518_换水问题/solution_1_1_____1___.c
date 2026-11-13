/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116 */
/* LeetCode 1518. 换水问题 — C 版（方案1） */
#include <stdio.h>                                                // 引入头文件
static int num_water_bottles(int num_bottles, int num_exchange) { // 定义函数/方法 num_water_bottles
    int ans = num_bottles, empty = num_bottles; // 把 num_bottles, empty 赋值为 num_bottles 存入 答案
    while (empty >= num_exchange) {             // 循环，直到不满足「empty 不低于 num_exchange」
        int new_b = empty / num_exchange;       // 把 empty 除以 num_exchange 存入 new_b
        ans += new_b;                           // 答案累加 new_b
        empty = new_b + empty % num_exchange;   // 把 new_b 加 empty 对…取模 num_exchange; 写入 empty
    }
    return ans; // 返回 答案
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (num_water_bottles(9, 3) != 13) {
        printf("FAIL 1\n");
        return 1;
    }
    if (num_water_bottles(15, 4) != 19) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
