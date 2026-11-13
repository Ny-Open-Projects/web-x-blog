// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134378688
// LeetCode 448. 找到所有数组中消失的数字 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> findDisappearedNumbers(std::vector<int> nums) {
    for (size_t i = 0; i < nums.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
        int idx = std::abs(nums[i]) - 1; // 把 std::取绝对值 数组[下标 i]) 减 1 存入 idx
        if (nums[idx] > 0)
            nums[idx] = -nums[idx]; // 若 数组[idx] 超过 0) 数组[idx] 赋值为 减 数组[idx];
    }
    std::vector<int> out;                      // std::vector 小于 int 超过 out;
    for (size_t i = 0; i < nums.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
        if (nums[i] > 0)
            out.push_back(static_cast<int>(i) +
                          1); // 若 数组[下标 i] 超过 0) out 追加 static_cast 小于 int 超过 (下标 i) 加 1);
    }
    return out; // 返回 out
}
int main() {
    assert((findDisappearedNumbers({4, 3, 2, 7, 8, 2, 3, 1}) == std::vector<int>{5, 6}));
    assert((findDisappearedNumbers({1, 1}) == std::vector<int>{2}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS