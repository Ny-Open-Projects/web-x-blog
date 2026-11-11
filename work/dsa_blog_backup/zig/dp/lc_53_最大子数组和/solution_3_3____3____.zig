// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130497821
// LeetCode 53. 最大子数组和 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn maxSubArray(nums: []const i32) i32 { // 定义函数/方法 maxSubArray
    var best = nums[0]; // 把 数组[0] 存入 当前最优
    var cur = nums[0]; // 把 数组[0] 存入 当前值
    for (nums[1..]) |v| { // for (数组[1..]) 按位或 值 按位或 {
        cur = @max(cur + v, v); // 把 @取较大值 当前值 加 值, 值); 写入 当前值
        best = @max(best, cur); // 把 @取较大值 当前最优, 当前值); 写入 当前最优
    }
    return best; // 返回 当前最优
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (maxSubArray(&[_]i32{ -2, 1, -3, 4, -1, 2, 1, -5, 4 }) != 6) return error.TestFailed;
    if (maxSubArray(&[_]i32{1}) != 1) return error.TestFailed; // 若 maxSubArray( 按位与 [_]i32{1}) 不等于 1，直接返回 error.TestFailed
    if (maxSubArray(&[_]i32{ 5, 4, -1, 7, 8 }) != 23) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
