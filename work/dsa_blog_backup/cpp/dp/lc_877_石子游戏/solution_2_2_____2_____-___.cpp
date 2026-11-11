// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130709323
// LeetCode 877. 石子游戏 — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static bool stoneGame(const std::vector<int> &piles) {
    (void)piles;
    return true;
}
int main() {
    assert(stoneGame({5, 3, 4, 5}));
    assert(stoneGame({3, 7, 2, 3}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS