// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975
// LeetCode 922. 按奇偶排序数组II — C++ 版（方案9）
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件
static std::vector<int> sortArrayByParityII(std::vector<int> nums) {
    std::sort(nums.begin(), nums.end()); // std::sort(数组 迭代位置 , 数组.终点());
    std::vector<int> res(nums.size());   // std::vector 小于 int 超过 结果(数组.大小());
    int odd = 1, even = 0;               // 把 1, even 赋值为 0 存入 odd
    for (int item : nums) {              // for (int item : 数组) {
        if (item % 2 != 0) {
            res[odd] = item;
            odd += 2;
        } // 若 item 对…取模 2 不等于 0) { 结果[odd] 赋值为 item; odd 累加 2; }
        else {
            res[even] = item;
            even += 2;
        } // 否则
    }
    return res; // 返回 结果
}
int main() { // 程序入口：跑内嵌自测用例
    assert((sortArrayByParityII({4, 2, 5, 7}) == std::vector<int>{2, 5, 4, 7})); // 断言校验
    assert((sortArrayByParityII({2, 3}) == std::vector<int>{2, 3}));             // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
