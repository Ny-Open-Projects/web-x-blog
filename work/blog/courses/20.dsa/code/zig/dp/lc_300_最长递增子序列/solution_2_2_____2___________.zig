// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130727613
// LeetCode 300. 最长递增子序列 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn lengthOfLIS(nums: []const i32) i32 { // 定义函数/方法 lengthOfLIS
    var dp: [4096]i32 = undefined; // 把 undefined; 写入 var dp: [4096]i32
    var best: i32 = 0; // 把 0; 写入 var best: i32
    for (0..nums.len) |i| { // 逐个取出 0..数组.长度 的元素（下标 i）
        dp[i] = 1; // 把 1; 写入 dp[i]
        for (0..i) |j| { // 让 下标 j 从 0 走到 下标 i 减一
            if (nums[j] < nums[i] and dp[j] + 1 > dp[i]) dp[i] = dp[j] + 1;
        }
        if (dp[i] > best) best = dp[i]; // 若 DP 表[下标 i] 超过 当前最优) 当前最优 赋值为 DP 表[下标 i];
    }
    return best; // 返回 当前最优
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (lengthOfLIS(&[_]i32{ 10, 9, 2, 5, 3, 7, 101, 18 }) != 4) return error.TestFailed;
    if (lengthOfLIS(&[_]i32{ 0, 1, 0, 3, 2, 3 }) != 4) return error.TestFailed;
    if (lengthOfLIS(&[_]i32{ 7, 7, 7, 7 }) != 1) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
