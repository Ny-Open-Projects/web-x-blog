// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130771847
// LeetCode 673. 最长递增子序列的个数 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn findNumberOfLIS(nums: []const i32) i32 { // 定义函数/方法 findNumberOfLIS
    const n = nums.len; // 把 数组.长度 存入 元素个数
    var dp: [4096]i32 = undefined; // 把 undefined; 写入 var dp: [4096]i32
    var cnt: [4096]i32 = undefined; // 把 undefined; 写入 var cnt: [4096]i32
    var best: i32 = 0; // 把 0; 写入 var best: i32
    var res: i32 = 0; // 把 0; 写入 var res: i32
    for (0..n) |i| { // 让 下标 i 从 0 走到 元素个数 减一
        dp[i] = 1; // 把 1; 写入 dp[i]
        cnt[i] = 1; // 把 1; 写入 cnt[i]
        for (0..i) |j| { // 让 下标 j 从 0 走到 下标 i 减一
            if (nums[j] < nums[i]) { // 若 数组[下标 j] 小于 数组[下标 i]
                if (dp[j] + 1 > dp[i]) { // 若 DP 表[下标 j] 加 1 超过 DP 表[下标 i]
                    dp[i] = dp[j] + 1; // 把 DP 表[下标 j] 加 1; 写入 dp[i]
                    cnt[i] = cnt[j]; // 把 计数[下标 j]; 写入 cnt[i]
                } else if (dp[j] + 1 == dp[i]) { // 否则，若 DP 表[下标 j] 加 1 等于 DP 表[下标 i]
                    cnt[i] += cnt[j]; // cnt[i]累加 计数[下标 j]
                }
            }
        }
        if (dp[i] > best) { // 若 DP 表[下标 i] 超过 当前最优
            best = dp[i]; // 把 DP 表[下标 i]; 写入 当前最优
            res = cnt[i]; // 把 计数[下标 i]; 写入 结果
        } else if (dp[i] == best) { // 否则，若 DP 表[下标 i] 等于 当前最优
            res += cnt[i]; // 结果累加 计数[下标 i]
        }
    }
    return res; // 返回 结果
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (findNumberOfLIS(&[_]i32{ 1, 3, 5, 4, 7 }) != 2) return error.TestFailed;
    if (findNumberOfLIS(&[_]i32{ 2, 2, 2, 2, 2 }) != 5) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
