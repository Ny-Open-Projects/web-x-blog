// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137060905
// LeetCode 451. 根据字符出现频率排序 — C++ 版（方案5）
#include <algorithm>     // 引入头文件
#include <cassert>       // 引入头文件
#include <iostream>      // 引入头文件
#include <string>        // 引入头文件
#include <unordered_map> // 引入头文件
#include <vector>        // 引入头文件
static std::string frequencySort(const std::string &s) {
    std::unordered_map<char, long long> counts; // std::unordered_map 小于 char, long long 超过 counts;
    std::unordered_map<char, size_t> firstIdx;  // std::unordered_map 小于 char, size_t 超过 firstIdx;
    for (size_t i = 0; i < s.size(); ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 字符串.大小() 就继续
        ++counts[s[i]];                     // 加一 counts[字符串[下标 i]];
        firstIdx.emplace(s[i], i); // firstIdx.emplace(字符串[下标 i], 下标 i);
    }
    std::vector<std::pair<char, std::pair<long long, size_t>>> items;
    for (auto &[c, n] : counts)
        items.emplace_back(c, std::make_pair(n, firstIdx[c]));
    std::sort(items.begin(), items.end(), [](auto &a, auto &b) {
        if (a.second.first != b.second.first)
            return a.second.first > b.second.first;
        return a.second.second < b.second.second; // 返回 数组.second.second 小于 b.second.second
    });                                           // });
    std::string res;                              // std::string 结果;
    for (auto &[c, p] : items)
        res.append(static_cast<size_t>(p.first),
                   c); // 把 static_cast 小于 size_t 超过 (节点.first 追加到列表尾部
    return res;        // 返回 结果
}
int main() {                                     // 程序入口：跑内嵌自测用例
    assert(frequencySort("tree") == "eetr");     // 断言校验
    assert(frequencySort("") == "");             // 断言校验
    assert(frequencySort("cccaaa") == "cccaaa"); // 断言校验
    std::cout << "PASS" << std::endl;            // 全部用例通过，输出 PASS
    return 0;                                    // 返回 0
}
