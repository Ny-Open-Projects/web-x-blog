// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134283831
// LeetCode 23. 合并K个升序链表 — C++ 版（方案5）
#include <cassert>                    // 引入头文件
#include <iostream>                   // 引入头文件
#include <vector>                     // 引入头文件
struct LNode {                        // 定义类型
    int val;                          // int 值;
    LNode *next = nullptr;            // 把 nullptr; 写入 LNode *next
    explicit LNode(int v) : val(v) {} // explicit LNode(int 值) : 值(值) {}
};
static LNode *buildList(const std::vector<int> &vals) {
    LNode dummy(0);               // LNode 哨兵节点(0);
    LNode *cur = &dummy;          // 把 按位与 哨兵节点; 写入 LNode *cur
    for (int v : vals) {          // for (int 值 : vals) {
        cur->next = new LNode(v); // 把 new LNode(值); 写入 cur->next
        cur = cur->next;          // 把 当前值 减 超过 下一个; 写入 当前值
    }
    return dummy.next; // 返回 哨兵节点.下一个
}
static void freeList(LNode *h) { // 定义函数/方法 freeList
    while (h) {
        LNode *n = h->next;
        delete h;
        h = n;
    }
}
static std::vector<int>
listToVec(LNode *head) {  // static std::vector 小于 int 超过 listToVec(LNode 乘 头节点) {
    std::vector<int> out; // std::vector 小于 int 超过 out;
    while (head) {
        out.push_back(head->val);
        head = head->next;
    } // 循环，直到不满足「头节点) { out 追加 头节点 减 超过 值); 头节点 赋值为 头节点 减 超过 下一个; }」
    return out; // 返回 out
}
static LNode *mergeKLists(std::vector<LNode *> &lists) {
    LNode dummy(0);       // LNode 哨兵节点(0);
    LNode *tail = &dummy; // 把 按位与 哨兵节点; 写入 LNode *tail
    while (true) {        // 循环，直到不满足「true」
        int bestI = -1;   // 把 减 1 存入 bestI
        for (size_t i = 0; i < lists.size();
             ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 lists.大小() 就继续
            if (lists[i] && (bestI < 0 || lists[i]->val < lists[bestI]->val))
                bestI = static_cast<int>(i);
        }
        if (bestI < 0)
            break;                         // 若 bestI 小于 0) break;
        tail->next = lists[bestI];         // 把 lists[bestI]; 写入 tail->next
        lists[bestI] = lists[bestI]->next; // 把 lists[bestI] 减 超过 下一个; 写入 lists[bestI]
        tail = tail->next;                 // 把 尾节点 减 超过 下一个; 写入 尾节点
    }
    return dummy.next; // 返回 哨兵节点.下一个
}
int main() { // 程序入口：跑内嵌自测用例
    std::vector<LNode *> lists = {buildList({1, 4, 5}), buildList({1, 3, 4}), buildList({2, 6})};
    LNode *got = mergeKLists(lists); // 把 mergeKLists(lists); 写入 LNode *got
    assert((listToVec(got) == std::vector<int>{1, 1, 2, 3, 4, 4, 5, 6})); // 断言校验
    freeList(got);                                                        // freeList(got);
    std::vector<LNode *> emptyLists;            // std::vector 小于 LNode 乘 超过 emptyLists;
    assert(mergeKLists(emptyLists) == nullptr); // 断言校验
    std::cout << "PASS" << std::endl;           // 全部用例通过，输出 PASS
    return 0;                                   // 返回 0
}
