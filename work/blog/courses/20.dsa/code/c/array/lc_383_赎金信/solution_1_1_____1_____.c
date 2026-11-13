/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134312127 */
/* LeetCode 383. 赎金信 — C 版（方案1） */
#include <stdio.h>                                       // 引入头文件
#include <string.h>                                      // 引入头文件
static int can_construct(const char *r, const char *m) { // 定义函数/方法 can_construct
    int cnt[26] = {0};                                   // 把 {0}; 写入 int cnt[26]
    for (const char *p = m; *p; p++)
        cnt[*p - 'a']++;
    for (const char *p = r; *p; p++) { // 把 右指针; 乘 节点; 节点 加一 ) { 写入 for (const char *p
        cnt[*p - 'a']--;               // 计数[ 乘 节点 减 '数组'] 减一 ;
        if (cnt[*p - 'a'] < 0)
            return 0; // 若 计数[ 乘 节点 减 '数组'] 小于 0，直接返回 0
    }
    return 1; // 返回 1
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (can_construct("a", "b")) {
        printf("FAIL 1\n");
        return 1;
    } // 若 can_construct(「数组」, 「数组」)) { 输出「数组」); return 1; }
    if (can_construct("aa", "ab")) {
        printf("FAIL 2\n");
        return 1;
    } // 若 can_construct(「aa」, 「aa」)) { 输出「aa」); return 1; }
    if (!can_construct("aa", "aab")) {
        printf("FAIL 3\n");
        return 1;
    } // 若 取反 can_construct(「aa」, 「aa」)) { 输出「aa」); return 1; }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS