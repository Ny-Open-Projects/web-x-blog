// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130663853
// LeetCode 1. 两数之和 — Zig 版（方案1：暴力双循环）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn twoSum(nums: []const i32, target: i32, out: *[2]i32) usize { // 定义函数/方法 twoSum
    for (nums, 0..) |a, i| { // for (数组, 0..) 按位或 数组, 下标 i 按位或 {
        for (nums[i + 1 ..], i + 1..) |b, j| { // for (数组[下标 i 加 1 ..], 下标 i 加 1..) 按位或 b, 下标 j 按位或 {
            if (a + b == target) { // 若 数组 加 b 等于 目标值
                out[0] = @intCast(i); // 把 @intCast(下标 i); 写入 out[0]
                out[1] = @intCast(j); // 把 @intCast(下标 j); 写入 out[1]
                return 2; // 返回 2
            }
        }
    }
    return 0; // 返回 0
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out: [2]i32 = undefined; // 把 undefined; 写入 var out: [2]i32
    if (twoSum(&[_]i32{ 2, 7, 11, 15 }, 9, &out) != 2 or out[0] != 0 or out[1] != 1) return error.TestFailed;
    if (twoSum(&[_]i32{ 3, 2, 4 }, 6, &out) != 2 or out[0] != 1 or out[1] != 2) return error.TestFailed;
    if (twoSum(&[_]i32{ 3, 3 }, 6, &out) != 2 or out[0] != 0 or out[1] != 1) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
