/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145012016 */
/* LeetCode 496. 下一个更大元素 I — C 版（方案1） */
#include <stdio.h> // 引入头文件
static int next_greater_element(const int *n1, int l1, const int *n2, int l2,
                                int out[]) { // 定义函数/方法 next_greater_element
    int next[65536];                         // int 下一个[65536];
    for (int i = 0; i < 65536; i++)
        next[i] = -1;              // 让 下标 i 从 0 开始计数，下标 i 小于 65536 就继续
    int st[8192], top = 0;         // 把 0; 写入 int st[8192], top
    for (int i = 0; i < l2; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 l2 就继续
        while (top > 0 &&
               st[top - 1] < n2[i]) { // 循环，直到不满足「top 超过 0 且 st[top 减 1] 小于 n2[下标 i]」
            next[st[top - 1] + 32768] = n2[i]; // 把 n2[下标 i]; 写入 next[st[top - 1] + 32768]
            top--;                             // top 减一
        }
        st[top++] = n2[i]; // 把 n2[下标 i]; 写入 st[top++]
    }
    for (int i = 0; i < l1; i++)
        out[i] = next[n1[i] + 32768]; // 让 下标 i 从 0 开始计数，下标 i 小于 l1 就继续
    return l1;                        // 返回 l1
}
int main(void) { // 程序入口：跑内嵌自测用例
    int out[64]; // int out[64];
    next_greater_element((int[]){4, 1, 2}, 3, (int[]){1, 3, 4, 2}, 4, out);
    if (!(out[0] == -1 && out[1] == 3 && out[2] == -1)) {
        printf("FAIL 1\n");
        return 1;
    }
    next_greater_element((int[]){2, 4}, 2, (int[]){1, 2, 3, 4}, 4, out);
    if (!(out[0] == 3 && out[1] == -1)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS