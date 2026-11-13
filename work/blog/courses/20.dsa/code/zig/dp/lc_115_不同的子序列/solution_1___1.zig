// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130590161
// LeetCode 115. 不同的子序列 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn numDistinct(s: []const u8, t: []const u8) i32 { // 定义函数/方法 numDistinct
    const m = s.len; // 把 字符串.长度 存入 映射表
    const n = t.len; // 把 另一字符串.长度 存入 元素个数
    var dp: [1001]i64 = undefined; // 把 undefined; 写入 var dp: [1001]i64
    dp[0] = 1; // 把 1; 写入 dp[0]
    for (1..n + 1) |j| dp[j] = 0; // 把 0; 写入 for (1..n + 1) |j| dp[j]
    for (1..m + 1) |i| { // for (1..映射表 加 1) 按位或 下标 i 按位或 {
        var j: usize = n; // 把 元素个数; 写入 var j: usize
        while (j >= 1) : (j -= 1) { // 循环，直到不满足「下标 j 不低于 1) : (下标 j 累减 1」
            if (s[i - 1] == t[j - 1]) dp[j] += dp[j - 1];
            if (j == 1) break; // 若 下标 j 等于 1) break;
        }
    }
    return @intCast(dp[n]); // 返回 @intCast(DP 表[元素个数])
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (numDistinct("rabbbit", "rabbit") != 3) return error.TestFailed;
    if (numDistinct("babgbag", "bag") != 5) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
