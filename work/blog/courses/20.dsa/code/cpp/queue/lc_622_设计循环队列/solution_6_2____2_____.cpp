// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130471048
// LeetCode 622. 设计循环队列 — C++ 版
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

// 方案6：数组 + front/rear/size 循环队列
class MyCircularQueue {    // 定义类型
    int capacity;          // int capacity;
    std::vector<int> data; // std::vector 小于 int 超过 data;
    int front;             // int front;
    int rear;              // int rear;
    int size;              // int 大小;

  public:                           // public:
    explicit MyCircularQueue(int k) // 定义函数/方法 MyCircularQueue
        : capacity(k), data(k, 0), front(0), rear(0), size(0) {
    } // : capacity(下标 k), data(下标 k, 0), front(0), rear(0), 大小(0) {}

    bool enQueue(int value) { // 定义函数/方法 enQueue
        if (isFull())
            return false;             // 若 isFull()，直接返回 false
        data[rear] = value;           // 把 value; 写入 data[rear]
        rear = (rear + 1) % capacity; // 把 (rear 加 1) 对…取模 capacity; 写入 rear
        size += 1;                    // 大小累加 1
        return true;                  // 返回 true
    }

    bool deQueue() { // 定义函数/方法 deQueue
        if (isEmpty())
            return false;               // 若 isEmpty()，直接返回 false
        front = (front + 1) % capacity; // 把 (front 加 1) 对…取模 capacity; 写入 front
        size -= 1;                      // 大小累减 1
        return true;                    // 返回 true
    }

    int Front() { // 定义函数/方法 Front
        if (isEmpty())
            return -1;      // 若 isEmpty()，直接返回 减 1
        return data[front]; // 返回 data[front]
    }

    int Rear() { // 定义函数/方法 Rear
        if (isEmpty())
            return -1;                                 // 若 isEmpty()，直接返回 减 1
        return data[(rear - 1 + capacity) % capacity]; // 返回 data[(rear 减 1 加 capacity) 对…取模 capacity]
    }

    bool isEmpty() const { return size == 0; } // 把 赋值为 0; } 写入 bool isEmpty() const { return size
    bool isFull() const {
        return size == capacity;
    } // 把 赋值为 capacity; } 写入 bool isFull() const { return size
};

int main() { // 程序入口：跑内嵌自测用例
    // 与 TS 事实源内嵌用例一致：[true,true,true,false,3,true,true,true,4]
    // 布尔结果用 1/0 表示
    MyCircularQueue q(3);                // MyCircularQueue 节点(3);
    std::vector<int> got;                // std::vector 小于 int 超过 got;
    got.push_back(q.enQueue(1) ? 1 : 0); // got 追加 节点.enQueue(1) ? 1 : 0);
    got.push_back(q.enQueue(2) ? 1 : 0); // got 追加 节点.enQueue(2) ? 1 : 0);
    got.push_back(q.enQueue(3) ? 1 : 0); // got 追加 节点.enQueue(3) ? 1 : 0);
    got.push_back(q.enQueue(4) ? 1 : 0); // got 追加 节点.enQueue(4) ? 1 : 0);
    got.push_back(q.Rear());             // got 追加 节点.Rear());
    got.push_back(q.isFull() ? 1 : 0);   // got 追加 节点.isFull() ? 1 : 0);
    got.push_back(q.deQueue() ? 1 : 0);  // got 追加 节点.deQueue() ? 1 : 0);
    got.push_back(q.enQueue(4) ? 1 : 0); // got 追加 节点.enQueue(4) ? 1 : 0);
    got.push_back(q.Rear());             // got 追加 节点.Rear());
    std::vector<int> want = {1, 1, 1, 0, 3,
                             1, 1, 1, 4};   // 把 { 1, 1, 1, 0, 3, 1, 1, 1, 4 }; 写入 std::vector<int> want
    if (got != want) {                      // 若 got 不等于 want
        std::cout << "FAILED" << std::endl; // 打印输出
        return 1;                           // 返回 1
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
