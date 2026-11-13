/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138684407 */
/* LeetCode 649. Dota2参议院 — C 版（方案1） */
#include <stdio.h>  // 引入头文件
#include <string.h> // 引入头文件
static const char *predict_party_victory(const char *senate) {
    int n = (int)strlen(senate);        // 把 (int)strlen(senate) 存入 元素个数
    int radiant[8192], dire[8192];      // int radiant[8192], dire[8192];
    int rn = 0, dn = 0, rh = 0, dh = 0; // 把 0, dn 赋值为 0, rh 赋值为 0, dh 赋值为 0 存入 rn
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        if (senate[i] == 'R')
            radiant[rn++] = i; // 若 senate[下标 i] 等于 'R') radiant[rn 加一 ] 赋值为 下标 i;
        else
            dire[dn++] = i; // 否则
    }
    while (rh < rn && dh < dn) { // 循环，直到不满足「rh 小于 rn 且 dh 小于 dn」
        int r = radiant[rh++];   // 把 radiant[rh 加一 ] 存入 右指针
        int d = dire[dh++];      // 把 dire[dh 加一 ] 存入 d
        if (r < d)
            radiant[rn++] = r + n; // 若 右指针 小于 d) radiant[rn 加一 ] 赋值为 右指针 加 元素个数;
        else
            dire[dn++] = d + n; // 否则
    }
    return rh >= rn ? "Dire" : "Radiant"; // 返回 rh 不低于 rn ? 「Dire」 : 「Dire」
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (strcmp(predict_party_victory("RD"), "Radiant") != 0) {
        printf("FAIL 1\n");
        return 1;
    }
    if (strcmp(predict_party_victory("DDR"), "Dire") != 0) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
