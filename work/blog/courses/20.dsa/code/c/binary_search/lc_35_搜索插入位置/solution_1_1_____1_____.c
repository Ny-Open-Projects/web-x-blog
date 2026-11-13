/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233077
 * LeetCode 35. 搜索插入位置 — C 版（方案1：二分查找） */
#include <stdio.h>                                      // 引入头文件
int search_insert(const int *nums, int n, int target) { // 定义函数/方法 search_insert
    int left = 0, right = n;                 // 把 0, 右边界 赋值为 元素个数 存入 左边界
    while (left < right) {                   // 循环，直到不满足「左边界 小于 右边界」
        int mid = left + (right - left) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2 存入 中点
        if (nums[mid] < target)
            left = mid + 1;
        else
            right = mid; // 若 数组[中点] 小于 目标值) 左边界 赋值为 中点 加 1; else 右边界 赋值为 中点;
    }
    return left; // 返回 左边界
}
int main(void) {                              // 程序入口：跑内嵌自测用例
    int a1[] = {1, 2, 3}, a[] = {1, 3, 5, 6}; // 把 {1, 2, 3}, 数组[] 赋值为 {1, 3, 5, 6}; 写入 int a1[]
    struct {
        const int *nums;
        int n;
        int t;
        int want;
    } cs[] = {
        {a1, 3, 1, 0}, {a, 4, 5, 2}, {a, 4, 2, 1}, {a, 4, 7, 4}, {a, 4, 0, 0},
    };
    for (int i = 0; i < 5; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 5 就继续
        if (search_insert(cs[i].nums, cs[i].n, cs[i].t) != cs[i].want) {
            printf("FAIL %d\n", i);
            return 1;
        }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
