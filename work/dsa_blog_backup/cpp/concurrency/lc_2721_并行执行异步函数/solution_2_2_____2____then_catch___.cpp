// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386399
// LeetCode 2721. 并行执行异步函数 — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> executeAll(const std::vector<int> &fns) { return fns; }
int main() {                                                      // 程序入口：跑内嵌自测用例
    assert((executeAll({1, 2, 3}) == std::vector<int>{1, 2, 3})); // 断言校验
    assert(executeAll({}).empty());                               // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS