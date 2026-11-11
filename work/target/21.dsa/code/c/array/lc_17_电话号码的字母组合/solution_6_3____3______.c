/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133596542 */
/* LeetCode 17. 电话号码的字母组合 — C 版（方案6） */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件
static const char *MAP[10] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
static int letter_combinations(const char *digits, char out[][8]) { // 定义函数/方法 letter_combinations
    int cnt = 1;                                                    // 把 1 存入 计数
    out[0][0] = '\0';                                               // 把 '\0'; 写入 out[0][0]
    for (const char *p = digits; *p; p++) { // 把 digits; 乘 节点; 节点 加一 ) { 写入 for (const char *p
        const char *letters = MAP[*p - '0']; // 把 MAP[ 乘 节点 减 '0']; 写入 const char *letters
        int newCnt = 0;                      // 把 0 存入 newCnt
        char tmp[256][8];                    // char 临时变量[256][8];
        for (int i = 0; i < cnt; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 计数 就继续
            for (const char *c = letters; *c;
                 c++) { // 把 letters; 乘 字符; 字符 加一 ) { 写入 for (const char *c
                snprintf(tmp[newCnt], 8, "%s%c", out[i], *c); // 打印输出
                newCnt++;                                     // newCnt 加一
            }
        }
        for (int i = 0; i < newCnt; i++)
            strcpy(out[i], tmp[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 newCnt 就继续
        cnt = newCnt;               // 把 newCnt; 写入 计数
    }
    return cnt; // 返回 计数
}
int main(void) {                            // 程序入口：跑内嵌自测用例
    char out[256][8];                       // char out[256][8];
    int n = letter_combinations("23", out); // 把 letter_combinations(「23」, out) 存入 元素个数
    if (n != 9 || strcmp(out[0], "ad") != 0 || strcmp(out[8], "cf") != 0) {
        printf("FAIL 1\n");
        return 1;
    }
    if (letter_combinations("", out) != 1) {
        printf("FAIL 2\n");
        return 1;
    } // 若 letter_combinations(「」, out) 不等于 1) { 输出「」); return 1; }
    if (letter_combinations("2", out) != 3) {
        printf("FAIL 3\n");
        return 1;
    } // 若 letter_combinations(「2」, out) 不等于 3) { 输出「2」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS