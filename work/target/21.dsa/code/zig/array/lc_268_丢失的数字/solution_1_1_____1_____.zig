// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133968437
// LeetCode 268. 丢失的数字 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn missingNumber(nums: []const i32) i32 { // 定义函数/方法 missingNumber
    const n: i64 = @intCast(nums.len); // 把 @intCast(数组.长度); 写入 const n: i64
    var sum: i64 = 0; // 把 0; 写入 var sum: i64
    for (nums) |v| sum += v; // 逐个取出 数组 的元素（值）
    return @intCast(@divTrunc(n * (n + 1), 2) - sum); // 返回 @intCast(@divTrunc(元素个数 乘 (元素个数 加 1), 2) 减 累计和)
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (missingNumber(&[_]i32{ 3, 0, 1 }) != 2) return error.TestFailed;
    if (missingNumber(&[_]i32{ 0, 1 }) != 2) return error.TestFailed;
    if (missingNumber(&[_]i32{ 9, 6, 4, 2, 3, 5, 7, 0, 1 }) != 8) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
