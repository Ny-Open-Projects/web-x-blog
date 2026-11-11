// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134055742
// LeetCode 283. 移动零 — C++ 版（方案1）
#include <cassert>                               // 引入头文件
#include <iostream>                              // 引入头文件
#include <vector>                                // 引入头文件
static void moveZeroes(std::vector<int> &nums) { // 定义函数/方法 moveZeroes
    size_t pos = 0;                              // 把 0; 写入 size_t pos
    for (size_t i = 0; i < nums.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
        if (nums[i] != 0) {
            std::swap(nums[pos], nums[i]);
            ++pos;
        } // 若 数组[下标 i] 不等于 0) { std::交换 数组[pos], 数组[下标 i]); 加一 pos; }
    }
}
int main() {                                         // 程序入口：跑内嵌自测用例
    std::vector<int> v = {0, 1, 0, 3, 12};           // 把 {0, 1, 0, 3, 12}; 写入 std::vector<int> v
    moveZeroes(v);                                   // moveZeroes(值);
    assert((v == std::vector<int>{1, 3, 12, 0, 0})); // 断言校验
    std::vector<int> v2 = {0};                       // 把 {0}; 写入 std::vector<int> v2
    moveZeroes(v2);                                  // moveZeroes(v2);
    assert((v2 == std::vector<int>{0}));             // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS