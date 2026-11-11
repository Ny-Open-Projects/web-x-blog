// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245934
// LeetCode 155. 最小栈 — C++ 版（方案2）
#include <cassert>               // 引入头文件
#include <iostream>              // 引入头文件
#include <vector>                // 引入头文件
struct MinStack {                // 定义类型
    std::vector<int> vals, mins; // std::vector 小于 int 超过 vals, mins;
    void push(int v) {           // 定义函数/方法 push
        vals.push_back(v);       // vals 追加 值);
        mins.push_back(mins.empty()
                           ? v
                           : std::min(mins.back(),
                                      v)); // mins 追加 mins 是否为空 ? 值 : std::取较小值 mins.back(), 值));
    }
    void pop() {
        vals.pop_back();
        mins.pop_back();
    }                                    // 弹出栈顶元素
    int top() { return vals.back(); }    // int top() { return vals.back(); }
    int getMin() { return mins.back(); } // int getMin() { return mins.back(); }
};
int main() {                  // 程序入口：跑内嵌自测用例
    MinStack s;               // MinStack 字符串;
    s.push(-2);               // 把 减 2 压入栈/数组尾部
    s.push(0);                // 把 0 压入栈/数组尾部
    s.push(-3);               // 把 减 3 压入栈/数组尾部
    assert(s.getMin() == -3); // 断言校验
    s.pop();                  // 弹出栈顶元素
    assert(s.top() == 0);     // 断言校验
    assert(s.getMin() == -2); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS