// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案13：微型正则匹配 match/matchhere/matchstar）
#include <iostream> // 引入头文件
#include <string>   // 引入头文件

static bool matchhere(const std::string &re, const std::string &text);

static bool matchstar(char c, const std::string &re, const std::string &text) { // 定义函数/方法 matchstar
    size_t i = 0;                                                               // 把 0; 写入 size_t i
    while (true) { // 循环，直到不满足「true」
        if (matchhere(re, text.substr(i)))
            return true; // 若 matchhere(re, text 截取 下标 i))，直接返回 true
        if (i >= text.size())
            break; // 若 下标 i 不低于 text.大小()) break;
        if (text[i] != c && c != '.')
            break; // 若 text[下标 i] 不等于 字符 且 字符 不等于 '.') break;
        ++i;       // 加一 下标 i;
    }
    return false; // 返回 false
}

static bool matchhere(const std::string &re, const std::string &text) { // 定义函数/方法 matchhere
    if (re.empty())
        return true; // 若 re 是否为空，直接返回 true
    if (re.size() >= 2 && re[1] == '*')
        return matchstar(re[0], re.substr(2), text);
    if (re[0] == '$' && re.size() == 1)
        return text.empty(); // 若 re[0] 等于 '$' 且 re.大小() 等于 1，直接返回 text 是否为空
    if (!text.empty() && (re[0] == '.' || re[0] == text[0]))
        return matchhere(re.substr(1), text.substr(1));
    return false; // 返回 false
}

static bool match(const std::string &re, const std::string &text) { // 定义函数/方法 match
    if (!re.empty() && re[0] == '^')
        return matchhere(re.substr(1), text);
    size_t i = 0;  // 把 0; 写入 size_t i
    while (true) { // 循环，直到不满足「true」
        if (matchhere(re, text.substr(i)))
            return true; // 若 matchhere(re, text 截取 下标 i))，直接返回 true
        if (i >= text.size())
            break; // 若 下标 i 不低于 text.大小()) break;
        ++i;       // 加一 下标 i;
    }
    return false; // 返回 false
}

int main() { // 程序入口：跑内嵌自测用例
    if (!match("abc", "xxabcxx")) {
        std::cout << "m1 failed" << std::endl;
        return 1;
    }
    if (!match("a.c", "axc")) {
        std::cout << "m2 failed" << std::endl;
        return 1;
    }
    if (!match("a*", "aaaa")) {
        std::cout << "m3 failed" << std::endl;
        return 1;
    }
    if (match("^a", "ba")) {
        std::cout << "m4 failed" << std::endl;
        return 1;
    }
    if (!match("c$", "abc")) {
        std::cout << "m5 failed" << std::endl;
        return 1;
    }
    if (!match("a.*c", "aXYZc")) {
        std::cout << "m6 failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
