// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145398097
// LeetCode 2637. 有时间限制的Promise对象 — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <optional> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> promiseWithTimeLimit(const std::vector<std::optional<int>> &values, int t) {
    std::vector<int> out; // std::vector 小于 int 超过 out;
    for (auto &v : values)
        out.push_back(v.has_value() ? *v : -1); // 逐个取出 values 的元素（值）
    return out;                                 // 返回 out
}
int main() { // 程序入口：跑内嵌自测用例
    assert((promiseWithTimeLimit({5, std::nullopt, 9}, 50) == std::vector<int>{5, -1, 9})); // 断言校验
    assert((promiseWithTimeLimit({std::nullopt}, 100) == std::vector<int>{-1}));            // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS