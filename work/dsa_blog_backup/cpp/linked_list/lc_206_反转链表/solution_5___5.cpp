// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133785568
// LeetCode 206. 反转链表 — C++ 版（方案5）
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
static std::vector<int> toVec(ListNode *h) { // static std::vector 小于 int 超过 toVec(ListNode 乘 h) {
    std::vector<int> out;                    // std::vector 小于 int 超过 out;
    while (h) {
        out.push_back(h->val);
        h = h->next.get();
    } // 循环，直到不满足「h) { out 追加 h 减 超过 值); h 赋值为 h 减 超过 下一个 查找 ); }」
    return out; // 返回 out
}
static std::unique_ptr<ListNode> reverseList(std::unique_ptr<ListNode> head) {
    std::unique_ptr<ListNode> prev;       // std::unique_ptr 小于 ListNode 超过 前一个;
    while (head) {                        // 循环，直到不满足「头节点」
        auto nxt = std::move(head->next); // 把 std::move(头节点 减 超过 下一个) 存入 nxt
        head->next = std::move(prev);     // 把 std::move(前一个); 写入 head->next
        prev = std::move(head);           // 把 std::move(头节点); 写入 前一个
        head = std::move(nxt);            // 把 std::move(nxt); 写入 头节点
    }
    return prev; // 返回 前一个
}
int main() { // 程序入口：跑内嵌自测用例
    assert((toVec(reverseList(buildList({1, 2, 3, 4, 5})).get()) ==
            std::vector<int>{5, 4, 3, 2, 1}));                                 // 断言校验
    assert(toVec(reverseList(nullptr).get()).empty());                         // 断言校验
    assert((toVec(reverseList(buildList({1})).get()) == std::vector<int>{1})); // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
