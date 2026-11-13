// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
// LeetCode 110240695. 分治策略之 greatest slice — C++ 版（方案B：增量扫描）
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

static long long max_sub_array_ic(const std::vector<int> &arr) {
    if (arr.empty())
        return 0;                             // 若 数组 是否为空，直接返回 0
    long long gs = arr[0];                    // 把 数组[0] 存入 gs
    for (size_t i = 0; i < arr.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
        long long s = 0;                      // 把 0 存入 字符串
        for (size_t j = i; j < arr.size();
             ++j) {      // 让 下标 j 从 下标 i 开始计数，下标 j 小于 数组.大小() 就继续
            s += arr[j]; // 字符串累加 数组[下标 j]
            if (gs < s)
                gs = s; // 若 gs 小于 字符串) gs 赋值为 字符串;
        }
    }
    return gs; // 返回 gs
}

int main() { // 程序入口：跑内嵌自测用例
    if (max_sub_array_ic({-2, 1, -3, 4, -1, 2, 1}) != 6) {
        std::cout << "ms1 failed" << std::endl;
        return 1;
    }
    if (max_sub_array_ic({-1, -2, -3}) != -1) {
        std::cout << "ms2 failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
