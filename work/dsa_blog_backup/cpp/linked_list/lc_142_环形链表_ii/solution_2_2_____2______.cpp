// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133874671
// LeetCode 142. 环形链表II — C++ 版（方案2）
#include <cassert>                       // 引入头文件
#include <iostream>                      // 引入头文件
struct ListNode {                        // 定义类型
    int val;                             // int 值;
    ListNode *next = nullptr;            // 把 nullptr; 写入 ListNode *next
    explicit ListNode(int v) : val(v) {} // explicit ListNode(int 值) : 值(值) {}
};
static ListNode *buildWithCycle(const std::vector<int> &vals, int pos) {
    ListNode dummy(0);                         // ListNode 哨兵节点(0);
    ListNode *cur = &dummy;                    // 把 按位与 哨兵节点; 写入 ListNode *cur
    ListNode *tailAt = nullptr;                // 把 nullptr; 写入 ListNode *tailAt
    for (size_t i = 0; i < vals.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 vals.大小() 就继续
        cur->next = new ListNode(vals[i]); // 把 new ListNode(vals[下标 i]); 写入 cur->next
        cur = cur->next;                   // 把 当前值 减 超过 下一个; 写入 当前值
        if (static_cast<int>(i) + 1 == pos)
            tailAt = cur; // 若 static_cast 小于 int 超过 (下标 i) 加 1 等于 pos) tailAt 赋值为 当前值;
    }
    if (tailAt)
        cur->next = tailAt; // 若 tailAt) 当前值 减 超过 下一个 赋值为 tailAt;
    return dummy.next;      // 返回 哨兵节点.下一个
}
static ListNode *detectCycle(ListNode *head) { // static ListNode 乘 detectCycle(ListNode 乘 头节点) {
    ListNode *slow = head, *fast = head; // 把 头节点, 乘 快指针 赋值为 头节点; 写入 ListNode *slow
    while (fast && fast->next) { // 循环，直到不满足「快指针 且 快指针 减 超过 下一个」
        slow = slow->next;       // 把 慢指针 减 超过 下一个; 写入 慢指针
        fast = fast->next->next; // 把 快指针 减 超过 下一个 减 超过 下一个; 写入 快指针
        if (slow == fast) {      // 若 慢指针 等于 快指针
            ListNode *p1 = head, *p2 = slow; // 把 头节点, 乘 p2 赋值为 慢指针; 写入 ListNode *p1
            while (p1 != p2) {
                p1 = p1->next;
                p2 = p2->next;
            }
            return p1; // 返回 p1
        }
    }
    return nullptr; // 返回 nullptr
}
int main() {                                        // 程序入口：跑内嵌自测用例
    ListNode *h = buildWithCycle({3, 2, 0, -4}, 2); // 把 buildWithCycle({3, 2, 0, 减 4}, 2); 写入 ListNode *h
    ListNode *e = detectCycle(h);                   // 把 detectCycle(h); 写入 ListNode *e
    assert(e != nullptr && e->val == 2);            // 断言校验
    ListNode *s = new ListNode(1);                  // 把 new ListNode(1); 写入 ListNode *s
    assert(detectCycle(s) == nullptr);              // 断言校验
    std::cout << "PASS" << std::endl;               // 全部用例通过，输出 PASS
    return 0;                                       // 返回 0
}
