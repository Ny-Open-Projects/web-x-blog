// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130641517
// LeetCode 62. 不同路径 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn uniquePaths(m: i32, n: i32) i32 { // 定义函数/方法 uniquePaths
    var dp: [101]i32 = undefined; // 把 undefined; 写入 var dp: [101]i32
    for (0..@intCast(n)) |j| dp[j] = 1; // 把 1; 写入 for (0..@intCast(n)) |j| dp[j]
    var i: i32 = 1; // 把 1; 写入 var i: i32
    while (i < m) : (i += 1) { // 循环，直到不满足「下标 i 小于 映射表) : (下标 i 累加 1」
        var j: usize = 1; // 把 1; 写入 var j: usize
        while (j < @as(usize, @intCast(n))) : (j += 1) dp[j] += dp[j - 1];
    }
    return dp[@intCast(n - 1)]; // 返回 DP 表[@intCast(元素个数 减 1)]
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (uniquePaths(3, 7) != 28) return error.TestFailed; // 若 uniquePaths(3, 7) 不等于 28，直接返回 error.TestFailed
    if (uniquePaths(3, 2) != 3) return error.TestFailed; // 若 uniquePaths(3, 2) 不等于 3，直接返回 error.TestFailed
    if (uniquePaths(1, 1) != 1) return error.TestFailed; // 若 uniquePaths(1, 1) 不等于 1，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
