// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133874590
// LeetCode 83. 删除排序链表中的重复元素 — C++ 版（方案5）
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
static ListNode *
deleteDuplicates(ListNode *head) { // static ListNode 乘 deleteDuplicates(ListNode 乘 头节点) {
    ListNode *cur = head;          // 把 头节点; 写入 ListNode *cur
    while (cur && cur->next) { // 循环，直到不满足「当前值 且 当前值 减 超过 下一个」
        if (cur->val == cur->next->val) { // 若 当前值 减 超过 值 等于 当前值 减 超过 下一个 减 超过 值
            ListNode *dup = cur->next; // 把 当前值 减 超过 下一个; 写入 ListNode *dup
            cur->next = dup->next;     // 把 dup 减 超过 下一个; 写入 cur->next
            delete dup;                // delete dup;
        } else {                       // 否则
            cur = cur->next;           // 把 当前值 减 超过 下一个; 写入 当前值
        }
    }
    return head; // 返回 头节点
}
int main() { // 程序入口：跑内嵌自测用例
    ListNode *r =
        deleteDuplicates(buildList({1, 1, 2})); // 把 deleteDuplicates(buildList({1, 1, 2})); 写入 ListNode *r
    assert((toVec(r) == std::vector<int>{1, 2})); // 断言校验
    freeList(r);                                  // freeList(右指针);
    ListNode *r2 = deleteDuplicates(buildList({1, 1, 2, 3, 3}));
    assert((toVec(r2) == std::vector<int>{1, 2, 3})); // 断言校验
    freeList(r2);                                     // freeList(r2);
    ListNode *r3 = deleteDuplicates(
        buildList({1, 1, 1})); // 把 deleteDuplicates(buildList({1, 1, 1})); 写入 ListNode *r3
    assert((toVec(r3) == std::vector<int>{1})); // 断言校验
    freeList(r3);                               // freeList(r3);
    std::cout << "PASS" << std::endl;           // 全部用例通过，输出 PASS
    return 0;                                   // 返回 0
}
