// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
// LeetCode 65. 有效数字 — C++ 版
#include <cctype>   // 引入头文件
#include <iostream> // 引入头文件
#include <map>      // 引入头文件
#include <string>   // 引入头文件

// 方案6（确定有限状态自动机 DFA，其余字符 lowercase）
bool isNumber(const std::string &s) { // 定义判定函数 isNumber
    const std::map<int, std::map<std::string, int>> graph = {
        // 把 { 写入 const std::map<int, std::map<std::string, int>> graph
        {0, {{"blank", 0}, {"sign", 1}, {".", 2}, {"digit", 6}}},
        {1, {{"digit", 6}, {".", 2}}},
        {2, {{"digit", 3}}},
        {3, {{"digit", 3}, {"e", 4}}},
        {4, {{"digit", 5}, {"sign", 7}}},
        {5, {{"digit", 5}}},
        {6, {{"digit", 6}, {".", 3}, {"e", 4}}},
        {7, {{"digit", 5}}},
    };
    std::string t = s; // 把 字符串; 写入 std::string t
    // trim 首尾空白，等价于 TS 的 String.trim()
    size_t b = t.find_first_not_of(" \t\n\r\f\v"); // 把 另一字符串.find_first_not_of(「 」); 写入 size_t b
    size_t e = t.find_last_not_of(" \t\n\r\f\v"); // 把 另一字符串.find_last_not_of(「 」); 写入 size_t e
    t = (b == std::string::npos) ? "" : t.substr(b, e - b + 1);
    int state = 0;      // 把 0 存入 state
    for (char ch : t) { // for (char 字符 : 另一字符串) {
        std::string c;  // std::string 字符;
        if (std::isdigit(
                static_cast<unsigned char>(ch))) // 若 std::isdigit(static_cast 小于 unsigned char 超过 (字符
            c = "digit";                         // 把 「digit」; 写入 字符
        else if (ch == ' ')                      // 定义函数/方法 if
            c = "blank";                         // 把 「blank」; 写入 字符
        else if (ch == '+' || ch == '-')         // 定义函数/方法 if
            c = "sign";                          // 把 「sign」; 写入 字符
        else                                     // 否则
            c = std::string(1, static_cast<char>(std::tolower(static_cast<unsigned char>(
                                   ch)))); // std::tolower(static_cast 小于 unsigned char 超过 (字符))));
        const auto &row = graph.at(state); // 把 graph.at(state); 写入 const auto &row
        auto it = row.find(c);             // 把 row 查找 字符) 存入 it
        if (it == row.end())
            return false;   // 若 it 等于 row.终点()，直接返回 false
        state = it->second; // 把 it 减 超过 second; 写入 state
    }
    return state == 3 || state == 5 || state == 6; // 返回 state 等于 3 或 state 等于 5 或 state 等于 6
}

int main() {                                                      // 程序入口：跑内嵌自测用例
    if (isNumber("0") != true) {                                  // 若 isNumber(「0」) 不等于 true
        std::cout << "isNumber('0') should be true" << std::endl; // 打印输出
        return 1;                                                 // 返回 1
    }
    if (isNumber("abc") != false) { // 若 isNumber(「abc」) 不等于 false
        std::cout << "isNumber('abc') should be false" << std::endl; // 打印输出
        return 1;                                                    // 返回 1
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
