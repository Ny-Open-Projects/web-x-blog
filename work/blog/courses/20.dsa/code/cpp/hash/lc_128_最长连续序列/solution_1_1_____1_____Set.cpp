// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135167108
// LeetCode 128. 最长连续序列 — C++ 版（方案1）
#include <cassert>                                            // 引入头文件
#include <iostream>                                           // 引入头文件
#include <unordered_set>                                      // 引入头文件
#include <vector>                                             // 引入头文件
static int longestConsecutive(const std::vector<int> &nums) { // 定义函数/方法 longestConsecutive
    std::unordered_set<int> set(
        nums.begin(), nums.end()); // std::unordered_set 小于 int 超过 set(数组 迭代位置 , 数组.终点());
    int best = 0;                  // 把 0 存入 当前最优
    for (int num : set) {          // for (int num : set) {
        if (set.count(num - 1))
            continue;              // 若 set.计数(num 减 1)) continue;
        int cur = num, streak = 1; // 把 num, streak 赋值为 1 存入 当前值
        while (set.count(cur + 1)) {
            ++cur;
            ++streak;
        } // 循环，直到不满足「set.计数(当前值 加 1)) { 加一 当前值; 加一 streak; }」
        best = std::max(best, streak); // 把 std::取较大值 当前最优, streak); 写入 当前最优
    }
    return best; // 返回 当前最优
}
int main() {                                                         // 程序入口：跑内嵌自测用例
    assert(longestConsecutive({100, 4, 200, 1, 3, 2}) == 4);         // 断言校验
    assert(longestConsecutive({0, 3, 7, 2, 5, 8, 4, 6, 0, 1}) == 9); // 断言校验
    assert(longestConsecutive({}) == 0);                             // 断言校验
    std::cout << "PASS" << std::endl;                                // 全部用例通过，输出 PASS
    return 0;                                                        // 返回 0
}
