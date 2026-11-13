// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134859971
// LeetCode 2050. 并行课程III — C++ 版（方案2）
#include <algorithm>     // 引入头文件
#include <cassert>       // 引入头文件
#include <iostream>      // 引入头文件
#include <unordered_map> // 引入头文件
#include <vector>        // 引入头文件
static int minimumTime(int n, const std::vector<std::vector<int>> &relations,
                       const std::vector<int> &time) { // 定义函数/方法 minimumTime
    std::unordered_map<int, std::vector<int>>
        next; // std::unordered_map 小于 int, std::vector 小于 int 超过 超过 下一个;
    std::vector<int> indeg(n + 1, 0); // std::vector 小于 int 超过 indeg(元素个数 加 1, 0);
    for (const auto &r : relations) { // 逐个取出 relations 的元素（右指针）
        next[r[0]].push_back(r[1]);   // 下一个[右指针[0]] 追加 右指针[1]);
        indeg[r[1]]++;                // indeg[右指针[1]] 加一 ;
    }
    std::vector<int> finish(n + 1, 0); // std::vector 小于 int 超过 finish(元素个数 加 1, 0);
    std::vector<int> queue;            // std::vector 小于 int 超过 队列;
    for (int c = 1; c <= n; ++c)
        if (indeg[c] == 0)
            queue.push_back(c); // 让 字符 从 1 开始计数，字符 不超过 元素个数 就继续
    int total = 0;              // 把 0 存入 总和
    while (!queue.empty()) {    // 循环，直到不满足「取反 队列.empty(」
        std::vector<int> nq;    // std::vector 小于 int 超过 nq;
        for (int c : queue) {   // for (int 字符 : 队列) {
            finish[c] += time[c - 1];           // finish[c]累加 time[字符 减 1]
            total = std::max(total, finish[c]); // 把 std::取较大值 总和, finish[字符]); 写入 总和
            for (int nx : next[c]) {            // for (int nx : 下一个[字符]) {
                finish[nx] = std::max(
                    finish[nx], finish[c]); // 把 std::取较大值 finish[nx], finish[字符]); 写入 finish[nx]
                if (--indeg[nx] == 0)
                    nq.push_back(nx); // 若 减一 indeg[nx] 等于 0) nq 追加 nx);
            }
        }
        queue = std::move(nq); // 把 std::move(nq); 写入 队列
    }
    return total; // 返回 总和
}
int main() {                                                  // 程序入口：跑内嵌自测用例
    assert(minimumTime(3, {{1, 3}, {2, 3}}, {3, 2, 5}) == 8); // 断言校验
    assert(minimumTime(5, {{1, 2}, {2, 3}, {3, 4}, {4, 5}}, {1, 2, 3, 4, 5}) == 15); // 断言校验
    assert(minimumTime(1, {}, {5}) == 5);                                            // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS