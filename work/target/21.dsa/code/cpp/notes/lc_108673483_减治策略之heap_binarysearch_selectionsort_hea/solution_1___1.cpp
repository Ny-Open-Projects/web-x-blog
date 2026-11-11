// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
// LeetCode 108673483. 减治策略 — C++ 版（方案1：二分查找）
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

static int binary_search(const std::vector<int> &arr, int target) { // 定义函数/方法 binary_search
    int left = 0, right = static_cast<int>(arr.size()) -
                          1; // 把 0, 右边界 赋值为 static_cast 小于 int 超过 (数组.大小()) 减 1 存入 左边界
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

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::vector<int>> as = {
        // 把 { 写入 std::vector<std::vector<int>> as
        {1, 3, 5, 7, 9},
        {1, 3, 5, 7, 9},
        {},
        {1, 3, 5, 7, 9},
    };
    int ts[4] = {5, 4, 5, 1};     // 把 {5, 4, 5, 1}; 写入 int ts[4]
    int ws[4] = {2, -1, -1, 0};   // 把 {2, 减 1, 减 1, 0}; 写入 int ws[4]
    for (int i = 0; i < 4; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
        int got = binary_search(as[i], ts[i]); // 把 binary_search(as[下标 i], ts[下标 i]) 存入 got
        if (got != ws[i]) {
            std::cout << "case " << i << " failed" << std::endl;
            return 1;
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
