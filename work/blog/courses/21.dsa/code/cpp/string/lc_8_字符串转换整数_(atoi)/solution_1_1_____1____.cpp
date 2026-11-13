// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135129920
// LeetCode 8. 字符串转换整数 (atoi) — C++ 版（方案1）
#include <cassert>                        // 引入头文件
#include <cctype>                         // 引入头文件
#include <climits>                        // 引入头文件
#include <iostream>                       // 引入头文件
#include <string>                         // 引入头文件
static int myAtoi(const std::string &s) { // 定义函数/方法 myAtoi
    size_t i = 0, n = s.size();           // 把 0, 元素个数 赋值为 字符串.大小(); 写入 size_t i
    while (i < n && s[i] == ' ')
        ++i; // 循环，直到不满足「下标 i 小于 元素个数 且 字符串[下标 i] 等于 ' ') 加一 下标 i;」
    long long sign = 1; // 把 1 存入 sign
    if (i < n &&
        (s[i] == '+' ||
         s[i] ==
             '-')) { // 若 下标 i 小于 元素个数 且 (字符串[下标 i] 等于 ' 加 ' 或 字符串[下标 i] 等于 ' 减 '
        if (s[i] == '-')
            sign = -1; // 若 字符串[下标 i] 等于 ' 减 ') sign 赋值为 减 1;
        ++i;           // 加一 下标 i;
    }
    long long ans = 0; // 把 0 存入 答案
    while (i < n && std::isdigit(static_cast<unsigned char>(s[i]))) {
        ans = ans * 10 + (s[i] - '0'); // 把 答案 乘 10 加 (字符串[下标 i] 减 '0'); 写入 答案
        if (ans > 2147483648LL)
            ans = 2147483648LL; // 若 答案 超过 2147483648LL) 答案 赋值为 2147483648LL;
        ++i;                    // 加一 下标 i;
    }
    ans *= sign; // 把 sign; 写入 ans *
    if (ans > INT_MAX)
        return INT_MAX; // 若 答案 超过 INT_MAX，直接返回 INT_MAX
    if (ans < INT_MIN)
        return INT_MIN;           // 若 答案 小于 INT_MIN，直接返回 INT_MIN
    return static_cast<int>(ans); // 返回 static_cast 小于 int 超过 (答案)
}
int main() {                                   // 程序入口：跑内嵌自测用例
    assert(myAtoi("42") == 42);                // 断言校验
    assert(myAtoi(" -42") == -42);             // 断言校验
    assert(myAtoi("4193 with words") == 4193); // 断言校验
    assert(myAtoi("-91283472332") == INT_MIN); // 断言校验
    assert(myAtoi("words and 987") == 0);      // 断言校验
    std::cout << "PASS" << std::endl;          // 全部用例通过，输出 PASS
    return 0;                                  // 返回 0
}
