// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133807379
// LeetCode 209. 长度最小的子数组 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn minSubArrayLen(target: i32, nums: []const i32) i32 { // 定义函数/方法 minSubArrayLen
    var l: usize = 0; // 把 0; 写入 var l: usize
    var sum: i64 = 0; // 把 0; 写入 var sum: i64
    var best: i32 = std.math.maxInt(i32); // 把 std.math.maxInt(i32); 写入 var best: i32
    for (nums, 0..) |v, r| { // for (数组, 0..) 按位或 值, 右指针 按位或 {
        sum += v; // 累计和累加 值
        while (sum >= target) { // 循环，直到不满足「累计和 不低于 目标值」
            const len: i32 = @intCast(r - l + 1); // 把 @intCast(右指针 减 左指针 加 1); 写入 const len: i32
            if (len < best) best = len; // 若 长度 小于 当前最优) 当前最优 赋值为 长度;
            sum -= nums[l]; // 累计和累减 数组[左指针]
            l += 1; // 左指针累加 1
        }
    }
    return if (best == std.math.maxInt(i32)) 0 else best; // 返回 if (当前最优 等于 std.math.maxInt(i32)) 0 else 当前最优
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (minSubArrayLen(7, &[_]i32{ 2, 3, 1, 2, 4, 3 }) != 2) return error.TestFailed;
    if (minSubArrayLen(4, &[_]i32{ 1, 4, 4 }) != 1) return error.TestFailed;
    if (minSubArrayLen(11, &[_]i32{ 1, 1, 1, 1, 1, 1, 1, 1 }) != 0) return error.TestFailed;
    if (minSubArrayLen(1, &[_]i32{ 1, 2, 3 }) != 1) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
