// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237
// 数据结构与算法之排序: 冒泡排序 — Zig 版（方案5）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn gnomeSortBubble(nums: []i32) void { // 定义函数/方法 gnomeSortBubble
    const n = nums.len; // 把 数组.长度 存入 元素个数
    for (0..n) |i| { // 让 下标 i 从 0 走到 元素个数 减一
        for (0..n - 1 - i) |j| { // for (0..元素个数 减 1 减 下标 i) 按位或 下标 j 按位或 {
            if (nums[j] > nums[j + 1]) { // 若 数组[下标 j] 超过 数组[下标 j 加 1]
                const t = nums[j]; // 把 数组[下标 j] 存入 另一字符串
                nums[j] = nums[j + 1]; // 把 数组[下标 j 加 1]; 写入 nums[j]
                nums[j + 1] = t; // 把 另一字符串; 写入 nums[j + 1]
            }
        }
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var v1 = [_]i32{ 5, 4, 3, 2, 1 }; // 把 [_]i32{ 5, 4, 3, 2, 1 } 存入 v1
    gnomeSortBubble(&v1); // gnomeSortBubble( 按位与 v1);
    if (v1[0] != 1 or v1[4] != 5) return error.TestFailed; // 若 v1[0] 不等于 1 or v1[4] 不等于 5，直接返回 error.TestFailed
    var v2 = [_]i32{ 3, 1, 2 }; // 把 [_]i32{ 3, 1, 2 } 存入 v2
    gnomeSortBubble(&v2); // gnomeSortBubble( 按位与 v2);
    if (v2[0] != 1 or v2[2] != 3) return error.TestFailed; // 若 v2[0] 不等于 1 or v2[2] 不等于 3，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
