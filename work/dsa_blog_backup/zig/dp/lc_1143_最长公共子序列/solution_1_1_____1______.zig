// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
// LeetCode 1143. 最长公共子序列 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn longestCommonSubsequence(t1: []const u8, t2: []const u8) i32 { // 定义函数/方法 longestCommonSubsequence
    const m = t1.len; // 把 t1.长度 存入 映射表
    const n = t2.len; // 把 t2.长度 存入 元素个数
    var dp: [1001]i32 = undefined; // 把 undefined; 写入 var dp: [1001]i32
    dp[0] = 0; // 把 0; 写入 dp[0]
    for (1..n + 1) |j| dp[j] = 0; // 把 0; 写入 for (1..n + 1) |j| dp[j]
    for (1..m + 1) |i| { // for (1..映射表 加 1) 按位或 下标 i 按位或 {
        var prev_diag: i32 = 0; // 把 0; 写入 var prev_diag: i32
        for (1..n + 1) |j| { // for (1..元素个数 加 1) 按位或 下标 j 按位或 {
            const tmp = dp[j]; // 把 DP 表[下标 j] 存入 临时变量
            dp[j] = if (t1[i - 1] == t2[j - 1]) prev_diag + 1 else @max(dp[j], dp[j - 1]);
            prev_diag = tmp; // 把 临时变量; 写入 prev_diag
        }
    }
    return dp[n]; // 返回 DP 表[元素个数]
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (longestCommonSubsequence("abcde", "ace") != 3) return error.TestFailed;
    if (longestCommonSubsequence("abc", "abc") != 3) return error.TestFailed;
    if (longestCommonSubsequence("abc", "def") != 0) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
