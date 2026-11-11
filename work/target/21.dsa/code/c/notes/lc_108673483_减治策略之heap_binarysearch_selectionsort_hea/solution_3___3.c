/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
 * LeetCode 108673483. 减治策略 — C 版（方案3：Boyer-Moore 摩尔投票求多数元素）
 */
#include <stdio.h> // 引入头文件

static int majority_element(const int *arr, int n) { // 定义函数/方法 majority_element
    int candidate = 0;                               // 把 0 存入 candidate
    int count = 0;                                   // 把 0 存入 计数
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        if (count == 0)
            candidate = arr[i]; // 若 计数 等于 0) candidate 赋值为 数组[下标 i];
        if (arr[i] == candidate)
            count++; // 若 数组[下标 i] 等于 candidate) 计数 加一 ;
        else
            count--; // 否则
    }
    int cnt = 0; // 把 0 存入 计数
    for (int i = 0; i < n; i++)
        if (arr[i] == candidate)
            cnt++; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    if (cnt > n / 2)
        return candidate; // 若 计数 超过 元素个数 除以 2，直接返回 candidate
    return -1;            // 返回 减 1
}

int main(void) {                       // 程序入口：跑内嵌自测用例
    int a0[7] = {2, 2, 1, 1, 1, 1, 1}; // 把 {2, 2, 1, 1, 1, 1, 1}; 写入 int a0[7]
    int a1[3] = {1, 2, 3};             // 把 {1, 2, 3}; 写入 int a1[3]
    int a2[3] = {3, 3, 4};             // 把 {3, 3, 4}; 写入 int a2[3]
    if (majority_element(a0, 7) != 1) {
        printf("case 0 failed\n");
        return 1;
    }
    if (majority_element(a1, 3) != -1) {
        printf("case 1 failed\n");
        return 1;
    }
    if (majority_element(a2, 3) != 3) {
        printf("case 2 failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
