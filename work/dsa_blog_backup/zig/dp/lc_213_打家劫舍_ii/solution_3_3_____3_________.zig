// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130716392
// LeetCode 213. 打家劫舍II — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn robLine(nums: []const i32) i32 {
    var a: i32 = 0;
    var b: i32 = 0;
    for (nums) |v| {
        const t = @max(b, a + v);
        a = b;
        b = t;
    }
    return b;
} // 定义函数/方法 robLine
fn robII(nums: []const i32) i32 { // 定义函数/方法 robII
    if (nums.len == 1) return nums[0]; // 若 数组.长度 等于 1，直接返回 数组[0]
    const r1 = robLine(nums[1..]); // 把 robLine(数组[1..]) 存入 r1
    const r2 = robLine(nums[0 .. nums.len - 1]); // 把 robLine(数组[0 .. 数组.长度 减 1]) 存入 r2
    return @max(r1, r2); // 返回 @取较大值 r1, r2)
}
pub fn main() !void {
    if (robII(&[_]i32{ 2, 3, 2 }) != 3) return error.TestFailed;
    if (robII(&[_]i32{ 1, 2, 3, 1 }) != 4) return error.TestFailed;
    if (robII(&[_]i32{1}) != 1) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 程序入口：跑内嵌自测用例
