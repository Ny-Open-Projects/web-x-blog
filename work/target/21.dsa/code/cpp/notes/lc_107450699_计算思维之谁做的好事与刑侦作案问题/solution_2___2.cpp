// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107450699
// 计算思维之谁做的好事 — C++ 版（方案2）
#include <cassert>                        // 引入头文件
#include <iostream>                       // 引入头文件
static char findGoodMan() {               // 定义函数/方法 findGoodMan
    for (char m : {'A', 'B', 'C', 'D'}) { // for (char 映射表 : {'A', 'B', 'C', 'D'}) {
        int t = 0;                        // 把 0 存入 另一字符串
        if (m != 'A')
            ++t; // 若 映射表 不等于 'A') 加一 另一字符串;
        if (m == 'C')
            ++t; // 若 映射表 等于 'C') 加一 另一字符串;
        if (m == 'D')
            ++t; // 若 映射表 等于 'D') 加一 另一字符串;
        if (m != 'D')
            ++t; // 若 映射表 不等于 'D') 加一 另一字符串;
        if (t == 3)
            return m; // 若 另一字符串 等于 3，直接返回 映射表
    }
    return '?'; // 返回 '?'
}
int main() {
    assert(findGoodMan() == 'C');
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS