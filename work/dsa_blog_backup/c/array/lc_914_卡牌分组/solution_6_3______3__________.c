/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134934324 */
/* LeetCode 914. 卡牌分组 — C 版（方案6） */
#include <stdio.h> // 引入头文件
static int gcd(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}
static int has_groups_size_x(const int *deck, int len) { // 定义函数/方法 has_groups_size_x
    int counts[65536] = {0};                             // 把 {0}; 写入 int counts[65536]
    for (int i = 0; i < len; i++)
        counts[deck[i] + 32768]++; // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
    int g = 0;                     // 把 0 存入 g
    for (int i = 0; i < 65536; i++)
        if (counts[i])
            g = gcd(g, counts[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 65536 就继续
    return g >= 2;                 // 返回 g 不低于 2
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (!has_groups_size_x((int[]){1, 2, 3, 4, 4, 3, 2, 1}, 8)) {
        printf("FAIL 1\n");
        return 1;
    }
    if (has_groups_size_x((int[]){1, 1, 1, 2, 2, 2, 3, 3}, 8)) {
        printf("FAIL 2\n");
        return 1;
    }
    if (has_groups_size_x((int[]){1}, 1)) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS