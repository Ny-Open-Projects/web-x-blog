// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130704336
// LeetCode 63. 不同路径II — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn uniquePathsWithObstacles(grid: []const []const i32) i32 { // 定义函数/方法 uniquePathsWithObstacles
    const m = grid.len; // 把 网格.长度 存入 映射表
    const n = grid[0].len; // 把 网格[0].长度 存入 元素个数
    var dp: [101]i32 = undefined; // 把 undefined; 写入 var dp: [101]i32
    for (0..101) |k| dp[k] = 0; // 让 下标 k 从 0 走到 101 减一
    dp[0] = if (grid[0][0] == 1) 0 else 1; // 把 if (网格[0][0] 等于 1) 0 else 1; 写入 dp[0]
    for (0..m) |i| { // 让 下标 i 从 0 走到 映射表 减一
        for (0..n) |j| { // 让 下标 j 从 0 走到 元素个数 减一
            if (grid[i][j] == 1) { // 若 网格[下标 i][下标 j] 等于 1
                dp[j] = 0; // 把 0; 写入 dp[j]
            } else if (j > 0) { // 否则，若 下标 j 超过 0
                dp[j] += dp[j - 1]; // dp[j]累加 DP 表[下标 j 减 1]
            }
        }
    }
    return dp[n - 1]; // 返回 DP 表[元素个数 减 1]
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    const r1 = [_]i32{ 0, 0, 0 }; // 把 [_]i32{ 0, 0, 0 } 存入 r1
    const r2 = [_]i32{ 0, 1, 0 }; // 把 [_]i32{ 0, 1, 0 } 存入 r2
    const r3 = [_]i32{ 0, 0, 0 }; // 把 [_]i32{ 0, 0, 0 } 存入 r3
    const g1 = [_][]const i32{ &r1, &r2, &r3 }; // 把 [_][]const i32{ 按位与 r1, 按位与 r2, 按位与 r3 } 存入 g1
    if (uniquePathsWithObstacles(&g1) != 2) return error.TestFailed;
    const s1 = [_]i32{ 0, 1 }; // 把 [_]i32{ 0, 1 } 存入 s1
    const s2 = [_]i32{ 0, 0 }; // 把 [_]i32{ 0, 0 } 存入 s2
    const g2 = [_][]const i32{ &s1, &s2 }; // 把 [_][]const i32{ 按位与 s1, 按位与 s2 } 存入 g2
    if (uniquePathsWithObstacles(&g2) != 1) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
