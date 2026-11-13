// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145238093
// LeetCode 374. 猜数字大小 — C++ 版（方案3：迭代二分）
#include <cassert>           // 引入头文件
#include <iostream>          // 引入头文件
static long pick_v = 6;      // 把 6; 写入 static long pick_v
static int guess(long num) { // 定义函数/方法 guess
    if (num == pick_v)
        return 0;                 // 若 num 等于 pick_v，直接返回 0
    return num < pick_v ? 1 : -1; // 返回 num 小于 pick_v ? 1 : 减 1
}
static long guessNumber(long n) {          // 定义函数/方法 guessNumber
    long low = 1, high = n;                // 把 1, high 赋值为 元素个数; 写入 long low
    while (low <= high) {                  // 循环，直到不满足「low 不超过 high」
        long mid = low + (high - low) / 2; // 把 low 加 (high 减 low) 除以 2; 写入 long mid
        int res = guess(mid);              // 把 guess(中点) 存入 结果
        if (res == 0)
            return mid; // 若 结果 等于 0，直接返回 中点
        if (res == 1)
            low = mid + 1;
        else
            high = mid - 1; // 若 结果 等于 1) low 赋值为 中点 加 1; else high 赋值为 中点 减 1;
    }
    return -1; // 返回 减 1
}
int main() { // 程序入口：跑内嵌自测用例
    long cs[4][2] = {
        {10, 6}, {1, 1}, {5, 3}, {2, 2}};  // 把 {{10, 6}, {1, 1}, {5, 3}, {2, 2}}; 写入 long cs[4][2]
    for (auto &c : cs) {                   // 逐个取出 cs 的元素（字符）
        pick_v = c[1];                     // 把 字符[1]; 写入 pick_v
        assert(guessNumber(c[0]) == c[1]); // 断言校验
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
}
