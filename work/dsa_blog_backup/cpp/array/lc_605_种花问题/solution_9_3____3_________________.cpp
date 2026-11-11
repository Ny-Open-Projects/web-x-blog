// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134638462
// LeetCode 605. 种花问题 — C++ 版（方案9）
#include <cassert>                                         // 引入头文件
#include <iostream>                                        // 引入头文件
#include <vector>                                          // 引入头文件
static bool canPlaceFlowers(std::vector<int> bed, int n) { // 定义函数/方法 canPlaceFlowers
    int count = 0;                                         // 把 0 存入 计数
    for (size_t i = 0; i < bed.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 bed.大小() 就继续
        if (bed[i] == 0 && (i == 0 || bed[i - 1] == 0) && (i + 1 == bed.size() || bed[i + 1] == 0)) {
            bed[i] = 1; // 把 1; 写入 bed[i]
            ++count;    // 加一 计数;
        }
    }
    return count >= n; // 返回 计数 不低于 元素个数
}
int main() {
    assert(canPlaceFlowers({1, 0, 0, 0, 1}, 1));
    assert(!canPlaceFlowers({1, 0, 0, 0, 1}, 2));
    assert(canPlaceFlowers({0, 0, 1, 0, 0}, 1));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS