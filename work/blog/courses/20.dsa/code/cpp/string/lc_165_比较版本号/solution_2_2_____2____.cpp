// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135004886
// LeetCode 165. 比较版本号 — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <cstdlib>  // 引入头文件
#include <iostream> // 引入头文件
#include <string>   // 引入头文件
#include <vector>   // 引入头文件
static int compareVersion(const std::string &version1,
                          const std::string &version2) { // 定义函数/方法 compareVersion
    std::vector<long long> p1, p2;                       // std::vector 小于 long long 超过 p1, p2;
    size_t start = 0;                                    // 把 0; 写入 size_t start
    for (size_t i = 0; i <= version1.size();
         ++i) { // 让 下标 i 从 0 开始计数，下标 i 不超过 version1.大小() 就继续
        if (i == version1.size() ||
            version1[i] == '.') { // 若 下标 i 等于 version1.大小() 或 version1[下标 i] 等于 '.'
            p1.push_back(std::atoll(
                version1.substr(start, i - start)
                    .c_str())); // p1 追加 std::atoll(version1 截取 起点, 下标 i 减 起点).c_str()));
            start = i + 1;      // 把 下标 i 加 1; 写入 起点
        }
    }
    start = 0; // 把 0; 写入 起点
    for (size_t i = 0; i <= version2.size();
         ++i) { // 让 下标 i 从 0 开始计数，下标 i 不超过 version2.大小() 就继续
        if (i == version2.size() ||
            version2[i] == '.') { // 若 下标 i 等于 version2.大小() 或 version2[下标 i] 等于 '.'
            p2.push_back(std::atoll(
                version2.substr(start, i - start)
                    .c_str())); // p2 追加 std::atoll(version2 截取 起点, 下标 i 减 起点).c_str()));
            start = i + 1;      // 把 下标 i 加 1; 写入 起点
        }
    }
    size_t n = std::max(p1.size(), p2.size()); // 把 std::取较大值 p1.大小(), p2.大小()); 写入 size_t n
    for (size_t i = 0; i < n; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        long long a = i < p1.size() ? p1[i] : 0; // 把 下标 i 小于 p1.大小() ? p1[下标 i] : 0 存入 数组
        long long b = i < p2.size() ? p2[i] : 0; // 把 下标 i 小于 p2.大小() ? p2[下标 i] : 0 存入 b
        if (a < b)
            return -1; // 若 数组 小于 b，直接返回 减 1
        if (a > b)
            return 1; // 若 数组 超过 b，直接返回 1
    }
    return 0; // 返回 0
}
int main() {                                      // 程序入口：跑内嵌自测用例
    assert(compareVersion("1.01", "1.001") == 0); // 断言校验
    assert(compareVersion("1.0", "1.0.0") == 0);  // 断言校验
    assert(compareVersion("0.1", "1.1") == -1);   // 断言校验
    std::cout << "PASS" << std::endl;             // 全部用例通过，输出 PASS
    return 0;                                     // 返回 0
}
