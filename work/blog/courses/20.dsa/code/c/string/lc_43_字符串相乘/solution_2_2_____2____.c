/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130701795 */
/* LeetCode 43. 字符串相乘 — C 版（方案2） */
#include <stdio.h>                                                     // 引入头文件
#include <string.h>                                                    // 引入头文件
static void multiply(const char *num1, const char *num2, char out[]) { // 定义函数/方法 multiply
    if (strcmp(num1, "0") == 0 || strcmp(num2, "0") == 0) {
        strcpy(out, "0");
        return;
    }
    int m = (int)strlen(num1),
        n = (int)strlen(num2); // 把 (int)strlen(num1), 元素个数 赋值为 (int)strlen(num2) 存入 映射表
    int result[512] = {0};     // 把 {0}; 写入 int result[512]
    for (int i = m - 1; i >= 0; i--) { // 让 下标 i 从 映射表 减 1 开始计数，下标 i 不低于 0 就继续
        for (int j = n - 1; j >= 0; j--) { // 让 下标 j 从 元素个数 减 1 开始计数，下标 j 不低于 0 就继续
            int mul = (num1[i] - '0') *
                      (num2[j] - '0'); // 把 (num1[下标 i] 减 '0') 乘 (num2[下标 j] 减 '0') 存入 mul
            int p1 = i + j, p2 = i + j + 1; // 把 下标 i 加 下标 j, p2 赋值为 下标 i 加 下标 j 加 1 存入 p1
            int total = mul + result[p2]; // 把 mul 加 结果[p2] 存入 总和
            result[p2] = total % 10;      // 把 总和 对…取模 10; 写入 result[p2]
            result[p1] += total / 10;     // result[p1]累加 总和 除以 10
        }
    }
    int pos = 0, started = 0; // 把 0, started 赋值为 0 存入 pos
    for (int i = 0; i < m + n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 加 元素个数 就继续
        if (result[i] != 0 || started) {
            out[pos++] = '0' + result[i];
            started = 1;
        }
    }
    if (pos == 0)
        out[pos++] = '0'; // 若 pos 等于 0) out[pos 加一 ] 赋值为 '0';
    out[pos] = '\0';      // 把 '\0'; 写入 out[pos]
}
int main(void) {             // 程序入口：跑内嵌自测用例
    char out[1024];          // char out[1024];
    multiply("2", "3", out); // multiply(「2」, 「2」, out);
    if (strcmp(out, "6") != 0) {
        printf("FAIL 1\n");
        return 1;
    }                            // 若 strcmp(out, 「6」) 不等于 0) { 输出「6」); return 1; }
    multiply("123", "456", out); // multiply(「123」, 「123」, out);
    if (strcmp(out, "56088") != 0) {
        printf("FAIL 2\n");
        return 1;
    }                 // 若 strcmp(out, 「56088」) 不等于 0) { 输出「56088」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
