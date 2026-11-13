/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
 * LeetCode 107524703. 人鬼渡河问题 — C 版（方案1：安全判定谓词）
 */
#include <stdio.h> // 引入头文件

static int is_safe(int r, int g) { // 定义判定函数 is_safe
    return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

int main(void) {                              // 程序入口：跑内嵌自测用例
    int rs[5] = {3, 3, 2, 1, 0};              // 把 {3, 3, 2, 1, 0}; 写入 int rs[5]
    int gs[5] = {3, 1, 2, 3, 0};              // 把 {3, 1, 2, 3, 0}; 写入 int gs[5]
    int ws[5] = {1, 1, 1, 0, 1};              // 把 {1, 1, 1, 0, 1}; 写入 int ws[5]
    for (int i = 0; i < 5; i++) {             // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
        if (is_safe(rs[i], gs[i]) != ws[i]) { // 若 is_safe(rs[下标 i], gs[下标 i]) 不等于 ws[下标 i]
            printf("is_safe(%d,%d) failed\n", rs[i], gs[i]); // 打印输出
            return 1;                                        // 返回 1
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
