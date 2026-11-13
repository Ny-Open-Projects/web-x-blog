// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136236962
// LeetCode 1685. 有序数组中差绝对值之和 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn getSumAbsoluteDifferences(nums: []const i32, out: []i32) void { // 定义函数/方法 getSumAbsoluteDifferences
    const n = nums.len; // 把 数组.长度 存入 元素个数
    var total: i64 = 0; // 把 0; 写入 var total: i64
    for (nums) |v| total += v; // 逐个取出 数组 的元素（值）
    var prefix: i64 = 0; // 把 0; 写入 var prefix: i64
    for (0..n) |i| { // 让 下标 i 从 0 走到 元素个数 减一
        const v: i64 = nums[i]; // 把 数组[下标 i]; 写入 const v: i64
        const left = v * @as(i64, @intCast(i)) - prefix; // 把 值 乘 @as(i64, @intCast(下标 i)) 减 prefix 存入 左边界
        const right = (total - prefix - v) - v * @as(i64, @intCast(n - 1 - i));
        out[i] = @intCast(left + right); // 把 @intCast(左边界 加 右边界); 写入 out[i]
        prefix += v; // prefix累加 值
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out: [8]i32 = undefined; // 把 undefined; 写入 var out: [8]i32
    getSumAbsoluteDifferences(&[_]i32{ 2, 3, 5 }, &out); // getSumAbsoluteDifferences( 按位与 [_]i32{ 2, 3, 5 }, 按位与 out);
    if (out[0] != 4 or out[2] != 5) return error.TestFailed; // 若 out[0] 不等于 4 or out[2] 不等于 5，直接返回 error.TestFailed
    var out2: [8]i32 = undefined; // 把 undefined; 写入 var out2: [8]i32
    getSumAbsoluteDifferences(&[_]i32{ 1, 4, 6, 8, 10 }, &out2);
    if (out2[0] != 24 or out2[2] != 13 or out2[4] != 21) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
