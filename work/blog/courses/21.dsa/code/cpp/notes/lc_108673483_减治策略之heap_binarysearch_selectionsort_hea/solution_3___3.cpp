// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
// LeetCode 108673483. 减治策略 — C++ 版（方案3：Boyer-Moore 摩尔投票求多数元素）
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

static int majority_element(const std::vector<int> &arr) { // 定义函数/方法 majority_element
    int candidate = 0;                                     // 把 0 存入 candidate
    int count = 0;                                         // 把 0 存入 计数
    for (int num : arr) {                                  // for (int num : 数组) {
        if (count == 0)
            candidate = num; // 若 计数 等于 0) candidate 赋值为 num;
        if (num == candidate)
            ++count; // 若 num 等于 candidate) 加一 计数;
        else
            --count; // 否则
    }
    int cnt = 0; // 把 0 存入 计数
    for (int num : arr)
        if (num == candidate)
            ++cnt; // 把 赋值为 candidate) 加一 计数; 写入 for (int num : arr) if (num
    if (cnt > static_cast<int>(arr.size()) / 2)
        return candidate; // 若 计数 超过 static_cast 小于 int 超过 (数组.大小()) 除以 2，直接返回 candidate
    return -1; // 返回 减 1
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::vector<int>> as = {
        // 把 { 写入 std::vector<std::vector<int>> as
        {2, 2, 1, 1, 1, 1, 1},
        {1, 2, 3},
        {3, 3, 4},
    };
    int ws[3] = {1, -1, 3};                // 把 {1, 减 1, 3}; 写入 int ws[3]
    for (int i = 0; i < 3; ++i) {          // 让 下标 i 从 0 开始计数，下标 i 小于 3 就继续
        int got = majority_element(as[i]); // 把 majority_element(as[下标 i]) 存入 got
        if (got != ws[i]) {
            std::cout << "case " << i << " failed" << std::endl;
            return 1;
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
