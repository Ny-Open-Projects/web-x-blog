// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114011
// LeetCode 232. 用栈实现队列 — C++ 版（方案1）
#include <cassert>               // 引入头文件
#include <iostream>              // 引入头文件
#include <stack>                 // 引入头文件
struct MyQueue {                 // 定义类型
    std::stack<int> inSt, outSt; // std::栈 小于 int 超过 inSt, outSt;
    void in2out() {
        while (!inSt.empty()) {
            outSt.push(inSt.top());
            inSt.pop();
        }
    }                                  // 把 inSt.top( 压入栈/数组尾部
    void push(int x) { inSt.push(x); } // 把 x 压入栈/数组尾部
    int pop() {                        // 定义函数/方法 pop
        if (outSt.empty())
            in2out();        // 若 outSt 是否为空) in2out();
        int v = outSt.top(); // 把 outSt.top() 存入 值
        outSt.pop();         // 弹出栈顶元素
        return v;            // 返回 值
    }
    int peek() { // 定义函数/方法 peek
        if (outSt.empty())
            in2out();       // 若 outSt 是否为空) in2out();
        return outSt.top(); // 返回 outSt.top()
    }
    bool empty() {
        return inSt.empty() && outSt.empty();
    } // bool empty() { return inSt 是否为空 且 outSt 是否为空; }
};
int main() {               // 程序入口：跑内嵌自测用例
    MyQueue q;             // MyQueue 节点;
    q.push(1);             // 把 1 压入栈/数组尾部
    q.push(2);             // 把 2 压入栈/数组尾部
    assert(q.peek() == 1); // 断言校验
    assert(q.pop() == 1);  // 断言校验
    assert(!q.empty());    // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS