// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130736023
// LeetCode 415. 字符串相加 — C++ 版（方案2）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <string>    // 引入头文件
static std::string addStrings(const std::string &a, const std::string &b) {
    int i = static_cast<int>(a.size()) - 1, j = static_cast<int>(b.size()) - 1, carry = 0;
    std::string out;                    // std::string out;
    while (i >= 0 || j >= 0 || carry) { // 循环，直到不满足「下标 i 不低于 0 或 下标 j 不低于 0 或 carry」
        int total = carry; // 把 carry 存入 总和
        if (i >= 0)
            total += a[i--] - '0'; // 若 下标 i 不低于 0) 总和 累加 数组[下标 i 减一 ] 减 '0';
        if (j >= 0)
            total += b[j--] - '0'; // 若 下标 j 不低于 0) 总和 累加 b[下标 j 减一 ] 减 '0';
        out.push_back('0' + total % 10); // out 追加 '0' 加 总和 对…取模 10);
        carry = total / 10;              // 把 总和 除以 10; 写入 carry
    }
    if (out.empty())
        out = "0";                        // 若 out 是否为空) out 赋值为 「0」;
    std::reverse(out.begin(), out.end()); // std::reverse(out 迭代位置 , out.终点());
    return out;                           // 返回 out
}
int main() {                                  // 程序入口：跑内嵌自测用例
    assert(addStrings("11", "123") == "134"); // 断言校验
    assert(addStrings("456", "77") == "533"); // 断言校验
    assert(addStrings("0", "0") == "0");      // 断言校验
    std::cout << "PASS" << std::endl;         // 全部用例通过，输出 PASS
    return 0;                                 // 返回 0
}
