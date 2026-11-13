// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114454
// LeetCode 26. 删除有序数组中的重复项 — C++ 版
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

// 方案2：快慢指针 —— fast 扫描，slow 指向已去重区间末尾
size_t removeDuplicates(std::vector<int> &nums) { // 定义函数/方法 removeDuplicates
    if (nums.empty())
        return 0;    // 若 数组 是否为空，直接返回 0
    size_t slow = 0; // 把 0; 写入 size_t slow
    for (size_t fast = 1; fast < nums.size();
         ++fast) { // 让 快指针 从 1 开始计数，快指针 小于 数组.大小() 就继续
        if (nums[fast] != nums[slow]) { // 若 数组[快指针] 不等于 数组[慢指针]
            ++slow;                     // 加一 慢指针;
            nums[slow] = nums[fast];    // 把 数组[快指针]; 写入 nums[slow]
        }
    }
    return slow + 1; // 返回 慢指针 加 1
}

int main() { // 程序入口：跑内嵌自测用例
    // 与 TS 事实源内嵌用例一致
    struct Case {             // 定义类型
        std::vector<int> in;  // std::vector 小于 int 超过 in;
        size_t k;             // size_t 下标 k;
        std::vector<int> pre; // std::vector 小于 int 超过 前缀和;
    };
    std::vector<Case> cases = {
        // 把 { 写入 std::vector<Case> cases
        {{1, 1, 2}, 2, {1, 2}},
        {{1, 2, 3}, 3, {1, 2, 3}},
        {{}, 0, {}},
    };
    for (const auto &c : cases) {            // 逐个取出 cases 的元素（字符）
        std::vector<int> nums = c.in;        // 把 字符.in; 写入 std::vector<int> nums
        size_t got = removeDuplicates(nums); // 把 removeDuplicates(数组); 写入 size_t got
        std::vector<int> prefix(nums.begin(), nums.begin() + static_cast<std::ptrdiff_t>(got));
        if (got != c.k || prefix != c.pre) { // 若 got 不等于 字符.下标 k 或 prefix 不等于 字符.前缀和
            std::cout << "FAILED case k=" << got << std::endl; // 打印输出
            return 1;                                          // 返回 1
        }
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
