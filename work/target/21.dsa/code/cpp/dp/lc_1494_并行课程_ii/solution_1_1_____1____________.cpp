// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134859412
// LeetCode 1494. 并行课程II — C++ 版（方案1）
#include <cassert>               // 引入头文件
#include <iostream>              // 引入头文件
#include <vector>                // 引入头文件
static int nG, kG;               // static int nG, kG;
static std::vector<int> prereqG; // static std::vector 小于 int 超过 prereqG;
static int go(int done) {        // 定义函数/方法 go
    if (done == (1 << nG) - 1)
        return 0;                  // 若 done 等于 (1 小于 小于 nG) 减 1，直接返回 0
    int avail = 0;                 // 把 0 存入 avail
    for (int i = 0; i < nG; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 nG 就继续
        if (!(done & (1 << i)) && (done & prereqG[i]) == prereqG[i])
            avail |= 1 << i;
    }
    int cnt = 0, chosen = 0, a = avail; // 把 0, chosen 赋值为 0, 数组 赋值为 avail 存入 计数
    while (a && cnt < kG) {             // 循环，直到不满足「数组 且 计数 小于 kG」
        int low = a & (-a);             // 把 数组 按位与 ( 减 数组) 存入 low
        chosen |= low;                  // 把 low; 写入 chosen |
        a ^= low;                       // 把 low; 写入 a ^
        ++cnt;                          // 加一 计数;
    }
    return 1 + go(done | chosen); // 返回 1 加 go(done 按位或 chosen)
}
static int minNumberOfSemesters(int n, const std::vector<std::vector<int>> &relations,
                                int k) { // 定义函数/方法 minNumberOfSemesters
    nG = n;                              // 把 元素个数; 写入 nG
    kG = k;                              // 把 下标 k; 写入 kG
    prereqG.assign(n, 0);                // prereqG.assign(元素个数, 0);
    for (const auto &r : relations)
        prereqG[r[1] - 1] |= 1 << (r[0] - 1); // 逐个取出 relations 的元素（右指针）
    return go(0);                             // 返回 go(0)
}
int main() {                                                           // 程序入口：跑内嵌自测用例
    assert(minNumberOfSemesters(4, {{2, 1}, {3, 1}, {1, 4}}, 2) == 3); // 断言校验
    assert(minNumberOfSemesters(5, {{2, 1}, {3, 1}, {4, 1}, {1, 5}}, 3) == 3); // 断言校验
    assert(minNumberOfSemesters(3, {}, 2) == 2);                               // 断言校验
    assert(minNumberOfSemesters(4, {{1, 2}, {2, 3}}, 1) == 4);                 // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS