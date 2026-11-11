// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130659442
// LeetCode 926. 将字符串翻转到单调递增 — C++ 版（方案2）
#include <algorithm>                                // 引入头文件
#include <cassert>                                  // 引入头文件
#include <iostream>                                 // 引入头文件
#include <string>                                   // 引入头文件
static int minFlipsMonoIncr(const std::string &s) { // 定义函数/方法 minFlipsMonoIncr
    int ones = 0, flips = 0;                        // 把 0, flips 赋值为 0 存入 ones
    for (char c : s) {                              // for (char 字符 : 字符串) {
        if (c == '1')
            ++ones;                        // 若 字符 等于 '1') 加一 ones;
        else {                             // 否则
            ++flips;                       // 加一 flips;
            flips = std::min(flips, ones); // 把 std::取较小值 flips, ones); 写入 flips
        }
    }
    return flips; // 返回 flips
}
int main() {
    assert(minFlipsMonoIncr("00110") == 1);
    assert(minFlipsMonoIncr("010110") == 2);
    assert(minFlipsMonoIncr("00011000") == 2);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS