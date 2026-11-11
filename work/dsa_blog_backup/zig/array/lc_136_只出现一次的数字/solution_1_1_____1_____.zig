// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133468105
// LeetCode 136. 只出现一次的数字 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn singleNumber(nums: []const i32) i32 {
    var x: i32 = 0;
    for (nums) |v| x ^= v;
    return x;
} // 定义函数/方法 singleNumber
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (singleNumber(&[_]i32{ 2, 2, 1 }) != 1) return error.TestFailed;
    if (singleNumber(&[_]i32{ 4, 1, 2, 1, 2 }) != 4) return error.TestFailed;
    if (singleNumber(&[_]i32{1}) != 1) return error.TestFailed; // 若 singleNumber( 按位与 [_]i32{1}) 不等于 1，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
