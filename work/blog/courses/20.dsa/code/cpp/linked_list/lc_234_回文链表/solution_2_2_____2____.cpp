// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133812752
// LeetCode 234. 回文链表 — C++ 版（方案2）
#include <cassert>                                        // 引入头文件
#include <iostream>                                       // 引入头文件
#include <vector>                                         // 引入头文件
static bool isPalindromeList(const std::vector<int> &v) { // 定义判定函数 isPalindromeList
    size_t i = 0, j = v.size(); // 把 0, 下标 j 赋值为 值.大小(); 写入 size_t i
    if (j == 0)
        return true; // 若 下标 j 等于 0，直接返回 true
    --j;             // 减一 下标 j;
    while (i < j) {  // 循环，直到不满足「下标 i 小于 下标 j」
        if (v[i] != v[j])
            return false; // 若 值[下标 i] 不等于 值[下标 j]，直接返回 false
        ++i;
        --j; // 加一 下标 i; 减一 下标 j;
    }
    return true; // 返回 true
}
int main() {                                // 程序入口：跑内嵌自测用例
    assert(isPalindromeList({}));           // 断言校验
    assert(isPalindromeList({1, 2, 2, 1})); // 断言校验
    assert(!isPalindromeList({1, 2}));      // 断言校验
    std::cout << "PASS" << std::endl;       // 全部用例通过，输出 PASS
    return 0;                               // 返回 0
}
