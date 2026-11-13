// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133867938
// LeetCode 876. 链表的中间结点 — C++ 版（方案3）
#include <cassert>                       // 引入头文件
#include <iostream>                      // 引入头文件
#include <memory>                        // 引入头文件
#include <vector>                        // 引入头文件
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
static void freeList(ListNode *h) {
    while (h) {
        ListNode *n = h->next;
        delete h;
        h = n;
    }
}
static std::vector<int> toVec(ListNode *h) { // static std::vector 小于 int 超过 toVec(ListNode 乘 h) {
    std::vector<int> out;                    // std::vector 小于 int 超过 out;
    while (h) {
        out.push_back(h->val);
        h = h->next;
    } // 循环，直到不满足「h) { out 追加 h 减 超过 值); h 赋值为 h 减 超过 下一个; }」
    return out; // 返回 out
}
static ListNode *middleNode(ListNode *head) { // static ListNode 乘 middleNode(ListNode 乘 头节点) {
    ListNode *slow = head, *fast = head; // 把 头节点, 乘 快指针 赋值为 头节点; 写入 ListNode *slow
    while (fast && fast->next) { // 循环，直到不满足「快指针 且 快指针 减 超过 下一个」
        slow = slow->next;       // 把 慢指针 减 超过 下一个; 写入 慢指针
        fast = fast->next->next; // 把 快指针 减 超过 下一个 减 超过 下一个; 写入 快指针
    }
    return slow; // 返回 慢指针
}
int main() { // 程序入口：跑内嵌自测用例
    ListNode *m =
        middleNode(buildList({1, 2, 3, 4, 5})); // 把 middleNode(buildList({1, 2, 3, 4, 5})); 写入 ListNode *m
    assert((toVec(m) == std::vector<int>{3, 4, 5})); // 断言校验
    freeList(m);                                     // freeList(映射表);
    ListNode *m2 = middleNode(
        buildList({1, 2, 3, 4, 5, 6})); // 把 middleNode(buildList({1, 2, 3, 4, 5, 6})); 写入 ListNode *m2
    assert((toVec(m2) == std::vector<int>{4, 5, 6})); // 断言校验
    freeList(m2);                                     // freeList(m2);
    ListNode *m3 = middleNode(buildList({1}));        // 把 middleNode(buildList({1})); 写入 ListNode *m3
    assert((toVec(m3) == std::vector<int>{1}));       // 断言校验
    freeList(m3);                                     // freeList(m3);
    std::cout << "PASS" << std::endl;                 // 全部用例通过，输出 PASS
    return 0;                                         // 返回 0
}
