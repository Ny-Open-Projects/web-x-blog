// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130701795
// LeetCode 43. 字符串相乘 — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <string>   // 引入头文件
#include <vector>   // 引入头文件
static std::string multiply(const std::string &num1, const std::string &num2) {
    if (num1 == "0" || num2 == "0")
        return "0"; // 若 num1 等于 「0」 或 num2 等于 「0」，直接返回 「0」
    int m = static_cast<int>(num1.size()), n = static_cast<int>(num2.size());
    std::vector<int> result(m + n, 0); // std::vector 小于 int 超过 结果(映射表 加 元素个数, 0);
    for (int i = m - 1; i >= 0; --i) { // 让 下标 i 从 映射表 减 1 开始计数，下标 i 不低于 0 就继续
        for (int j = n - 1; j >= 0; --j) { // 让 下标 j 从 元素个数 减 1 开始计数，下标 j 不低于 0 就继续
            int mul = (num1[i] - '0') *
                      (num2[j] - '0'); // 把 (num1[下标 i] 减 '0') 乘 (num2[下标 j] 减 '0') 存入 mul
            int p1 = i + j, p2 = i + j + 1; // 把 下标 i 加 下标 j, p2 赋值为 下标 i 加 下标 j 加 1 存入 p1
            int total = mul + result[p2]; // 把 mul 加 结果[p2] 存入 总和
            result[p2] = total % 10;      // 把 总和 对…取模 10; 写入 result[p2]
            result[p1] += total / 10;     // result[p1]累加 总和 除以 10
        }
    }
    std::string out;       // std::string out;
    bool started = false;  // 把 false 存入 started
    for (int d : result) { // for (int d : 结果) {
        if (d != 0 || started) {
            out.push_back('0' + d);
            started = true;
        } // 若 d 不等于 0 或 started) { out 追加 '0' 加 d); started 赋值为 true; }
    }
    if (out.empty())
        out = "0"; // 若 out 是否为空) out 赋值为 「0」;
    return out;    // 返回 out
}
int main() {                                   // 程序入口：跑内嵌自测用例
    assert(multiply("2", "3") == "6");         // 断言校验
    assert(multiply("123", "456") == "56088"); // 断言校验
    std::cout << "PASS" << std::endl;          // 全部用例通过，输出 PASS
    return 0;                                  // 返回 0
}
