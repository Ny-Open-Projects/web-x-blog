// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
// LeetCode 65. 有效数字 — C++ 版
#include <cctype>   // 引入头文件
#include <iostream> // 引入头文件
#include <string>   // 引入头文件

// 方案1（线性扫描）
bool isNumber(const std::string &s) { // 定义判定函数 isNumber
    std::string t = s;                // 把 字符串; 写入 std::string t
    // trim 首尾空白，等价于 TS 的 String.trim()
    size_t b = t.find_first_not_of(" \t\n\r\f\v"); // 把 另一字符串.find_first_not_of(「 」); 写入 size_t b
    size_t e = t.find_last_not_of(" \t\n\r\f\v"); // 把 另一字符串.find_last_not_of(「 」); 写入 size_t e
    t = (b == std::string::npos) ? "" : t.substr(b, e - b + 1);
    if (t.empty())
        return false;      // 若 另一字符串 是否为空，直接返回 false
    bool hasDot = false;   // 把 false 存入 hasDot
    bool hasE = false;     // 把 false 存入 hasE
    bool hasDigit = false; // 把 false 存入 hasDigit
    for (size_t i = 0; i < t.size(); i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 另一字符串.大小() 就继续
        char c = t[i];                      // 把 另一字符串[下标 i]; 写入 char c
        if (c == '.') { // 若 字符 等于 '.'
            if (hasDot || hasE)
                return false;              // 若 hasDot 或 hasE，直接返回 false
            hasDot = true;                 // 把 true; 写入 hasDot
        } else if (c == 'e' || c == 'E') { // 否则，若 字符 等于 'e' 或 字符 等于 'E'
            if (hasE || !hasDigit)
                return false;              // 若 hasE 或 取反 hasDigit，直接返回 false
            hasE = true;                   // 把 true; 写入 hasE
            hasDigit = false;              // 把 false; 写入 hasDigit
        } else if (c == '+' || c == '-') { // 否则，若 字符 等于 ' 加 ' 或 字符 等于 ' 减 '
            if (i > 0 && t[i - 1] != 'e' && t[i - 1] != 'E')
                return false;
        } else if (std::isdigit(static_cast<unsigned char>(
                       c))) { // 否则，若 std::isdigit(static_cast 小于 unsigned char 超过 (字符
            hasDigit = true;  // 把 true; 写入 hasDigit
        } else {              // 否则
            return false;     // 返回 false
        }
    }
    return hasDigit; // 返回 hasDigit
}

int main() {                        // 程序入口：跑内嵌自测用例
    if (isNumber("abc") != false) { // 若 isNumber(「abc」) 不等于 false
        std::cout << "isNumber('abc') should be false" << std::endl; // 打印输出
        return 1;                                                    // 返回 1
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
