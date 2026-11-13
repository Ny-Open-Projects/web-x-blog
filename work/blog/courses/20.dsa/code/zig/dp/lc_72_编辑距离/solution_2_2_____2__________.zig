// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130540333
// LeetCode 72. 编辑距离 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn minDistance(w1: []const u8, w2: []const u8) i32 { // 定义函数/方法 minDistance
    const m = w1.len; // 把 w1.长度 存入 映射表
    const n = w2.len; // 把 w2.长度 存入 元素个数
    var dp: [1001]i32 = undefined; // 把 undefined; 写入 var dp: [1001]i32
    for (0..n + 1) |j| dp[j] = @intCast(j); // 把 @intCast(下标 j); 写入 for (0..n + 1) |j| dp[j]
    for (1..m + 1) |i| { // for (1..映射表 加 1) 按位或 下标 i 按位或 {
        var prev_diag = dp[0]; // 把 DP 表[0] 存入 prev_diag
        dp[0] = @intCast(i); // 把 @intCast(下标 i); 写入 dp[0]
        for (1..n + 1) |j| { // for (1..元素个数 加 1) 按位或 下标 j 按位或 {
            const tmp = dp[j]; // 把 DP 表[下标 j] 存入 临时变量
            dp[j] = if (w1[i - 1] == w2[j - 1]) prev_diag else 1 + @min(prev_diag, @min(dp[j], dp[j - 1]));
            prev_diag = tmp; // 把 临时变量; 写入 prev_diag
        }
    }
    return dp[n]; // 返回 DP 表[元素个数]
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (minDistance("horse", "ros") != 3) return error.TestFailed; // 若 minDistance(「horse」, 「horse」) 不等于 3，直接返回 error.TestFailed
    if (minDistance("intention", "execution") != 5) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
