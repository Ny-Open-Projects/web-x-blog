// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134707891
// LeetCode 66. 加一 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> plusOne(std::vector<int> digits) {
    for (size_t i = digits.size(); i > 0; --i) { // 让 下标 i 从 digits.大小() 开始计数，下标 i 超过 0 就继续
        if (digits[i - 1] < 9) {
            ++digits[i - 1];
            return digits;
        }
        digits[i - 1] = 0; // 把 0; 写入 digits[i - 1]
    }
    digits.insert(digits.begin(), 1); // digits 插入 digits 迭代位置 , 1);
    return digits;                    // 返回 digits
}
int main() {
    assert((plusOne({1, 2, 3}) == std::vector<int>{1, 2, 4}));
    assert((plusOne({4, 3, 2, 1}) == std::vector<int>{4, 3, 2, 2}));
    assert((plusOne({9}) == std::vector<int>{1, 0}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS