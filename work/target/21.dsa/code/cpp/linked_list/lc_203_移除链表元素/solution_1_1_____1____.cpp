// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133813394
// LeetCode 203. 移除链表元素 — C++ 版（方案1）
#include <cassert>                       // 引入头文件
#include <iostream>                      // 引入头文件
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
static ListNode *removeElements(ListNode *head,
                                int val) { // static ListNode 乘 removeElements(ListNode 乘 头节点, int 值) {
    ListNode dummy(0);                     // ListNode 哨兵节点(0);
    dummy.next = head;                     // 把 头节点; 写入 下一个
    ListNode *cur = &dummy;                // 把 按位与 哨兵节点; 写入 ListNode *cur
    while (cur->next) {                    // 循环，直到不满足「当前值 减 超过 下一个」
        if (cur->next->val == val) {       // 若 当前值 减 超过 下一个 减 超过 值 等于 值
            ListNode *rm = cur->next;      // 把 当前值 减 超过 下一个; 写入 ListNode *rm
            cur->next = rm->next;          // 把 rm 减 超过 下一个; 写入 cur->next
            delete rm;                     // delete rm;
        } else {                           // 否则
            cur = cur->next;               // 把 当前值 减 超过 下一个; 写入 当前值
        }
    }
    return dummy.next; // 返回 哨兵节点.下一个
}
int main() { // 程序入口：跑内嵌自测用例
    ListNode *r = removeElements(buildList({1, 2, 3, 4, 5, 6}), 6);
    assert((toVec(r) == std::vector<int>{1, 2, 3, 4, 5}));         // 断言校验
    freeList(r);                                                   // freeList(右指针);
    assert(removeElements(buildList({7, 7, 7, 7}), 7) == nullptr); // 断言校验
    ListNode *r3 = removeElements(buildList({1, 2, 2, 1}), 2);
    assert((toVec(r3) == std::vector<int>{1, 1})); // 断言校验
    freeList(r3);                                  // freeList(r3);
    std::cout << "PASS" << std::endl;              // 全部用例通过，输出 PASS
    return 0;                                      // 返回 0
}
