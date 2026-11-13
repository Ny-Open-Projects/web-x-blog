// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107573690
// 抽象思维之对比算法 发现共性 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn climbStairsRefactored(n: i32) i64 { // 定义函数/方法 climbStairsRefactored
    if (n == 0) return 1; // 若 元素个数 等于 0，直接返回 1
    if (n < 0) return 0; // 若 元素个数 小于 0，直接返回 0
    var dp: [64]i64 = undefined; // 把 undefined; 写入 var dp: [64]i64
    dp[0] = 1; // 把 1; 写入 dp[0]
    for (1..@intCast(n + 1)) |i| { // for (1..@intCast(元素个数 加 1)) 按位或 下标 i 按位或 {
        dp[i] = dp[i - 1]; // 把 DP 表[下标 i 减 1]; 写入 dp[i]
        if (i >= 2) dp[i] += dp[i - 2]; // 若 下标 i 不低于 2) DP 表[下标 i] 累加 DP 表[下标 i 减 2];
        if (i >= 3) dp[i] += dp[i - 3]; // 若 下标 i 不低于 3) DP 表[下标 i] 累加 DP 表[下标 i 减 3];
    }
    return dp[@intCast(n)]; // 返回 DP 表[@intCast(元素个数)]
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (climbStairsRefactored(10) != 274 or climbStairsRefactored(3) != 4) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
