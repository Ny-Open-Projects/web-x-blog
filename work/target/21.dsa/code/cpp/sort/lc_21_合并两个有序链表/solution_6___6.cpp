// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133594090
// LeetCode 21. 合并两个有序链表 — C++ 版（方案6）
#include <cassert>                       // 引入头文件
#include <iostream>                      // 引入头文件
#include <memory>                        // 引入头文件
#include <vector>                        // 引入头文件
struct ListNode {                        // 定义类型
    int val;                             // int 值;
    std::unique_ptr<ListNode> next;      // std::unique_ptr 小于 ListNode 超过 下一个;
    explicit ListNode(int v) : val(v) {} // explicit ListNode(int 值) : 值(值) {}
};
static std::unique_ptr<ListNode> buildList(const std::vector<int> &vals) {
    ListNode dummy(0);      // ListNode 哨兵节点(0);
    ListNode *cur = &dummy; // 把 按位与 哨兵节点; 写入 ListNode *cur
    for (int v : vals) {    // for (int 值 : vals) {
        cur->next =
            std::make_unique<ListNode>(v); // 把 std::make_unique 小于 ListNode 超过 (值); 写入 cur->next
        cur = cur->next.get();             // 把 当前值 减 超过 下一个 查找 ); 写入 当前值
    }
    return std::move(dummy.next); // 返回 std::move(哨兵节点.下一个)
}
static std::vector<int>
listToVec(ListNode *head) { // static std::vector 小于 int 超过 listToVec(ListNode 乘 头节点) {
    std::vector<int> out;   // std::vector 小于 int 超过 out;
    while (head) {
        out.push_back(head->val);
        head = head->next.get();
    }
    return out; // 返回 out
}
static std::unique_ptr<ListNode> mergeTwoLists(std::unique_ptr<ListNode> l1, std::unique_ptr<ListNode> l2) {
    ListNode dummy(0);               // ListNode 哨兵节点(0);
    ListNode *p = &dummy;            // 把 按位与 哨兵节点; 写入 ListNode *p
    while (l1 && l2) {               // 循环，直到不满足「l1 且 l2」
        if (l1->val < l2->val) {     // 若 l1 减 超过 值 小于 l2 减 超过 值
            p->next = std::move(l1); // 把 std::move(l1); 写入 p->next
            l1 = std::move(p->next->next); // 把 std::move(节点 减 超过 下一个 减 超过 下一个); 写入 l1
        } else {                           // 否则
            p->next = std::move(l2); // 把 std::move(l2); 写入 p->next
            l2 = std::move(p->next->next); // 把 std::move(节点 减 超过 下一个 减 超过 下一个); 写入 l2
        }
        p = p->next.get(); // 把 节点 减 超过 下一个 查找 ); 写入 节点
    }
    p->next = l1 ? std::move(l1) : std::move(l2); // 把 l1 ? std::move(l1) : std::move(l2); 写入 p->next
    return std::move(dummy.next);                 // 返回 std::move(哨兵节点.下一个)
}
int main() { // 程序入口：跑内嵌自测用例
    auto got = listToVec(mergeTwoLists(buildList({1, 2, 4}), buildList({1, 3, 4})).get());
    assert((got == std::vector<int>{1, 1, 2, 3, 4, 4}));              // 断言校验
    assert(listToVec(mergeTwoLists(nullptr, nullptr).get()).empty()); // 断言校验
    auto got3 = listToVec(mergeTwoLists(nullptr, buildList({0})).get());
    assert((got3 == std::vector<int>{0})); // 断言校验
    std::cout << "PASS" << std::endl;      // 全部用例通过，输出 PASS
    return 0;                              // 返回 0
}
