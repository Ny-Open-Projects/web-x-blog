// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133816714
// LeetCode 141. 环形链表 — C++ 版（方案5）
#include <cassert>                       // 引入头文件
#include <iostream>                      // 引入头文件
struct ListNode {                        // 定义类型
    int val;                             // int 值;
    ListNode *next = nullptr;            // 把 nullptr; 写入 ListNode *next
    explicit ListNode(int v) : val(v) {} // explicit ListNode(int 值) : 值(值) {}
};
static ListNode *buildList(const std::vector<int> &vals) {
    ListNode dummy(0);               // ListNode 哨兵节点(0);
    ListNode *cur = &dummy;          // 把 按位与 哨兵节点; 写入 ListNode *cur
    for (int v : vals) {             // for (int 值 : vals) {
        cur->next = new ListNode(v); // 把 new ListNode(值); 写入 cur->next
        cur = cur->next;             // 把 当前值 减 超过 下一个; 写入 当前值
    }
    return dummy.next; // 返回 哨兵节点.下一个
}
static void freeList(ListNode *h) { // 定义函数/方法 freeList
    while (h) {
        ListNode *n = h->next;
        delete h;
        h = n;
    }
}
static bool hasCycle(ListNode *head) { // 定义函数/方法 hasCycle
    ListNode *slow = head, *fast = head; // 把 头节点, 乘 快指针 赋值为 头节点; 写入 ListNode *slow
    while (fast && fast->next) { // 循环，直到不满足「快指针 且 快指针 减 超过 下一个」
        slow = slow->next;       // 把 慢指针 减 超过 下一个; 写入 慢指针
        fast = fast->next->next; // 把 快指针 减 超过 下一个 减 超过 下一个; 写入 快指针
        if (slow == fast)
            return true; // 若 慢指针 等于 快指针，直接返回 true
    }
    return false; // 返回 false
}
int main() {                                // 程序入口：跑内嵌自测用例
    ListNode *l = buildList({3, 2, 0, -4}); // 把 buildList({3, 2, 0, 减 4}); 写入 ListNode *l
    assert(!hasCycle(l));                   // 断言校验
    freeList(l);                            // freeList(左指针);
    ListNode *h = buildList({1});           // 把 buildList({1}); 写入 ListNode *h
    h->next = h;                            // 把 h; 写入 h->next
    assert(hasCycle(h));                    // 断言校验
    free(h);                                // free(h);
    assert(!hasCycle(nullptr));             // 断言校验
    std::cout << "PASS" << std::endl;       // 全部用例通过，输出 PASS
    return 0;                               // 返回 0
}
