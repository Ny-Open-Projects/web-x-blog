/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233483
 * LeetCode 153. 寻找旋转排序数组中的最小值 — C 版（方案1：二分查找） */

#include <stdio.h> // 引入头文件

int findMin(const int *nums, int n) { // 定义函数/方法 findMin
    int low = 0, high = n - 1;        // 把 0, high 赋值为 元素个数 减 1 存入 low
    while (low < high) {              // 循环，直到不满足「low 小于 high」
        int pivot = low + (high - low) / 2;
            /* 防溢出写法 */ // 把 low 加 (high 减 low) 除以 2; 除以 乘 防溢出写法 乘 除以 存入 pivot
        if (nums[pivot] < nums[high]) { // 若 数组[pivot] 小于 数组[high]
            high = pivot;               // 把 pivot; 写入 high
        } else {                        // 否则
            low = pivot + 1;            // 把 pivot 加 1; 写入 low
        }
    }
    return nums[low]; // 返回 数组[low]
}

int main(void) {                      // 程序入口：跑内嵌自测用例
    int a1[] = {1, 2, 3};             // 把 {1, 2, 3}; 写入 int a1[]
    int a2[] = {3, 4, 5, 1, 2};       // 把 {3, 4, 5, 1, 2}; 写入 int a2[]
    int a3[] = {4, 5, 6, 7, 0, 1, 2}; // 把 {4, 5, 6, 7, 0, 1, 2}; 写入 int a3[]
    int a4[] = {11, 13, 15, 17};      // 把 {11, 13, 15, 17}; 写入 int a4[]
    if (findMin(a1, 3) != 1) {
        printf("case 1 FAILED\n");
        return 1;
    } // 若 findMin(a1, 3) 不等于 1) { 输出「case 1 FAILED 」); return 1; }
    if (findMin(a2, 5) != 1) {
        printf("case 2 FAILED\n");
        return 1;
    } // 若 findMin(a2, 5) 不等于 1) { 输出「case 2 FAILED 」); return 1; }
    if (findMin(a3, 7) != 0) {
        printf("case 3 FAILED\n");
        return 1;
    } // 若 findMin(a3, 7) 不等于 0) { 输出「case 3 FAILED 」); return 1; }
    if (findMin(a4, 4) != 11) {
        printf("case 4 FAILED\n");
        return 1;
    }                 // 若 findMin(a4, 4) 不等于 11) { 输出「case 4 FAILED 」); return 1; }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
