// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
// LeetCode 621. 任务调度器 — C++ 版
#include <algorithm>  // 引入头文件
#include <functional> // 引入头文件
#include <iostream>   // 引入头文件
#include <map>        // 引入头文件
#include <string>     // 引入头文件
#include <vector>     // 引入头文件

// 方案3（贪心模拟，每轮取剩余次数最多的 n+1 个，最后一轮只计实际执行数）
int leastInterval(const std::vector<std::string> &tasks, int n) { // 定义函数/方法 leastInterval
    std::map<std::string, int> count; // std::映射表 小于 std::string, int 超过 计数;
    for (const auto &t : tasks)
        count[t]++;       // 逐个取出 tasks 的元素（另一字符串）
    std::vector<int> cnt; // std::vector 小于 int 超过 计数;
    for (const auto &kv : count)
        cnt.push_back(kv.second); // 逐个取出 计数 的元素（kv）
    int time = 0;                 // 把 0 存入 time
    while (!cnt.empty()) {        // 循环，直到不满足「取反 计数.empty(」
        std::sort(
            cnt.begin(), cnt.end(),
            std::greater<int>()); // std::sort(计数 迭代位置 , 计数.终点(), std::greater 小于 int 超过 ());
        int used = 0;             // 把 0 存入 已用标记
        int take = std::min(n + 1, static_cast<int>(cnt.size()));
        for (int i = 0; i < take; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 take 就继续
            if (cnt[i] > 0) {            // 若 计数[下标 i] 超过 0
                cnt[i] -= 1;             // cnt[i]累减 1
                ++used;                  // 加一 已用标记;
            }
        }
        cnt.erase(std::remove_if(cnt.begin(), cnt.end(), [](int c) { return c <= 0; }), cnt.end());
        time += !cnt.empty() ? n + 1 : used; // time累加 取反 计数 是否为空 ? 元素个数 加 1 : 已用标记
    }
    return time; // 返回 time
}

int main() { // 程序入口：跑内嵌自测用例
    // 与 TS 事实源内嵌用例一致
    std::vector<std::vector<std::string>> taskCases = {
        // 把 { 写入 std::vector<std::vector<std::string>> taskCases
        {"A", "A", "A", "B", "B", "B"},
        {"A", "A", "A", "A"},
        {"A", "B", "C", "D"},
    };
    std::vector<int> ns = {2, 2, 0};     // 把 { 2, 2, 0 }; 写入 std::vector<int> ns
    std::vector<int> wants = {8, 10, 4}; // 把 { 8, 10, 4 }; 写入 std::vector<int> wants
    for (size_t i = 0; i < taskCases.size();
         ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 taskCases.大小() 就继续
        int got =
            leastInterval(taskCases[i], ns[i]); // 把 leastInterval(taskCases[下标 i], ns[下标 i]) 存入 got
        if (got != wants[i]) {                  // 若 got 不等于 wants[下标 i]
            std::cout << "FAIL case " << i << " got " << got << " want " << wants[i] << std::endl; // 打印输出
            return 1;                                                                              // 返回 1
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
