// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133907522
// LeetCode 238. 除自身以外数组的乘积 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn productExceptSelf(nums: []const i32, out: []i32) void { // 定义函数/方法 productExceptSelf
    const n = nums.len; // 把 数组.长度 存入 元素个数
    var left: i64 = 1; // 把 1; 写入 var left: i64
    for (0..n) |i| {
        out[i] = @intCast(left);
        left *= nums[i];
    } // 让 下标 i 从 0 走到 元素个数 减一
    var right: i64 = 1; // 把 1; 写入 var right: i64
    var i: usize = n; // 把 元素个数; 写入 var i: usize
    while (i > 0) {
        i -= 1;
        out[i] = @intCast(@as(i64, out[i]) * right);
        right *= nums[i];
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out: [8]i32 = undefined; // 把 undefined; 写入 var out: [8]i32
    productExceptSelf(&[_]i32{ 1, 2, 3, 4 }, &out); // productExceptSelf( 按位与 [_]i32{ 1, 2, 3, 4 }, 按位与 out);
    if (out[0] != 24 or out[3] != 6) return error.TestFailed; // 若 out[0] 不等于 24 or out[3] 不等于 6，直接返回 error.TestFailed
    productExceptSelf(&[_]i32{ -1, 1, 0, -3, 3 }, &out);
    if (out[0] != 0 or out[2] != 9) return error.TestFailed; // 若 out[0] 不等于 0 or out[2] 不等于 9，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
