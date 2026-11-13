// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355207
// LeetCode LCR 152. 验证二叉搜索树的后序遍历序列 — C++ 版（方案1）
#include <cassert>                                               // 引入头文件
#include <iostream>                                              // 引入头文件
#include <vector>                                                // 引入头文件
static bool check(const std::vector<int> &seq, int lo, int hi) { // 定义判定函数 check
    if (hi - lo <= 1)
        return true;    // 若 右边界 减 左边界 不超过 1，直接返回 true
    int root = seq[hi]; // 把 seq[右边界] 存入 根节点
    int i = lo;         // 把 左边界 存入 下标 i
    while (i < hi && seq[i] < root)
        ++i; // 循环，直到不满足「下标 i 小于 右边界 且 seq[下标 i] 小于 根节点) 加一 下标 i;」
    for (int j = i; j < hi; ++j) { // 让 下标 j 从 下标 i 开始计数，下标 j 小于 右边界 就继续
        if (seq[j] < root)
            return false; // 若 seq[下标 j] 小于 根节点，直接返回 false
    }
    return check(seq, lo, i - 1) &&
           check(seq, i, hi - 1); // 返回 check(seq, 左边界, 下标 i 减 1) 且 check(seq, 下标 i, 右边界 减 1)
}
static bool verifyPostorder(const std::vector<int> &postorder) { // 定义函数/方法 verifyPostorder
    return check(postorder, 0, static_cast<int>(postorder.size()) - 1);
}
int main() {                                     // 程序入口：跑内嵌自测用例
    assert(!verifyPostorder({1, 6, 3, 2, 5}));   // 断言校验
    assert(verifyPostorder({1, 3, 2, 4, 5}));    // 断言校验
    assert(verifyPostorder({4, 6, 5, 9, 8, 7})); // 断言校验
    assert(verifyPostorder({1, 2, 3}));          // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS