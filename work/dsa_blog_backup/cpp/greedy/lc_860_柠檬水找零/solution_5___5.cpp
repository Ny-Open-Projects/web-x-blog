// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135167617
// LeetCode 860. 柠檬水找零 — C++ 版（方案5）
#include <cassert>                                          // 引入头文件
#include <iostream>                                         // 引入头文件
#include <vector>                                           // 引入头文件
static bool lemonadeChange(const std::vector<int> &bills) { // 定义函数/方法 lemonadeChange
    int f5 = 0, f10 = 0;                                    // 把 0, f10 赋值为 0 存入 f5
    for (int b : bills) {                                   // for (int b : bills) {
        if (b == 5)
            ++f5; // 若 b 等于 5) 加一 f5;
        else if (b == 10) {
            ++f10;
            --f5;
        }      // 否则，若 b 等于 10) { 加一 f10; 减一 f5; }
        else { // 否则
            if (f10 > 0) {
                --f10;
                --f5;
            } // 若 f10 超过 0) { 减一 f10; 减一 f5; }
            else
                f5 -= 3; // 否则
        }
        if (f5 < 0)
            return false; // 若 f5 小于 0，直接返回 false
    }
    return true; // 返回 true
}
int main() {                                     // 程序入口：跑内嵌自测用例
    assert(lemonadeChange({5, 5, 5, 10, 20}));   // 断言校验
    assert(!lemonadeChange({5, 5, 10, 10, 20})); // 断言校验
    assert(lemonadeChange({5, 5, 5, 5, 20}));    // 断言校验
    std::cout << "PASS" << std::endl;            // 全部用例通过，输出 PASS
    return 0;                                    // 返回 0
}
