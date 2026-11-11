// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130846022
// LeetCode 151. 反转字符串中的单词 — C++ 版（方案3）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <sstream>   // 引入头文件
#include <string>    // 引入头文件
#include <vector>    // 引入头文件
static std::string
reverseWords(const std::string &s) { // static std::string reverseWords(const std::string 按位与 字符串) {
    std::istringstream iss(s);       // std::istringstream iss(字符串);
    std::vector<std::string> words; // std::vector 小于 std::string 超过 单词列表;
    std::string w;                  // std::string 权重;
    while (iss >> w)
        words.push_back(w); // 循环，直到不满足「iss 超过 超过 权重) 单词列表 追加 权重);」
    std::reverse(words.begin(), words.end()); // std::reverse(单词列表 迭代位置 , 单词列表.终点());
    std::string out;                          // std::string out;
    for (size_t i = 0; i < words.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 单词列表.大小() 就继续
        if (i)
            out += " ";  // 若 下标 i) out 累加 「 」;
        out += words[i]; // out累加 单词列表[下标 i]
    }
    return out; // 返回 out
}
int main() {
    assert(reverseWords("the sky is blue") == "blue is sky the");
    assert(reverseWords("  hello world  ") == "world hello");
    assert(reverseWords("a good   example") == "example good a");
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS