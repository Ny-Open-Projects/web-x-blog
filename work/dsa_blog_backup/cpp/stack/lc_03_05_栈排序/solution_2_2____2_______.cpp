// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397311
// LeetCode 面试题 03.05. 栈排序 — C++ 版（方案2）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <stack>     // 引入头文件
#include <vector>    // 引入头文件
static std::vector<int> sortedStack(const std::vector<int> &input) {
    std::stack<int> stk, temp; // std::栈 小于 int 超过 栈, 临时变量;
    std::vector<int> output;   // std::vector 小于 int 超过 输出;
    for (int v : input)
        stk.push(v);       // 把 值 压入栈/数组尾部
    while (!stk.empty()) { // 循环，直到不满足「取反 栈.empty(」
        int v = stk.top(); // 把 栈.top() 存入 值
        stk.pop();         // 弹出栈顶元素
        while (!temp.empty() &&
               temp.top() > v) { // 循环，直到不满足「取反 临时变量 是否为空 且 临时变量.top() 超过 值」
            output.push_back(temp.top()); // 输出 追加 临时变量.top());
            temp.pop();                   // 弹出栈顶元素
        }
        temp.push(v); // 把 值 压入栈/数组尾部
    }
    while (!temp.empty()) {           // 循环，直到不满足「取反 临时变量.empty(」
        output.push_back(temp.top()); // 输出 追加 临时变量.top());
        temp.pop();                   // 弹出栈顶元素
    }
    std::sort(output.begin(), output.end()); // std::sort(输出 迭代位置 , 输出.终点());
    return output;                           // 返回 输出
}
int main() {
    assert((sortedStack({5, 2, 1, 4, 3}) == std::vector<int>{1, 2, 3, 4, 5}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS