// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734179
// LeetCode 518. 零钱兑换II — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn change(amount: i32, coins: []const i32) i32 { // 定义函数/方法 change
    var dp: [10001]i64 = undefined; // 把 undefined; 写入 var dp: [10001]i64
    dp[0] = 1; // 把 1; 写入 dp[0]
    for (1..@intCast(amount + 1)) |a| dp[a] = 0; // 把 0; 写入 for (1..@intCast(amount + 1)) |a| dp[a]
    for (coins) |c| { // 逐个取出 硬币面额 的元素（字符）
        const ci: usize = @intCast(c); // 把 @intCast(字符); 写入 const ci: usize
        var a = ci; // 把 ci 存入 数组
        while (a <= @as(usize, @intCast(amount))) : (a += 1) dp[a] += dp[a - ci];
    }
    return @intCast(dp[@intCast(amount)]); // 返回 @intCast(DP 表[@intCast(目标金额)])
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (change(5, &[_]i32{ 1, 2, 5 }) != 4) return error.TestFailed;
    if (change(3, &[_]i32{2}) != 0) return error.TestFailed; // 若 change(3, 按位与 [_]i32{2}) 不等于 0，直接返回 error.TestFailed
    if (change(10, &[_]i32{ 1, 2, 5 }) != 10) return error.TestFailed;
    if (change(0, &[_]i32{ 1, 2 }) != 1) return error.TestFailed; // 若 change(0, 按位与 [_]i32{ 1, 2 }) 不等于 1，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
