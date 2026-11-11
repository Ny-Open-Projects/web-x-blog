// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133807379
// LeetCode 209. 长度最小的子数组 — C++ 版（方案1）
#include <cassert>                                                    // 引入头文件
#include <iostream>                                                   // 引入头文件
#include <vector>                                                     // 引入头文件
static int minSubArrayLen(int target, const std::vector<int> &nums) { // 定义函数/方法 minSubArrayLen
    size_t l = 0;                                                     // 把 0; 写入 size_t l
    long long sum = 0;                                                // 把 0 存入 累计和
    int best = -1;                                                    // 把 减 1 存入 当前最优
    for (size_t r = 0; r < nums.size(); ++r) { // 让 右指针 从 0 开始计数，右指针 小于 数组.大小() 就继续
        sum += nums[r];                        // 累计和累加 数组[右指针]
        while (sum >= target) { // 循环，直到不满足「累计和 不低于 目标值」
            int len =
                static_cast<int>(r - l + 1); // 把 static_cast 小于 int 超过 (右指针 减 左指针 加 1) 存入 长度
            if (best == -1 || len < best)
                best = len; // 若 当前最优 等于 减 1 或 长度 小于 当前最优) 当前最优 赋值为 长度;
            sum -= nums[l++]; // 累计和累减 数组[左指针 加一 ]
        }
    }
    return best == -1 ? 0 : best; // 返回 当前最优 等于 减 1 ? 0 : 当前最优
}
int main() {
    assert(minSubArrayLen(7, {2, 3, 1, 2, 4, 3}) == 2);
    assert(minSubArrayLen(4, {1, 4, 4}) == 1);
    assert(minSubArrayLen(11, {1, 1, 1, 1, 1, 1, 1, 1}) == 0);
    assert(minSubArrayLen(1, {1, 2, 3}) == 1);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS