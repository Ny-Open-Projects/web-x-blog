// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133922762
// LeetCode 160. 相交链表 — C++ 版（方案1）
#include <cassert>                       // 引入头文件
#include <iostream>                      // 引入头文件
struct ListNode {                        // 定义类型
    int val;                             // int 值;
    ListNode *next = nullptr;            // 把 nullptr; 写入 ListNode *next
    explicit ListNode(int v) : val(v) {} // explicit ListNode(int 值) : 值(值) {}
};
static ListNode *getIntersectionNode(ListNode *a, ListNode *b) {
    if (!a || !b)
        return nullptr;         // 若 取反 数组 或 取反 b，直接返回 nullptr
    ListNode *p1 = a, *p2 = b;  // 把 数组, 乘 p2 赋值为 b; 写入 ListNode *p1
    while (p1 != p2) {          // 循环，直到不满足「p1 不等于 p2」
        p1 = p1 ? p1->next : b; // 把 p1 ? p1 减 超过 下一个 : b; 写入 p1
        p2 = p2 ? p2->next : a; // 把 p2 ? p2 减 超过 下一个 : 数组; 写入 p2
    }
    return p1; // 返回 p1
}
int main() {                                     // 程序入口：跑内嵌自测用例
    ListNode *shared = new ListNode(8);          // 把 new ListNode(8); 写入 ListNode *shared
    shared->next = new ListNode(4);              // 把 new ListNode(4); 写入 shared->next
    shared->next->next = new ListNode(5);        // 把 new ListNode(5); 写入 shared->next->next
    ListNode *a = new ListNode(4);               // 把 new ListNode(4); 写入 ListNode *a
    a->next = new ListNode(1);                   // 把 new ListNode(1); 写入 a->next
    a->next->next = shared;                      // 把 shared; 写入 a->next->next
    ListNode *b = new ListNode(5);               // 把 new ListNode(5); 写入 ListNode *b
    b->next = new ListNode(6);                   // 把 new ListNode(6); 写入 b->next
    b->next->next = new ListNode(1);             // 把 new ListNode(1); 写入 b->next->next
    b->next->next->next = shared;                // 把 shared; 写入 b->next->next->next
    assert(getIntersectionNode(a, b) == shared); // 断言校验
    assert(getIntersectionNode(new ListNode(1), new ListNode(1)) == nullptr); // 断言校验
    assert(getIntersectionNode(nullptr, nullptr) == nullptr);                 // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
