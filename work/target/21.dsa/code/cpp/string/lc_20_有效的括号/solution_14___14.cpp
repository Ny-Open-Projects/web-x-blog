// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133759617
// LeetCode 20. 有效的括号 — C++ 版（方案14）
#include <cassert>                          // 引入头文件
#include <iostream>                         // 引入头文件
#include <string>                           // 引入头文件
#include <vector>                           // 引入头文件
static bool isValid(const std::string &s) { // 定义判定函数 isValid
    std::vector<char> stack;                // std::vector 小于 char 超过 栈;
    for (char ch : s) {                     // for (char 字符 : 字符串) {
        if (ch == ')') {                    // 若 字符 等于 ')'
            if (stack.empty() || stack.back() != '(')
                return false;   // 若 栈 是否为空 或 栈.back() 不等于 '('，直接返回 false
            stack.pop_back();   // 弹出栈顶元素
        } else if (ch == ']') { // 否则，若 字符 等于 ']'
            if (stack.empty() || stack.back() != '[')
                return false;   // 若 栈 是否为空 或 栈.back() 不等于 '['，直接返回 false
            stack.pop_back();   // 弹出栈顶元素
        } else if (ch == '}') { // 否则，若 字符 等于 '}'
            if (stack.empty() || stack.back() != '{')
                return false;    // 若 栈 是否为空 或 栈.back() 不等于 '{'，直接返回 false
            stack.pop_back();    // 弹出栈顶元素
        } else {                 // 否则
            stack.push_back(ch); // 栈 追加 字符);
        }
    }
    return stack.empty(); // 返回 栈 是否为空
}
int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::string> tests = {"(", "()", "()[]{}", "(]", "([)]", "abc"};
    std::vector<bool> want = {false, true, true, false, false, false};
    for (size_t i = 0; i < tests.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 tests.大小() 就继续
        assert(isValid(tests[i]) == want[i]); // 断言校验
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
