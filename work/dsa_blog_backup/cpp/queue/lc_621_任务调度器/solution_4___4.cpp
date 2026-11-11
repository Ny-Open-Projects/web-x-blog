// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
// LeetCode 621. 任务调度器 — C++ 版
#include <algorithm> // 引入头文件
#include <iostream>  // 引入头文件
#include <string>    // 引入头文件
#include <vector>    // 引入头文件

// 方案4（26 位频率桶公式法）
int leastInterval(const std::vector<std::string> &tasks, int n) { // 定义函数/方法 leastInterval
    std::vector<int> freq(26, 0); // std::vector 小于 int 超过 频次表(26, 0);
    for (const auto &t : tasks) { // 逐个取出 tasks 的元素（另一字符串）
        freq[static_cast<size_t>(
            t[0] - 'A')]++; // 频次表[static_cast 小于 size_t 超过 (另一字符串[0] 减 'A')] 加一 ;
    }
    int maxFreq = 0;     // 把 0 存入 maxFreq
    for (int f : freq) { // for (int f : 频次表) {
        if (f > maxFreq)
            maxFreq = f; // 若 f 超过 maxFreq) maxFreq 赋值为 f;
    }
    int same = 0;        // 把 0 存入 same
    for (int f : freq) { // for (int f : 频次表) {
        if (f == maxFreq)
            same++; // 若 f 等于 maxFreq) same 加一 ;
    }
    int formula = (maxFreq - 1) * (n + 1) + same; // 把 (maxFreq 减 1) 乘 (元素个数 加 1) 加 same 存入 formula
    int total = static_cast<int>(tasks.size()); // 把 static_cast 小于 int 超过 (tasks.大小()) 存入 总和
    return std::max(formula, total);            // 返回 std::取较大值 formula, 总和)
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
