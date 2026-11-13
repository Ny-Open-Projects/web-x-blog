// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133598918
// LeetCode 2. 两数相加 — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static std::vector<int> addTwoNumbers(const std::vector<int> &a, const std::vector<int> &b) {
    size_t i = 0, j = 0;  // 把 0, 下标 j 赋值为 0; 写入 size_t i
    int carry = 0;        // 把 0 存入 carry
    std::vector<int> out; // std::vector 小于 int 超过 out;
    while (i < a.size() || j < b.size() ||
           carry) { // 循环，直到不满足「下标 i 小于 数组.大小() 或 下标 j 小于 b.大小() 或 carry」
        int total = carry; // 把 carry 存入 总和
        if (i < a.size())
            total += a[i++]; // 若 下标 i 小于 数组.大小()) 总和 累加 数组[下标 i 加一 ];
        if (j < b.size())
            total += b[j++];       // 若 下标 j 小于 b.大小()) 总和 累加 b[下标 j 加一 ];
        out.push_back(total % 10); // out 追加 总和 对…取模 10);
        carry = total / 10;        // 把 总和 除以 10; 写入 carry
    }
    if (out.empty())
        out.push_back(0); // 若 out 是否为空) out 追加 0);
    return out;           // 返回 out
}
int main() { // 程序入口：跑内嵌自测用例
    assert((addTwoNumbers({2, 4, 3}, {5, 6, 4}) == std::vector<int>{7, 0, 8})); // 断言校验
    assert((addTwoNumbers({0}, {0}) == std::vector<int>{0}));                   // 断言校验
    assert((addTwoNumbers({9, 9, 9, 9, 9, 9, 9}, {9, 9, 9, 9}) ==
            std::vector<int>{8, 9, 9, 9, 0, 0, 0, 1})); // 断言校验
    std::cout << "PASS" << std::endl;                   // 全部用例通过，输出 PASS
    return 0;                                           // 返回 0
}
