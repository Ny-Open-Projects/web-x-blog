// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130644389
// LeetCode 198. 打家劫舍 — Zig 版（方案8）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn rob(nums: []const i32) i32 {
    var a: i32 = 0;
    var b: i32 = 0;
    for (nums) |v| {
        const t = @max(b, a + v);
        a = b;
        b = t;
    }
    return b;
} // 定义函数/方法 rob
pub fn main() !void {
    if (rob(&[_]i32{ 1, 2, 3, 1 }) != 4) return error.TestFailed;
    if (rob(&[_]i32{ 2, 7, 9, 3, 1 }) != 12) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 程序入口：跑内嵌自测用例
