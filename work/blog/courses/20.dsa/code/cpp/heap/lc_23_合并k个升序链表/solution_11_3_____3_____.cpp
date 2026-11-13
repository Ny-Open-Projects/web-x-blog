// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134283831
// LeetCode 23. 合并K个升序链表 — C++ 版（方案11）
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
static ListNode *mergeTwo(ListNode *a,
                          ListNode *b) { // static ListNode 乘 mergeTwo(ListNode 乘 数组, ListNode 乘 b) {
    ListNode dummy(0);                   // ListNode 哨兵节点(0);
    ListNode *cur = &dummy;              // 把 按位与 哨兵节点; 写入 ListNode *cur
    while (a && b) {                     // 循环，直到不满足「数组 且 b」
        if (a->val <= b->val) {
            cur->next = std::unique_ptr<ListNode>(a);
            a = a->next.release();
        } else {
            cur->next = std::unique_ptr<ListNode>(b);
            b = b->next.release();
        }                      // 否则
        cur = cur->next.get(); // 把 当前值 减 超过 下一个 查找 ); 写入 当前值
    }
    cur->next = std::unique_ptr<ListNode>(
        a ? a : b); // 把 std::unique_ptr 小于 ListNode 超过 (数组 ? 数组 : b); 写入 cur->next
    return dummy.next.release(); // 返回 哨兵节点.下一个.release()
}
static std::unique_ptr<ListNode> mergeKLists(std::vector<std::unique_ptr<ListNode>> lists) {
    ListNode *acc = nullptr; // 把 nullptr; 写入 ListNode *acc
    for (auto &l : lists)
        acc = mergeTwo(acc, l.release());  // 逐个取出 lists 的元素（左指针）
    return std::unique_ptr<ListNode>(acc); // 返回 std::unique_ptr 小于 ListNode 超过 (累加器)
}
int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::unique_ptr<ListNode>>
        lists; // std::vector 小于 std::unique_ptr 小于 ListNode 超过 超过 lists;
    lists.push_back(buildList({1, 4, 5})); // lists 追加 buildList({1, 4, 5}));
    lists.push_back(buildList({1, 3, 4})); // lists 追加 buildList({1, 3, 4}));
    lists.push_back(buildList({2, 6}));    // lists 追加 buildList({2, 6}));
    auto got = listToVec(
        mergeKLists(std::move(lists)).get()); // 把 listToVec(mergeKLists(std::move(lists)) 查找 )) 存入 got
    assert((got == std::vector<int>{1, 1, 2, 3, 4, 4, 5, 6}));        // 断言校验
    assert((listToVec(mergeKLists({}).get()) == std::vector<int>{})); // 断言校验
    std::vector<std::unique_ptr<ListNode>>
        emptyLists; // std::vector 小于 std::unique_ptr 小于 ListNode 超过 超过 emptyLists;
    emptyLists.push_back(buildList({})); // emptyLists 追加 buildList({}));
    assert((listToVec(mergeKLists(std::move(emptyLists)).get()) == std::vector<int>{})); // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
