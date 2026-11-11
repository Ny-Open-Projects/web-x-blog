// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130726302
// LeetCode 150. 逆波兰表达式求值 — C++ 版（方案2）
#include <cassert>                                           // 引入头文件
#include <cstdlib>                                           // 引入头文件
#include <iostream>                                          // 引入头文件
#include <string>                                            // 引入头文件
#include <vector>                                            // 引入头文件
static int evalRPN(const std::vector<std::string> &tokens) { // 定义函数/方法 evalRPN
    std::vector<long long> st;                               // std::vector 小于 long long 超过 st;
    for (const auto &t : tokens) { // 逐个取出 tokens 的元素（另一字符串）
        if (t == "+" || t == "-" || t == "*" || t == "/") {
            long long b = st.back();
            st.pop_back(); // 把 st.back(); st 弹出 ) 存入 b
            long long a = st.back();
            st.pop_back(); // 把 st.back(); st 弹出 ) 存入 数组
            if (t == "+")
                st.push_back(a + b); // 若 另一字符串 等于 「 加 」) st 追加 数组 加 b);
            else if (t == "-")
                st.push_back(a - b); // 否则，若 另一字符串 等于 「 减 」) st 追加 数组 减 b);
            else if (t == "*")
                st.push_back(a * b); // 否则，若 另一字符串 等于 「 乘 」) st 追加 数组 乘 b);
            else
                st.push_back(a / b);     // 否则
        } else {                         // 否则
            st.push_back(std::stoll(t)); // st 追加 std::stoll(另一字符串));
        }
    }
    return static_cast<int>(st[0]); // 返回 static_cast 小于 int 超过 (st[0])
}
int main() {                                          // 程序入口：跑内嵌自测用例
    assert(evalRPN({"2", "1", "+", "3", "*"}) == 9);  // 断言校验
    assert(evalRPN({"4", "13", "5", "/", "+"}) == 6); // 断言校验
    assert(evalRPN({"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}) == 22); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS