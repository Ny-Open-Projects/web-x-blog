// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135003383
// LeetCode 164. 最大间距 — C++ 版（方案12）
#include <cassert>                                    // 引入头文件
#include <iostream>                                   // 引入头文件
#include <vector>                                     // 引入头文件
static int maximumGap(const std::vector<int> &nums) { // 定义函数/方法 maximumGap
    int n = static_cast<int>(nums.size()); // 把 static_cast 小于 int 超过 (数组.大小()) 存入 元素个数
    if (n < 2)
        return 0;                           // 若 元素个数 小于 2，直接返回 0
    int minVal = nums[0], maxVal = nums[0]; // 把 数组[0], maxVal 赋值为 数组[0] 存入 minVal
    for (int v : nums) {                    // for (int 值 : 数组) {
        minVal = std::min(minVal, v);       // 把 std::取较小值 minVal, 值); 写入 minVal
        maxVal = std::max(maxVal, v);       // 把 std::取较大值 maxVal, 值); 写入 maxVal
    }
    if (minVal == maxVal)
        return 0; // 若 minVal 等于 maxVal，直接返回 0
    int d = std::max(1, (maxVal - minVal) /
                            (n - 1)); // 把 std::取较大值 1, (maxVal 减 minVal) 除以 (元素个数 减 1)) 存入 d
    int bucketSize = (maxVal - minVal) / d + 1; // 把 (maxVal 减 minVal) 除以 d 加 1 存入 bucketSize
    std::vector<std::pair<int, int>> buckets(bucketSize, {-1, -1});
    for (int v : nums) {            // for (int 值 : 数组) {
        int idx = (v - minVal) / d; // 把 (值 减 minVal) 除以 d 存入 idx
        if (buckets[idx].first == -1)
            buckets[idx] = {v, v}; // 若 buckets[idx].first 等于 减 1) buckets[idx] 赋值为 {值, 值};
        else {                     // 否则
            buckets[idx].first = std::min(
                buckets[idx].first, v); // 把 std::取较小值 buckets[idx].first, 值); 写入 buckets[idx].first
            buckets[idx].second =
                std::max(buckets[idx].second,
                         v); // 把 std::取较大值 buckets[idx].second, 值); 写入 buckets[idx].second
        }
    }
    int ans = 0, prevMax = -1;       // 把 0, prevMax 赋值为 减 1 存入 答案
    for (auto &[lo, hi] : buckets) { // for (auto 按位与 [左边界, 右边界] : buckets) {
        if (lo == -1)
            continue; // 若 左边界 等于 减 1) continue;
        if (prevMax != -1)
            ans = std::max(
                ans,
                lo - prevMax); // 若 prevMax 不等于 减 1) 答案 赋值为 std::取较大值 答案, 左边界 减 prevMax);
        prevMax = hi; // 把 右边界; 写入 prevMax
    }
    return ans; // 返回 答案
}
int main() {                                      // 程序入口：跑内嵌自测用例
    assert(maximumGap({1, 2, 3}) == 1);           // 断言校验
    assert(maximumGap({3, 6, 9, 1}) == 3);        // 断言校验
    assert(maximumGap({10}) == 0);                // 断言校验
    assert(maximumGap({}) == 0);                  // 断言校验
    assert(maximumGap({1, 10000000}) == 9999999); // 断言校验
    std::cout << "PASS" << std::endl;             // 全部用例通过，输出 PASS
    return 0;                                     // 返回 0
}
