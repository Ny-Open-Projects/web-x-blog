// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145198996
// LeetCode 225. 用队列实现栈 — C++ 版（方案2）
#include <cassert>                        // 引入头文件
#include <deque>                          // 引入头文件
#include <iostream>                       // 引入头文件
struct MyStack {                          // 定义类型
    std::deque<int> q;                    // std::deque 小于 int 超过 节点;
    void push(int x) { q.push_front(x); } // void push(int x) { 节点.push_front(x); }
    int pop() {
        int v = q.front();
        q.pop_front();
        return v;
    }
    int top() { return q.front(); }    // int top() { return 节点.front(); }
    bool empty() { return q.empty(); } // bool empty() { return 节点 是否为空; }
};
int main() {              // 程序入口：跑内嵌自测用例
    MyStack s;            // MyStack 字符串;
    s.push(1);            // 把 1 压入栈/数组尾部
    s.push(2);            // 把 2 压入栈/数组尾部
    assert(s.top() == 2); // 断言校验
    assert(s.pop() == 2); // 断言校验
    assert(!s.empty());   // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS