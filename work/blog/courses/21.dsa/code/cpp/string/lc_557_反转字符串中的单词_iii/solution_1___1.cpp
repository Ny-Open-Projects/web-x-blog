// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975
// LeetCode 557. 反转字符串中的单词III — C++ 版（方案1）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <sstream>   // 引入头文件
#include <string>    // 引入头文件
#include <vector>    // 引入头文件
static std::string
reverseWords(const std::string &s) { // static std::string reverseWords(const std::string 按位与 字符串) {
    std::vector<std::string> words;       // std::vector 小于 std::string 超过 单词列表;
    std::istringstream iss(s);            // std::istringstream iss(字符串);
    std::string w;                        // std::string 权重;
    while (iss >> w) {                    // 循环，直到不满足「iss 超过 超过 权重」
        std::reverse(w.begin(), w.end()); // std::reverse(权重 迭代位置 , 权重.终点());
        words.push_back(w);               // 单词列表 追加 权重);
    }
    std::string out;                            // std::string out;
    for (size_t i = 0; i < words.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 单词列表.大小() 就继续
        if (i)
            out += " ";  // 若 下标 i) out 累加 「 」;
        out += words[i]; // out累加 单词列表[下标 i]
    }
    return out; // 返回 out
}
int main() { // 程序入口：跑内嵌自测用例
    assert(reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"); // 断言校验
    assert(reverseWords("God Ding") == "doG gniD");                                       // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
