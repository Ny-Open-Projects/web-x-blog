/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023 */
/* 求直方图最大面积算法分析 — C 版（方案3） */
#include <stdio.h>                                    // 引入头文件
static int get_result(int n, const int *h, int len) { // 定义函数/方法 get_result
    int st[4096];                                     // int st[4096];
    int top = 0;                                      // 把 0 存入 top
    int best = 0;                                     // 把 0 存入 当前最优
    for (int i = 0; i <= len; i++) {  // 让 下标 i 从 0 开始计数，下标 i 不超过 长度 就继续
        int cur = i < len ? h[i] : 0; // 把 下标 i 小于 长度 ? h[下标 i] : 0 存入 当前值
        while (top > 0 &&
               h[st[top - 1]] >= cur) { // 循环，直到不满足「top 超过 0 且 h[st[top 减 1]] 不低于 当前值」
            int t = st[--top];                     // 把 st[ 减一 top] 存入 另一字符串
            int left = top > 0 ? st[top - 1] : -1; // 把 top 超过 0 ? st[top 减 1] : 减 1 存入 左边界
            int width = i - left - 1;              // 把 下标 i 减 左边界 减 1 存入 width
            int area = h[t] * width;               // 把 h[另一字符串] 乘 width 存入 area
            if (area > best)
                best = area; // 若 area 超过 当前最优) 当前最优 赋值为 area;
        }
        st[top++] = i; // 把 下标 i; 写入 st[top++]
    }
    return best; // 返回 当前最优
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (get_result(5, (int[]){0, 2, 3, 3, 3, 2, 0}, 7) != 10) {
        printf("FAIL 1\n");
        return 1;
    }
    if (get_result(6, (int[]){0, 2, 1, 5, 6, 2, 3, 0}, 8) != 10) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS