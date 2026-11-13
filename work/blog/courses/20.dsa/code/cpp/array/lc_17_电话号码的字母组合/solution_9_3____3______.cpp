// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133596542
// LeetCode 17. 电话号码的字母组合 — C++ 版（方案9）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<std::string> letterCombinations(const std::string &digits) {
    if (digits.empty())
        return {}; // 若 digits 是否为空，直接返回 {}
    static const std::vector<std::string> map = {"",    "",    "abc",  "def", "ghi",
                                                 "jkl", "mno", "pqrs", "tuv", "wxyz"};
    std::vector<std::string> res{""};    // std::vector 小于 std::string 超过 结果{「」};
    for (char c : digits) {              // for (char 字符 : digits) {
        std::vector<std::string> next;   // std::vector 小于 std::string 超过 下一个;
        for (const auto &prefix : res) { // 逐个取出 结果 的元素（prefix）
            for (char lc : map[c - '0'])
                next.push_back(prefix + lc); // for (char lc : 映射表[字符 减 '0']) 下一个 追加 prefix 加 lc);
        }
        res = std::move(next); // 把 std::move(下一个); 写入 结果
    }
    return res; // 返回 结果
}
int main() { // 程序入口：跑内嵌自测用例
    assert((letterCombinations("23") ==
            std::vector<std::string>{"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"})); // 断言校验
    assert(letterCombinations("").empty());                                                   // 断言校验
    assert(letterCombinations("2").size() == 3);                                              // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS