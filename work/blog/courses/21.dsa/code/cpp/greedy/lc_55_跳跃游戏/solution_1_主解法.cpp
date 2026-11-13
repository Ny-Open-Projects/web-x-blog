// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133844403
// LeetCode 55. 跳跃游戏 — C++ 版（方案1）
#include <cassert>                                  // 引入头文件
#include <iostream>                                 // 引入头文件
#include <vector>                                   // 引入头文件
static bool canJump(const std::vector<int> &nums) { // 定义函数/方法 canJump
    int maxReach = 0;                               // 把 0 存入 maxReach
    for (int i = 0; i < static_cast<int>(nums.size());
         ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 static_cast 小于 int 超过 (数组.大小()) 就继续
        if (i > maxReach)
            return false; // 若 下标 i 超过 maxReach，直接返回 false
        maxReach = std::max(maxReach,
                            i + nums[i]); // 把 std::取较大值 maxReach, 下标 i 加 数组[下标 i]); 写入 maxReach
    }
    return true; // 返回 true
}
int main() {                           // 程序入口：跑内嵌自测用例
    assert(canJump({2, 3, 1, 1, 4}));  // 断言校验
    assert(!canJump({3, 2, 1, 0, 4})); // 断言校验
    std::cout << "PASS" << std::endl;  // 全部用例通过，输出 PASS
    return 0;                          // 返回 0
}
