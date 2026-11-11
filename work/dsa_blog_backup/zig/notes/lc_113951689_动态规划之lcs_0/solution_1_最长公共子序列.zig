// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689
// LeetCode 113951689. 动态规划之 LCS — Zig 版（最长公共子序列：DP 填表 + 回溯构造）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn lcsTable(a: []const u8, b: []const u8, dp: *[65][65]usize) usize { // 定义函数/方法 lcsTable
    const m = a.len; // 把 数组.长度 存入 映射表
    const n = b.len; // 把 b.长度 存入 元素个数
    for (0..m + 1) |i| { // for (0..映射表 加 1) 按位或 下标 i 按位或 {
        for (0..n + 1) |j| dp[i][j] = 0; // 把 0; 写入 for (0..n + 1) |j| dp[i][j]
    }
    for (1..m + 1) |i| { // for (1..映射表 加 1) 按位或 下标 i 按位或 {
        for (1..n + 1) |j| { // for (1..元素个数 加 1) 按位或 下标 j 按位或 {
            dp[i][j] = if (a[i - 1] == b[j - 1]) // 把 if (数组[下标 i 减 1] 等于 b[下标 j 减 1]) 写入 dp[i][j]
                dp[i - 1][j - 1] + 1 // DP 表[下标 i 减 1][下标 j 减 1] 加 1
            else // 否则
                @max(dp[i - 1][j], dp[i][j - 1]); // @取较大值 DP 表[下标 i 减 1][下标 j], DP 表[下标 i][下标 j 减 1]);
        }
    }
    return dp[m][n]; // 返回 DP 表[映射表][元素个数]
}

fn lcsLength(a: []const u8, b: []const u8) usize { // 定义函数/方法 lcsLength
    var dp: [65][65]usize = undefined; // 把 undefined; 写入 var dp: [65][65]usize
    return lcsTable(a, b, &dp); // 返回 lcsTable(数组, b, 按位与 DP 表)
}

fn lcsString(buf: []u8, a: []const u8, b: []const u8) ![]u8 { // 定义函数/方法 lcsString
    var dp: [65][65]usize = undefined; // 把 undefined; 写入 var dp: [65][65]usize
    _ = lcsTable(a, b, &dp); // 把 lcsTable(数组, b, 按位与 DP 表); 写入 _
    var i = a.len; // 把 数组.长度 存入 下标 i
    var j = b.len; // 把 b.长度 存入 下标 j
    var tmp: [64]u8 = undefined; // 把 undefined; 写入 var tmp: [64]u8
    var k: usize = 0; // 把 0; 写入 var k: usize
    while (i > 0 and j > 0) { // 循环，直到不满足「下标 i 超过 0 and 下标 j 超过 0」
        if (a[i - 1] == b[j - 1]) { // 若 数组[下标 i 减 1] 等于 b[下标 j 减 1]
            tmp[k] = a[i - 1]; // 把 数组[下标 i 减 1]; 写入 tmp[k]
            k += 1; // 下标 k累加 1
            i -= 1; // 下标 i累减 1
            j -= 1; // 下标 j累减 1
        } else if (dp[i - 1][j] >= dp[i][j - 1]) { // 否则，若 DP 表[下标 i 减 1][下标 j] 不低于 DP 表[下标 i][下标 j 减 1]
            i -= 1; // 下标 i累减 1
        } else { // 否则
            j -= 1; // 下标 j累减 1
        }
    }
    for (0..k) |t| buf[t] = tmp[k - 1 - t]; // 让 另一字符串 从 0 走到 下标 k 减一
    return buf[0..k]; // 返回 buf[0..下标 k]
}

fn isCommonSub(a: []const u8, b: []const u8, s: []const u8) bool { // 定义判定函数 isCommonSub
    var ia: usize = 0; // 把 0; 写入 var ia: usize
    var ib: usize = 0; // 把 0; 写入 var ib: usize
    for (s) |ch| { // 逐个取出 字符串 的元素（字符）
        while (ia < a.len and a[ia] != ch) ia += 1; // 循环，直到不满足「ia 小于 数组.长度 and 数组[ia] 不等于 字符) ia 累加 1;」
        while (ib < b.len and b[ib] != ch) ib += 1; // 循环，直到不满足「ib 小于 b.长度 and b[ib] 不等于 字符) ib 累加 1;」
        if (ia >= a.len or ib >= b.len) return false; // 若 ia 不低于 数组.长度 or ib 不低于 b.长度，直接返回 false
        ia += 1; // ia累加 1
        ib += 1; // ib累加 1
    }
    return true; // 返回 true
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const Case = struct { a: []const u8, b: []const u8, want: usize };
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .a = "ABCBDAB", .b = "BDCABA", .want = 4 },
        .{ .a = "AGGTAB", .b = "GXTXAYB", .want = 4 },
        .{ .a = "abc", .b = "abc", .want = 3 },
        .{ .a = "", .b = "abc", .want = 0 },
        .{ .a = "abc", .b = "xyz", .want = 0 },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        const got = lcsLength(c.a, c.b); // 把 lcsLength(字符.数组, 字符.b) 存入 got
        if (got != c.want) { // 若 got 不等于 字符.want
            std.debug.print("case {d} failed: got {d} want {d}\n", .{ idx, got, c.want }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    const pairs = [_][2][]const u8{ // 把 [_][2][]const u8{ 存入 pairs
        .{ "ABCBDAB", "BDCABA" },
        .{ "AGGTAB", "GXTXAYB" },
    };
    var buf: [64]u8 = undefined; // 把 undefined; 写入 var buf: [64]u8
    for (pairs) |p| { // 逐个取出 pairs 的元素（节点）
        const s = try lcsString(&buf, p[0], p[1]); // 把 try lcsString( 按位与 buf, 节点[0], 节点[1]) 存入 字符串
        if (s.len != lcsLength(p[0], p[1]) or !isCommonSub(p[0], p[1], s)) {
            std.debug.print("lcsString failed: {s}\n", .{s}); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
