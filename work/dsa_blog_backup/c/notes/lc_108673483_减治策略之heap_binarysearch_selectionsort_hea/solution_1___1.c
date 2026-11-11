/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
 * LeetCode 108673483. 减治策略 — C 版（方案1：二分查找）
 */
#include <stdio.h> // 引入头文件

static int binary_search(const int *arr, int n, int target) { // 定义函数/方法 binary_search
    int left = 0, right = n - 1;             // 把 0, 右边界 赋值为 元素个数 减 1 存入 左边界
    while (left <= right) {                  // 循环，直到不满足「左边界 不超过 右边界」
        int mid = left + (right - left) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2 存入 中点
        if (arr[mid] == target)
            return mid; // 若 数组[中点] 等于 目标值，直接返回 中点
        if (arr[mid] < target)
            left = mid + 1; // 若 数组[中点] 小于 目标值) 左边界 赋值为 中点 加 1;
        else
            right = mid - 1; // 否则
    }
    return -1; // 返回 减 1
}

int main(void) {                // 程序入口：跑内嵌自测用例
    int a[5] = {1, 3, 5, 7, 9}; // 把 {1, 3, 5, 7, 9}; 写入 int a[5]
    if (binary_search(a, 5, 5) != 2) {
        printf("case 0 failed\n");
        return 1;
    }
    if (binary_search(a, 5, 4) != -1) {
        printf("case 1 failed\n");
        return 1;
    }
    if (binary_search(a, 0, 5) != -1) {
        printf("case 2 failed\n");
        return 1;
    }
    if (binary_search(a, 5, 1) != 0) {
        printf("case 3 failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
