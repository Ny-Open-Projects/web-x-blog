// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133834060
// LeetCode 2407. 最长递增子序列II — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn lengthOfLIS(nums: []const i32, k: i32) i32 { // 定义函数/方法 lengthOfLIS
    const n = nums.len; // 把 数组.长度 存入 元素个数
    var dp: [4096]i32 = undefined; // 把 undefined; 写入 var dp: [4096]i32
    var best: i32 = 0; // 把 0; 写入 var best: i32
    for (0..n) |i| { // 让 下标 i 从 0 走到 元素个数 减一
        dp[i] = 1; // 把 1; 写入 dp[i]
        for (0..i) |j| { // 让 下标 j 从 0 走到 下标 i 减一
            if (nums[j] < nums[i] and nums[i] - nums[j] <= k and dp[j] + 1 > dp[i]) dp[i] = dp[j] + 1;
        }
        if (dp[i] > best) best = dp[i]; // 若 DP 表[下标 i] 超过 当前最优) 当前最优 赋值为 DP 表[下标 i];
    }
    return best; // 返回 当前最优
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (lengthOfLIS(&[_]i32{ 4, 2, 1, 4, 3, 4, 5, 8, 15 }, 3) != 5) return error.TestFailed;
    if (lengthOfLIS(&[_]i32{1}, 1) != 1) return error.TestFailed; // 若 lengthOfLIS( 按位与 [_]i32{1}, 1) 不等于 1，直接返回 error.TestFailed
    if (lengthOfLIS(&[_]i32{}, 3) != 0) return error.TestFailed; // 若 lengthOfLIS( 按位与 [_]i32{}, 3) 不等于 0，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
