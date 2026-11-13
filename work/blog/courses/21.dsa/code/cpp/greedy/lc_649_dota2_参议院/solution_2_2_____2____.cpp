// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138684407
// LeetCode 649. Dota2参议院 — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <deque>    // 引入头文件
#include <iostream> // 引入头文件
#include <string>   // 引入头文件
static std::string predictPartyVictory(const std::string &senate) {
    int n = static_cast<int>(senate.size()); // 把 static_cast 小于 int 超过 (senate.大小()) 存入 元素个数
    std::deque<int> radiant, dire;           // std::deque 小于 int 超过 radiant, dire;
    for (int i = 0; i < n; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        if (senate[i] == 'R')
            radiant.push_back(i); // 若 senate[下标 i] 等于 'R') radiant 追加 下标 i);
        else
            dire.push_back(i); // 否则
    }
    while (!radiant.empty() &&
           !dire.empty()) { // 循环，直到不满足「取反 radiant 是否为空 且 取反 dire.empty(」
        int r = radiant.front(); // 把 radiant.front() 存入 右指针
        radiant.pop_front();     // radiant.pop_front();
        int d = dire.front();    // 把 dire.front() 存入 d
        dire.pop_front();        // dire.pop_front();
        if (r < d)
            radiant.push_back(r + n); // 若 右指针 小于 d) radiant 追加 右指针 加 元素个数);
        else
            dire.push_back(d + n); // 否则
    }
    return radiant.empty() ? "Dire" : "Radiant"; // 返回 radiant 是否为空 ? 「Dire」 : 「Dire」
}
int main() {                                        // 程序入口：跑内嵌自测用例
    assert(predictPartyVictory("RD") == "Radiant"); // 断言校验
    assert(predictPartyVictory("DDR") == "Dire");   // 断言校验
    std::cout << "PASS" << std::endl;               // 全部用例通过，输出 PASS
    return 0;                                       // 返回 0
}
