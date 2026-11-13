// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133746567
// LeetCode 19. 删除链表的倒数第N个结点 — C++ 版（方案4）
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
static ListNode *removeNthFromEnd(ListNode *head, int n) {
    ListNode dummy(0); // ListNode 哨兵节点(0);
    dummy.next = head; // 把 头节点; 写入 下一个
    ListNode *fast = &dummy,
             *slow = &dummy; // 把 按位与 哨兵节点, 乘 慢指针 赋值为 按位与 哨兵节点; 写入 ListNode *fast
    for (int i = 0; i <= n; ++i)
        fast = fast->next; // 让 下标 i 从 0 开始计数，下标 i 不超过 元素个数 就继续
    while (fast) {
        fast = fast->next;
        slow = slow->next;
    }
    ListNode *rm = slow->next; // 把 慢指针 减 超过 下一个; 写入 ListNode *rm
    slow->next = rm->next;     // 把 rm 减 超过 下一个; 写入 slow->next
    delete rm;                 // delete rm;
    return dummy.next;         // 返回 哨兵节点.下一个
}
int main() { // 程序入口：跑内嵌自测用例
    ListNode *r = removeNthFromEnd(buildList({1, 2, 3, 4, 5}), 2);
    assert((toVec(r) == std::vector<int>{1, 2, 3, 5})); // 断言校验
    freeList(r);                                        // freeList(右指针);
    ListNode *r2 =
        removeNthFromEnd(buildList({1}), 1); // 把 removeNthFromEnd(buildList({1}), 1); 写入 ListNode *r2
    assert(r2 == nullptr);                   // 断言校验
    ListNode *r3 = removeNthFromEnd(buildList({1, 2}),
                                    2); // 把 removeNthFromEnd(buildList({1, 2}), 2); 写入 ListNode *r3
    assert((toVec(r3) == std::vector<int>{2})); // 断言校验
    freeList(r3);                               // freeList(r3);
    std::cout << "PASS" << std::endl;           // 全部用例通过，输出 PASS
    return 0;                                   // 返回 0
}
