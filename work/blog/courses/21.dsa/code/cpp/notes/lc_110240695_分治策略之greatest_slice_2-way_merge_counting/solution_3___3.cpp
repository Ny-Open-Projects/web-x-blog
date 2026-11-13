// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
// LeetCode 110240695. 分治策略之 greatest slice — C++ 版（方案C：分治 best/prefix/suffix/total）
#include <algorithm> // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件

struct Quad {                              // 定义类型
    long long best, prefix, suffix, total; // long long 当前最优, prefix, suffix, 总和;
};

static Quad helper(const std::vector<int> &arr, int lo, int hi) { // 定义函数/方法 helper
    if (hi - lo == 1) {                                           // 若 右边界 减 左边界 等于 1
        long long v = arr[lo];                                    // 把 数组[左边界] 存入 值
        return {v, v, v, v};                                      // 返回 {值, 值, 值, 值}
    }
    int mi = lo + (hi - lo) / 2;              // 把 (左边界 加 右边界) 除以 2 存入 mi
    Quad l = helper(arr, lo, mi);             // 把 helper(数组, 左边界, mi); 写入 Quad l
    Quad r = helper(arr, mi, hi);             // 把 helper(数组, mi, 右边界); 写入 Quad r
    long long crossing = l.suffix + r.prefix; // 把 左指针.suffix 加 右指针.prefix 存入 crossing
    Quad q;                                   // Quad 节点;
    q.best =
        std::max({l.best, r.best,
                  crossing}); // 把 std::取较大值 {左指针.当前最优, 右指针.当前最优, crossing}); 写入 当前最优
    q.prefix = std::max(
        l.prefix,
        l.total + r.prefix); // 把 std::取较大值 左指针.prefix, 左指针.总和 加 右指针.prefix); 写入 q.prefix
    q.suffix = std::max(
        r.suffix,
        r.total + l.suffix); // 把 std::取较大值 右指针.suffix, 右指针.总和 加 左指针.suffix); 写入 q.suffix
    q.total = l.total + r.total; // 把 左指针.总和 加 右指针.总和; 写入 总和
    return q;                    // 返回 节点
}

static long long max_sub_array_dc(const std::vector<int> &arr) {
    if (arr.empty())
        return 0; // 若 数组 是否为空，直接返回 0
    return helper(arr, 0, static_cast<int>(arr.size()))
        .best; // 返回 helper(数组, 0, static_cast 小于 int 超过 (数组.大小())).当前最优
}

int main() { // 程序入口：跑内嵌自测用例
    if (max_sub_array_dc({-2, 1, -3, 4, -1, 2, 1}) != 6) {
        std::cout << "ms1 failed" << std::endl;
        return 1;
    }
    if (max_sub_array_dc({1, 2, 3}) != 6) {
        std::cout << "ms2 failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
