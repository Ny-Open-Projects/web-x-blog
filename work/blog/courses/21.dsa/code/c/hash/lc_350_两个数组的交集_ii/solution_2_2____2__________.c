/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145568435 */
/* LeetCode 350. 两个数组的交集 II — C 版（方案2） */
#include <stdio.h>                                                            // 引入头文件
static int intersect(const int *a, int na, const int *b, int nb, int out[]) { // 定义函数/方法 intersect
    int used[256] = {0};                                                      // 把 {0}; 写入 int used[256]
    int cnt = 0;                                                              // 把 0 存入 计数
    for (int i = 0; i < nb; i++) {     // 让 下标 i 从 0 开始计数，下标 i 小于 nb 就继续
        for (int k = 0; k < na; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 na 就继续
            if (!used[k] && a[k] == b[i]) {
                used[k] = 1;
                out[cnt++] = b[i];
                break;
            }
        }
    }
    return cnt; // 返回 计数
}
int main(void) {    // 程序入口：跑内嵌自测用例
    int out[64], n; // int out[64], 元素个数;
    n = intersect((int[]){1, 2, 2, 1}, 4, (int[]){2, 2}, 2, out);
    if (n != 2 || out[0] != 2 || out[1] != 2) {
        printf("FAIL 1\n");
        return 1;
    }
    n = intersect((int[]){4, 9, 5}, 3, (int[]){9, 4, 9, 8, 4}, 5, out);
    if (n != 2 || out[0] != 9 || out[1] != 4) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
