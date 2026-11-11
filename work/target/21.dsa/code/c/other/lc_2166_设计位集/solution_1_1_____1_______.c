/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145556343 */
/* LeetCode 2166. 设计位集 — C 版（方案1） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
#include <string.h> // 引入头文件
typedef struct {
    int n;
    unsigned *words;
    int ones;
    unsigned reverse;
} Bitset;
static Bitset *bs_new(int size) {       // static Bitset 乘 bs_new(int 大小) {
    Bitset *b = malloc(sizeof(Bitset)); // 把 malloc(sizeof(Bitset)); 写入 Bitset *b
    b->n = size;                        // 把 大小; 写入 b->n
    b->words = calloc((size + 31) / 32,
                      sizeof(unsigned)); // 把 calloc((大小 加 31) 除以 32, sizeof(unsigned)); 写入 b->words
    b->ones = 0;
    b->reverse = 0; // 把 0; b 减 超过 reverse 赋值为 0; 写入 b->ones
    return b;       // 返回 b
}
static unsigned bs_get(Bitset *b, int idx) { return ((b->words[idx >> 5] >> (idx & 31)) & 1u) ^ b->reverse; }
static void bs_fix(Bitset *b, int idx) {
    if (bs_get(b, idx) == 0) {
        b->words[idx >> 5] |= 1u << (idx & 31);
        b->ones++;
    }
}
static void bs_unfix(Bitset *b, int idx) {
    if (bs_get(b, idx) == 1) {
        b->words[idx >> 5] &= ~(1u << (idx & 31));
        b->ones--;
    }
}
static void bs_flip(Bitset *b) {
    b->reverse ^= 1;
    b->ones = b->n - b->ones;
}
static int bs_all(Bitset *b) { return b->ones == b->n; }
static int bs_one(Bitset *b) {
    return b->ones > 0;
} // static int bs_one(Bitset 乘 b) { return b 减 超过 ones 超过 0; }
static void bs_str(Bitset *b, char out[]) { // 定义函数/方法 bs_str
    for (int i = 0; i < b->n; i++)
        out[i] = '0' + bs_get(b, i); // 让 下标 i 从 0 开始计数，下标 i 小于 b 减 超过 元素个数 就继续
    out[b->n] = '\0';                // 把 '\0'; 写入 out[b->n]
}
int main(void) {           // 程序入口：跑内嵌自测用例
    Bitset *b = bs_new(5); // 把 bs_new(5); 写入 Bitset *b
    char s[64];            // char 字符串[64];
    bs_fix(b, 0);
    bs_fix(b, 3); // bs_fix(b, 0); bs_fix(b, 3);
    bs_str(b, s); // bs_str(b, 字符串);
    if (strcmp(s, "10010") != 0) {
        printf("FAIL s1 %s\n", s);
        return 1;
    } // 若 strcmp(字符串, 「10010」) 不等于 0) { 输出「10010」, 字符串); return 1; }
    if (b->ones != 2) {
        printf("FAIL c1\n");
        return 1;
    }             // 若 b 减 超过 ones 不等于 2) { 输出「FAIL c1 」); return 1; }
    bs_flip(b);   // bs_flip(b);
    bs_str(b, s); // bs_str(b, 字符串);
    if (strcmp(s, "01101") != 0) {
        printf("FAIL s2 %s\n", s);
        return 1;
    } // 若 strcmp(字符串, 「01101」) 不等于 0) { 输出「01101」, 字符串); return 1; }
    if (b->ones != 3) {
        printf("FAIL c2\n");
        return 1;
    }               // 若 b 减 超过 ones 不等于 3) { 输出「FAIL c2 」); return 1; }
    bs_unfix(b, 0); // bs_unfix(b, 0);
    bs_str(b, s);   // bs_str(b, 字符串);
    if (strcmp(s, "01101") != 0) {
        printf("FAIL s3 %s\n", s);
        return 1;
    } // 若 strcmp(字符串, 「01101」) 不等于 0) { 输出「01101」, 字符串); return 1; }
    if (bs_all(b) || !bs_one(b)) {
        printf("FAIL ao\n");
        return 1;
    } // 若 bs_all(b) 或 取反 bs_one(b)) { 输出「FAIL ao 」); return 1; }
    free(b->words);
    free(b);          // free(b 减 超过 单词列表); free(b);
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
