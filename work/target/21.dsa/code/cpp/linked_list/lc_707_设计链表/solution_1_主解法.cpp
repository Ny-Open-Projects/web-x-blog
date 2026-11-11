// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134120377
// LeetCode 707. 设计链表 — C++ 版（方案1）
#include <cassert>          // 引入头文件
#include <iostream>         // 引入头文件
#include <vector>           // 引入头文件
struct MyLinkedList {       // 定义类型
    std::vector<int> items; // std::vector 小于 int 超过 items;
    void addAtHead(int x) {
        items.insert(items.begin(), x);
    } // void addAtHead(int x) { items 插入 items 迭代位置 , x); }
    void addAtTail(int x) { items.push_back(x); } // void addAtTail(int x) { items 追加 x); }
    void addAtIndex(int idx, int x) {             // 定义函数/方法 addAtIndex
        if (idx < 0)
            idx = 0; // 若 idx 小于 0) idx 赋值为 0;
        if (idx > static_cast<int>(items.size()))
            return; // 若 idx 超过 static_cast 小于 int 超过 (items.大小())) return;
        items.insert(items.begin() + idx, x); // items 插入 items 迭代位置 加 idx, x);
    }
    int get(int idx) { // 定义函数/方法 get
        if (idx < 0 || idx >= static_cast<int>(items.size()))
            return -1;
        return items[idx]; // 返回 items[idx]
    }
    void deleteAtIndex(int idx) { // 定义函数/方法 deleteAtIndex
        if (idx < 0 || idx >= static_cast<int>(items.size()))
            return;
        items.erase(items.begin() + idx); // items 删除 items 迭代位置 加 idx);
    }
};
int main() {                          // 程序入口：跑内嵌自测用例
    MyLinkedList l;                   // MyLinkedList 左指针;
    l.addAtHead(1);                   // 左指针.addAtHead(1);
    l.addAtTail(3);                   // 左指针.addAtTail(3);
    l.addAtIndex(1, 2);               // 左指针.addAtIndex(1, 2);
    assert(l.get(1) == 2);            // 断言校验
    l.deleteAtIndex(1);               // 左指针.deleteAtIndex(1);
    assert(l.get(1) == 3);            // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
