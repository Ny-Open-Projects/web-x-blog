// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130683917
// LeetCode 322. 零钱兑换 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn coinChange(coins: []const i32, amount: i32) i32 { // 定义函数/方法 coinChange
    var dp: [10001]i64 = undefined; // 把 undefined; 写入 var dp: [10001]i64
    dp[0] = 0; // 把 0; 写入 dp[0]
    for (1..@intCast(amount + 1)) |a| dp[a] = 1 << 40; // 把 1 小于 小于 40; 写入 for (1..@intCast(amount + 1)) |a| dp[a]
    for (1..@intCast(amount + 1)) |ai| { // for (1..@intCast(目标金额 加 1)) 按位或 ai 按位或 {
        for (coins) |c| { // 逐个取出 硬币面额 的元素（字符）
            const ci: usize = @intCast(c); // 把 @intCast(字符); 写入 const ci: usize
            if (ci <= ai and dp[ai - ci] < (1 << 40)) { // 若 ci 不超过 ai and DP 表[ai 减 ci] 小于 (1 小于 小于 40
                if (dp[ai - ci] + 1 < dp[ai]) dp[ai] = dp[ai - ci] + 1;
            }
        }
    }
    const r = dp[@intCast(amount)]; // 把 DP 表[@intCast(目标金额)] 存入 右指针
    return if (r >= (1 << 40)) -1 else @intCast(r); // 返回 if (右指针 不低于 (1 小于 小于 40)) 减 1 else @intCast(右指针)
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (coinChange(&[_]i32{ 1, 2, 5 }, 11) != 3) return error.TestFailed;
    if (coinChange(&[_]i32{2}, 3) != -1) return error.TestFailed;
    if (coinChange(&[_]i32{1}, 0) != 0) return error.TestFailed; // 若 coinChange( 按位与 [_]i32{1}, 0) 不等于 0，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
