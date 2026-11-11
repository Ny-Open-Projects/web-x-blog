// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134893847
// LeetCode 905. 按奇偶排序数组 — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> sortArrayByParity(std::vector<int> nums) {
    size_t pos = 0;                            // 把 0; 写入 size_t pos
    for (size_t i = 0; i < nums.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
        if (nums[i] % 2 == 0)
            std::swap(nums[pos++],
                      nums[i]); // 若 数组[下标 i] 对…取模 2 等于 0) std::交换 数组[pos 加一 ], 数组[下标 i]);
    }
    return nums; // 返回 数组
}
int main() {                                   // 程序入口：跑内嵌自测用例
    auto g1 = sortArrayByParity({3, 1, 2, 4}); // 把 sortArrayByParity({3, 1, 2, 4}) 存入 g1
    assert(g1.size() == 4 && g1[0] % 2 == 0 && g1[1] % 2 == 0 && g1[2] % 2 == 1); // 断言校验
    auto g2 = sortArrayByParity({1, 2, 3});    // 把 sortArrayByParity({1, 2, 3}) 存入 g2
    assert((g2 == std::vector<int>{2, 1, 3})); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS