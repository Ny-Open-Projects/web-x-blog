// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
// LeetCode 107431726. 最大红矩形分析 — C++ 版（方案A：逐行高度 + 暴力区间 / 卡片扩展）
#include <iostream> // 引入头文件
#include <string>   // 引入头文件
#include <vector>   // 引入头文件

static long long get_result(int n, int m, const std::vector<std::string> &matrix) {
    long long ans = 0;                       // 把 0 存入 答案
    std::vector<long long> height(m + 2, 0); // std::vector 小于 long long 超过 height(映射表 加 2, 0);
    for (int k = 0; k < n; ++k) { // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
        for (int i = 1; i <= m; ++i) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
            if (matrix[k][i - 1] == '.')
                ++height[i];
            else
                height[i] = 0;
        }
        for (int a = 1; a <= m; ++a) { // 让 数组 从 1 开始计数，数组 不超过 映射表 就继续
            long long min_h = 50000;   // 把 50000 存入 min_h
            for (int c = a; c <= m; ++c)
                if (height[c] < min_h)
                    min_h = height[c]; // 让 字符 从 数组 开始计数，字符 不超过 映射表 就继续
            long long area =
                static_cast<long long>(m - a + 1) *
                min_h; // 把 static_cast 小于 long long 超过 (映射表 减 数组 加 1) 乘 min_h 存入 area
            if (area > ans)
                ans = area; // 若 area 超过 答案) 答案 赋值为 area;
        }
    }
    return ans; // 返回 答案
}

static long long get_result_card(int n, int m, const std::vector<std::string> &matrix) {
    long long ans = 0;                       // 把 0 存入 答案
    std::vector<long long> height(m + 2, 0); // std::vector 小于 long long 超过 height(映射表 加 2, 0);
    for (int k = 0; k < n; ++k) { // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
        for (int i = 1; i <= m; ++i) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
            if (matrix[k][i - 1] == '.')
                ++height[i];
            else
                height[i] = 0;
        }
        for (int a = 1; a <= m; ++a) { // 让 数组 从 1 开始计数，数组 不超过 映射表 就继续
            long long cur_h = height[a]; // 把 height[数组] 存入 cur_h
            long long lo = a - 1;        // 把 数组 减 1 存入 左边界
            while (lo >= 1 && height[lo] >= cur_h)
                --lo; // 循环，直到不满足「左边界 不低于 1 且 height[左边界] 不低于 cur_h) 减一 左边界;」
            long long hi = a + 1; // 把 数组 加 1 存入 右边界
            while (hi <= m && height[hi] >= cur_h)
                ++hi; // 循环，直到不满足「右边界 不超过 映射表 且 height[右边界] 不低于 cur_h) 加一 右边界;」
            long long area = (hi - lo - 1) * cur_h; // 把 (右边界 减 左边界 减 1) 乘 cur_h 存入 area
            if (area > ans)
                ans = area; // 若 area 超过 答案) 答案 赋值为 area;
        }
    }
    return ans; // 返回 答案
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::string> matrix = {".....", "XXXXX", ".X...", "....."};
    if (get_result(4, 5, matrix) != 6) {
        std::cout << "brute failed" << std::endl;
        return 1;
    }
    if (get_result_card(4, 5, matrix) != 6) {
        std::cout << "card failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
