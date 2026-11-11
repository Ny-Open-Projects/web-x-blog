// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133911745
// LeetCode 45. 跳跃游戏II — C++ 版（方案1）
#include <cassert>                              // 引入头文件
#include <iostream>                             // 引入头文件
#include <vector>                               // 引入头文件
static int jump(const std::vector<int> &nums) { // 定义函数/方法 jump
    int position = static_cast<int>(nums.size()) - 1, steps = 0;
    while (position > 0) {                   // 循环，直到不满足「position 超过 0」
        for (int i = 0; i < position; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 position 就继续
            if (i + nums[i] >= position) {
                position = i;
                ++steps;
                break;
            }
        }
    }
    return steps; // 返回 steps
}
int main() {                            // 程序入口：跑内嵌自测用例
    assert(jump({2, 3, 1, 1, 4}) == 2); // 断言校验
    assert(jump({2, 3, 0, 1, 4}) == 2); // 断言校验
    assert(jump({1}) == 0);             // 断言校验
    std::cout << "PASS" << std::endl;   // 全部用例通过，输出 PASS
    return 0;                           // 返回 0
}
