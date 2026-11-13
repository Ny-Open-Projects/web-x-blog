/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
 * LeetCode 107431726. 最大红矩形分析 — C 版（方案D：逐行高度 + 单调栈）
 */
#include <stdio.h> // 引入头文件

static long long max_red_rectangle(const char *matrix[], int n) {
    int m = 0; // 把 0 存入 映射表
    while (matrix[0][m])
        m++;                      // 循环，直到不满足「矩阵[0][映射表]) 映射表 加一 ;」
    long long ans = 0;            // 把 0 存入 答案
    long long height[64] = {0};   // 把 {0}; 写入 long long height[64]
    int stack[66];                // int 栈[66];
    for (int k = 0; k < n; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
        for (int i = 1; i <= m; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
            if (matrix[k][i - 1] == '.')
                height[i]++;
            else
                height[i] = 0;
        }
        int top = 0;                       // 把 0 存入 top
        stack[top++] = 0;                  // 把 0; 写入 stack[top++]
        for (int i = 1; i <= m + 1; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 加 1 就继续
            long long hi =
                (i <= m) ? height[i] : 0; // 把 (下标 i 不超过 映射表) ? height[下标 i] : 0 存入 右边界
            while (height[stack[top - 1]] > hi) { // 循环，直到不满足「height[栈[top 减 1]] 超过 右边界」
                long long now_h = height[stack[--top]];   // 把 height[栈[ 减一 top]] 存入 now_h
                long long width = i - stack[top - 1] - 1; // 把 下标 i 减 栈[top 减 1] 减 1 存入 width
                long long area = now_h * width;           // 把 now_h 乘 width 存入 area
                if (area > ans)
                    ans = area; // 若 area 超过 答案) 答案 赋值为 area;
            }
            stack[top++] = i; // 把 下标 i; 写入 stack[top++]
        }
    }
    return ans; // 返回 答案
}

int main(void) { // 程序入口：跑内嵌自测用例
    const char *matrix[] = {".....", "XXXXX", ".X...", "....."};
    if (max_red_rectangle(matrix, 4) != 6) {
        printf("mono failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
