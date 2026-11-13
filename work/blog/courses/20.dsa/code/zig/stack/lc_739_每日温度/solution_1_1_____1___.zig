// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233913
// LeetCode 739. 每日温度 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn dailyTemperatures(t: []const i32, out: []i32) void { // 定义函数/方法 dailyTemperatures
    const n = t.len; // 把 另一字符串.长度 存入 元素个数
    for (0..n) |i| out[i] = 0; // 让 下标 i 从 0 走到 元素个数 减一
    var st: [8192]usize = undefined; // 把 undefined; 写入 var st: [8192]usize
    var top: usize = 0; // 把 0; 写入 var top: usize
    for (0..n) |i| { // 让 下标 i 从 0 走到 元素个数 减一
        while (top > 0 and t[st[top - 1]] < t[i]) { // 循环，直到不满足「top 超过 0 and 另一字符串[st[top 减 1]] 小于 另一字符串[下标 i]」
            out[st[top - 1]] = @intCast(i - st[top - 1]); // 把 @intCast(下标 i 减 st[top 减 1]); 写入 out[st[top - 1]]
            top -= 1; // top累减 1
        }
        st[top] = i; // 把 下标 i; 写入 st[top]
        top += 1; // top累加 1
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out: [8]i32 = undefined; // 把 undefined; 写入 var out: [8]i32
    dailyTemperatures(&[_]i32{ 73, 74, 75, 71, 69, 72, 76, 73 }, &out);
    if (out[0] != 1 or out[2] != 4 or out[7] != 0) return error.TestFailed;
    dailyTemperatures(&[_]i32{ 30, 40, 50, 60 }, &out); // dailyTemperatures( 按位与 [_]i32{ 30, 40, 50, 60 }, 按位与 out);
    if (out[0] != 1 or out[3] != 0) return error.TestFailed; // 若 out[0] 不等于 1 or out[3] 不等于 0，直接返回 error.TestFailed
    dailyTemperatures(&[_]i32{ 30, 60, 90 }, &out); // dailyTemperatures( 按位与 [_]i32{ 30, 60, 90 }, 按位与 out);
    if (out[0] != 1 or out[2] != 0) return error.TestFailed; // 若 out[0] 不等于 1 or out[2] 不等于 0，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
