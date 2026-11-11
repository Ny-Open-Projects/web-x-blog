// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145361774
// LeetCode 641. 设计循环双端队列 — C++ 版（方案2）
#include <cassert>                        // 引入头文件
#include <iostream>                       // 引入头文件
#include <vector>                         // 引入头文件
struct MyCircularDeque {                  // 定义类型
    std::vector<int> data;                // std::vector 小于 int 超过 data;
    size_t head = 0, tail = 0, size_ = 0; // 把 0, 尾节点 赋值为 0, size_ 赋值为 0; 写入 size_t head
    explicit MyCircularDeque(int k) : data(static_cast<size_t>(k)) {}
    bool insertFront(int v) { // 定义函数/方法 insertFront
        if (size_ == data.size())
            return false; // 若 size_ 等于 data.大小()，直接返回 false
        head = (head + data.size() - 1) %
               data.size(); // 把 (头节点 加 data.大小() 减 1) 对…取模 data.大小(); 写入 头节点
        data[head] = v; // 把 值; 写入 data[head]
        ++size_;        // 加一 size_;
        return true;    // 返回 true
    }
    bool insertLast(int v) { // 定义函数/方法 insertLast
        if (size_ == data.size())
            return false;                // 若 size_ 等于 data.大小()，直接返回 false
        data[tail] = v;                  // 把 值; 写入 data[tail]
        tail = (tail + 1) % data.size(); // 把 (尾节点 加 1) 对…取模 data.大小(); 写入 尾节点
        ++size_;                         // 加一 size_;
        return true;                     // 返回 true
    }
    bool deleteFront() { // 定义函数/方法 deleteFront
        if (size_ == 0)
            return false;                // 若 size_ 等于 0，直接返回 false
        head = (head + 1) % data.size(); // 把 (头节点 加 1) 对…取模 data.大小(); 写入 头节点
        --size_;                         // 减一 size_;
        return true;                     // 返回 true
    }
    bool deleteLast() { // 定义函数/方法 deleteLast
        if (size_ == 0)
            return false; // 若 size_ 等于 0，直接返回 false
        tail = (tail + data.size() - 1) %
               data.size(); // 把 (尾节点 加 data.大小() 减 1) 对…取模 data.大小(); 写入 尾节点
        --size_;            // 减一 size_;
        return true;        // 返回 true
    }
    int getFront() { return size_ == 0 ? -1 : data[head]; }
    int getRear() { return size_ == 0 ? -1 : data[(tail + data.size() - 1) % data.size()]; }
    bool isEmpty() { return size_ == 0; } // 把 赋值为 0; } 写入 bool isEmpty() { return size_
    bool isFull() {
        return size_ == data.size();
    } // 把 赋值为 data.大小(); } 写入 bool isFull() { return size_
};
int main() {                   // 程序入口：跑内嵌自测用例
    MyCircularDeque d(3);      // MyCircularDeque d(3);
    assert(d.insertLast(1));   // 断言校验
    assert(d.insertLast(2));   // 断言校验
    assert(d.insertFront(3));  // 断言校验
    assert(!d.insertFront(4)); // 断言校验
    assert(d.getRear() == 2);  // 断言校验
    assert(d.isFull());        // 断言校验
    assert(d.deleteLast());    // 断言校验
    assert(d.insertFront(4));  // 断言校验
    assert(d.getFront() == 4); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS