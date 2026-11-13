// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133886377
// LeetCode 237. 删除链表中的节点 — C++ 版（方案2）
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
static void deleteNode(ListNode *node) { // 定义函数/方法 deleteNode
    ListNode *next = node->next;         // 把 节点 减 超过 下一个; 写入 ListNode *next
    node->val = next->val;               // 把 下一个 减 超过 值; 写入 node->val
    node->next = next->next;             // 把 下一个 减 超过 下一个; 写入 node->next
    delete next;                         // delete 下一个;
}
int main() {                                         // 程序入口：跑内嵌自测用例
    ListNode *l = buildList({4, 5, 1, 9});           // 把 buildList({4, 5, 1, 9}); 写入 ListNode *l
    deleteNode(l->next);                             // deleteNode(左指针 减 超过 下一个);
    assert((toVec(l) == std::vector<int>{4, 1, 9})); // 断言校验
    freeList(l);                                     // freeList(左指针);
    ListNode *l2 = buildList({1, 2, 3});             // 把 buildList({1, 2, 3}); 写入 ListNode *l2
    deleteNode(l2->next);                            // deleteNode(l2 减 超过 下一个);
    assert((toVec(l2) == std::vector<int>{1, 3}));   // 断言校验
    freeList(l2);                                    // freeList(l2);
    std::cout << "PASS" << std::endl;                // 全部用例通过，输出 PASS
    return 0;                                        // 返回 0
}
