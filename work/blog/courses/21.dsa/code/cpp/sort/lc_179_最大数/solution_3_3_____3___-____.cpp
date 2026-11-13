// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134577890
// LeetCode 179. 最大数 — C++ 版（方案3）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <string>    // 引入头文件
#include <vector>    // 引入头文件
static std::string largestNumber(const std::vector<int> &nums) {
    std::vector<std::string> strs; // std::vector 小于 std::string 超过 strs;
    for (int v : nums)
        strs.push_back(std::to_string(v)); // for (int 值 : 数组) strs 追加 std::to_string(值));
    std::sort(strs.begin(), strs.end(), [](const std::string &a, const std::string &b) {
        return a + b > b + a; // 返回 数组 加 b 超过 b 加 数组
    });                       // });
    if (strs[0] == "0")
        return "0";  // 若 strs[0] 等于 「0」，直接返回 「0」
    std::string res; // std::string 结果;
    for (auto &s : strs)
        res += s; // 逐个取出 strs 的元素（字符串）
    return res;   // 返回 结果
}
int main() {                                               // 程序入口：跑内嵌自测用例
    assert(largestNumber({10, 2}) == "210");               // 断言校验
    assert(largestNumber({3, 30, 34, 5, 9}) == "9534330"); // 断言校验
    assert(largestNumber({0, 0}) == "0");                  // 断言校验
    std::cout << "PASS" << std::endl;                      // 全部用例通过，输出 PASS
    return 0;                                              // 返回 0
}
