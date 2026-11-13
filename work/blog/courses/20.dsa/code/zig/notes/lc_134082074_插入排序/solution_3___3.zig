// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134082074
// 数据结构与算法之排序: 插入排序 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn insertionSort(nums: []i32) void { // 定义函数/方法 insertionSort
    for (1..nums.len) |i| { // 逐个取出 1..数组.长度 的元素（下标 i）
        const key = nums[i]; // 把 数组[下标 i] 存入 key
        var j = i; // 把 下标 i 存入 下标 j
        while (j > 0 and nums[j - 1] > key) { // 循环，直到不满足「下标 j 超过 0 and 数组[下标 j 减 1] 超过 key」
            nums[j] = nums[j - 1]; // 把 数组[下标 j 减 1]; 写入 nums[j]
            j -= 1; // 下标 j累减 1
        }
        nums[j] = key; // 把 key; 写入 nums[j]
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var v1 = [_]i32{ 5, 4, 3, 2, 1 }; // 把 [_]i32{ 5, 4, 3, 2, 1 } 存入 v1
    insertionSort(&v1); // insertionSort( 按位与 v1);
    if (v1[0] != 1 or v1[4] != 5) return error.TestFailed; // 若 v1[0] 不等于 1 or v1[4] 不等于 5，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
