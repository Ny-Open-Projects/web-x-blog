/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134221939
 * LeetCode 704. 二分查找 — C 版（方案1：经典二分查找，闭区间 [left, right]） */

#include <stdio.h> // 引入头文件

int search(const int *nums, int n, int target) { // 定义函数/方法 search
    int left = 0, right = n - 1;             // 把 0, 右边界 赋值为 元素个数 减 1 存入 左边界
    while (left <= right) {                  // 循环，直到不满足「左边界 不超过 右边界」
        int mid = left + (right - left) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2 存入 中点
        if (nums[mid] == target) {           // 若 数组[中点] 等于 目标值
            return mid;                      // 返回 中点
        } else if (nums[mid] < target) {     // 否则，若 数组[中点] 小于 目标值
            left = mid + 1;                  // 把 中点 加 1; 写入 左边界
        } else {                             // 否则
            right = mid - 1;                 // 把 中点 减 1; 写入 右边界
        }
    }
    return -1; // 返回 减 1
}

int main(void) {                     // 程序入口：跑内嵌自测用例
    int a1[] = {1, 2, 3};            // 把 {1, 2, 3}; 写入 int a1[]
    int a2[] = {-1, 0, 3, 5, 9, 12}; // 把 { 减 1, 0, 3, 5, 9, 12}; 写入 int a2[]
    if (search(a1, 3, 1) != 0) {
        printf("case 1 FAILED\n");
        return 1;
    } // 若 search(a1, 3, 1) 不等于 0) { 输出「case 1 FAILED 」); return 1; }
    if (search(a2, 6, 9) != 4) {
        printf("case 2 FAILED\n");
        return 1;
    } // 若 search(a2, 6, 9) 不等于 4) { 输出「case 2 FAILED 」); return 1; }
    if (search(a2, 6, 2) != -1) {
        printf("case 3 FAILED\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
