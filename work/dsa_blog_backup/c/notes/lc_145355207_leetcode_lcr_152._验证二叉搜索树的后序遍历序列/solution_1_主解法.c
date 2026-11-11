/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355207 */
/* LeetCode LCR 152. 验证二叉搜索树的后序遍历序列 — C 版（方案1） */
#include <stdio.h>                                 // 引入头文件
static int check(const int *seq, int lo, int hi) { // 定义判定函数 check
    if (hi - lo <= 1)
        return 1;       // 若 右边界 减 左边界 不超过 1，直接返回 1
    int root = seq[hi]; // 把 seq[右边界] 存入 根节点
    int i = lo;         // 把 左边界 存入 下标 i
    while (i < hi && seq[i] < root)
        i++; // 循环，直到不满足「下标 i 小于 右边界 且 seq[下标 i] 小于 根节点) 下标 i 加一 ;」
    for (int j = i; j < hi; j++) { // 让 下标 j 从 下标 i 开始计数，下标 j 小于 右边界 就继续
        if (seq[j] < root)
            return 0; // 若 seq[下标 j] 小于 根节点，直接返回 0
    }
    return check(seq, lo, i - 1) &&
           check(seq, i, hi - 1); // 返回 check(seq, 左边界, 下标 i 减 1) 且 check(seq, 下标 i, 右边界 减 1)
}
static int verify_postorder(const int *seq, int n) { return check(seq, 0, n - 1); }
int main(void) { // 程序入口：跑内嵌自测用例
    if (verify_postorder((int[]){1, 6, 3, 2, 5}, 5)) {
        printf("FAIL 1\n");
        return 1;
    }
    if (!verify_postorder((int[]){1, 3, 2, 4, 5}, 5)) {
        printf("FAIL 2\n");
        return 1;
    }
    if (!verify_postorder((int[]){4, 6, 5, 9, 8, 7}, 6)) {
        printf("FAIL 3\n");
        return 1;
    }
    if (!verify_postorder((int[]){1, 2, 3}, 3)) {
        printf("FAIL 4\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS