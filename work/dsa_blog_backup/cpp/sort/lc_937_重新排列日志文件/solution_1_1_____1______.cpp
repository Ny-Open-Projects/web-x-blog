// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/139965098
// LeetCode 937. 重新排列日志文件 — C++ 版（方案1）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <string>    // 引入头文件
#include <vector>    // 引入头文件
static std::vector<std::string> reorderLogFiles(std::vector<std::string> logs) {
    auto isDigit = [](const std::string &s) {
        return !s.empty() && isdigit(static_cast<unsigned char>(s[0]));
    };
    std::vector<std::string> letter, digit; // std::vector 小于 std::string 超过 letter, digit;
    for (auto &log : logs) {                // 逐个取出 logs 的元素（log）
        auto idx = log.find(' ');           // 把 log 查找 ' ') 存入 idx
        auto content = log.substr(idx + 1); // 把 log 截取 idx 加 1) 存入 content
        if (isDigit(content))
            digit.push_back(std::move(log)); // 若 isDigit(content)) digit 追加 std::move(log));
        else
            letter.push_back(std::move(log)); // 否则
    }
    std::stable_sort(letter.begin(), letter.end(), [](const std::string &a, const std::string &b) {
        auto ca = a.substr(a.find(' ') + 1); // 把 数组 截取 数组 查找 ' ') 加 1) 存入 ca
        auto cb = b.substr(b.find(' ') + 1); // 把 b 截取 b 查找 ' ') 加 1) 存入 cb
        if (ca != cb)
            return ca < cb; // 若 ca 不等于 cb，直接返回 ca 小于 cb
        return a < b;       // 返回 数组 小于 b
    });                     // });
    letter.insert(letter.end(), digit.begin(),
                  digit.end()); // letter 插入 letter.终点(), digit 迭代位置 , digit.终点());
    return letter;              // 返回 letter
}
int main() { // 程序入口：跑内嵌自测用例
    auto got = reorderLogFiles({"a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"});
    assert((got == std::vector<std::string>{"g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1",
                                            "zo4 4 7"})); // 断言校验
    std::cout << "PASS" << std::endl;                     // 全部用例通过，输出 PASS
    return 0;                                             // 返回 0
}
