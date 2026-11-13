// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
// LeetCode 107431726. 最大红矩形分析 — C++ 版（方案C：逐行高度 + 单调栈）
#include <iostream> // 引入头文件
#include <string>   // 引入头文件
#include <vector>   // 引入头文件

static long long max_red_rectangle(const std::vector<std::string> &matrix) {
    size_t n = matrix.size();                // 把 矩阵.大小(); 写入 size_t n
    size_t m = matrix[0].size();             // 把 矩阵[0].大小(); 写入 size_t m
    long long ans = 0;                       // 把 0 存入 答案
    std::vector<long long> height(m + 2, 0); // std::vector 小于 long long 超过 height(映射表 加 2, 0);
    for (size_t k = 0; k < n; ++k) { // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
        for (size_t i = 1; i <= m; ++i) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
            if (matrix[k][i - 1] == '.')
                ++height[i];
            else
                height[i] = 0;
        }
        std::vector<size_t> stack{0}; // std::vector 小于 size_t 超过 栈{0};
        for (size_t i = 1; i <= m + 1; ++i) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 加 1 就继续
            long long hi =
                (i <= m) ? height[i] : 0; // 把 (下标 i 不超过 映射表) ? height[下标 i] : 0 存入 右边界
            while (height[stack.back()] > hi) { // 循环，直到不满足「height[栈.back()] 超过 右边界」
                long long now_h = height[stack.back()]; // 把 height[栈.back()] 存入 now_h
                stack.pop_back();                       // 弹出栈顶元素
                long long width = static_cast<long long>(
                    i - stack.back() -
                    1); // 把 static_cast 小于 long long 超过 (下标 i 减 栈.back() 减 1) 存入 width
                long long area = now_h * width; // 把 now_h 乘 width 存入 area
                if (area > ans)
                    ans = area; // 若 area 超过 答案) 答案 赋值为 area;
            }
            stack.push_back(i); // 栈 追加 下标 i);
        }
    }
    return ans; // 返回 答案
}

int main() { // 程序入口：跑内嵌自测用例
    std::vector<std::string> matrix = {".....", "XXXXX", ".X...", "....."};
    if (max_red_rectangle(matrix) != 6) {
        std::cout << "mono failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
